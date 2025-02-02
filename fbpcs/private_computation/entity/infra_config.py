# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from dataclasses_json import DataClassJsonMixin
from fbpcs.common.entity.pcs_mpc_instance import PCSMPCInstance
from fbpcs.common.entity.stage_state_instance import StageStateInstance
from fbpcs.pid.entity.pid_instance import PIDInstance
from fbpcs.post_processing_handler.post_processing_instance import (
    PostProcessingInstance,
)
from fbpcs.private_computation.entity.pce_config import PCEConfig
from fbpcs.private_computation.entity.private_computation_status import (
    PrivateComputationInstanceStatus,
)


class PrivateComputationRole(Enum):
    PUBLISHER = "PUBLISHER"
    PARTNER = "PARTNER"


class PrivateComputationGameType(Enum):
    LIFT = "LIFT"
    ATTRIBUTION = "ATTRIBUTION"


UnionedPCInstance = Union[
    PIDInstance, PCSMPCInstance, PostProcessingInstance, StageStateInstance
]


@dataclass
class InfraConfig(DataClassJsonMixin):
    """Stores metadata of infra config in a private computation instance

    Public attributes:
        mpc_compute_concurrency: number of threads to run per container at the MPC compute metrics stage

    Private attributes:
        _stage_flow_cls_name: the name of a PrivateComputationBaseStageFlow subclass (cls.__name__)
    """

    instance_id: str
    role: PrivateComputationRole
    status: PrivateComputationInstanceStatus
    status_update_ts: int
    instances: List[UnionedPCInstance]
    game_type: PrivateComputationGameType
    num_pid_containers: int
    num_mpc_containers: int
    num_files_per_mpc_container: int

    tier: Optional[str] = None
    pce_config: Optional[PCEConfig] = None

    # stored as a string because the enum was refusing to serialize to json, no matter what I tried.
    # TODO(T103299005): [BE] Figure out how to serialize StageFlow objects to json instead of using their class name
    _stage_flow_cls_name: str = "PrivateComputationStageFlow"

    retry_counter: int = 0
    creation_ts: int = field(default_factory=lambda: int(time.time()))
    end_ts: int = 0
    mpc_compute_concurrency: int = 1

    def __post_init__(self) -> None:
        # TODO: I will create hook for this check later
        if self.num_pid_containers > self.num_mpc_containers:
            raise ValueError(
                f"num_pid_containers must be less than or equal to num_mpc_containers. Received num_pid_containers = {self.num_pid_containers} and num_mpc_containers = {self.num_mpc_containers}"
            )
