#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from abc import ABC
from dataclasses import dataclass, field

from typing import Optional, Type

from dataclasses_json import config, DataClassJsonMixin

from fbpcs.private_computation.stage_flows.private_computation_base_stage_flow import (
    PrivateComputationBaseStageFlow,
)


@dataclass
class BoltCreateInstanceArgs(ABC):
    pass


@dataclass
class BoltPlayerArgs:
    create_instance_args: BoltCreateInstanceArgs
    expected_result_path: Optional[str] = None


@dataclass
class BoltJob(DataClassJsonMixin):
    job_name: str
    publisher_bolt_args: BoltPlayerArgs
    partner_bolt_args: BoltPlayerArgs
    stage_flow: Type[PrivateComputationBaseStageFlow] = field(
        metadata={
            **config(
                # the enum will be represented as a list of its members, so we can
                # use the first enum member to get the class name
                encoder=lambda x: x[0].get_cls_name(),
                # if no value is provided in the yaml file, then the dataclass json
                # library will return the default stage flow. Otherwise, if it was
                # provided in the yaml file, we should decode the string.
                decoder=lambda x: x
                if x is PrivateComputationBaseStageFlow
                else PrivateComputationBaseStageFlow.cls_name_to_cls(x),
            )
        },
    )
