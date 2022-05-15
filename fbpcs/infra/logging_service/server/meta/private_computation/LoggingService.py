#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

import logging
import sys

from thrift.protocol.TProtocol import TProtocolException
from thrift.Thrift import (
    TApplicationException,
    TException,
    TFrozenDict,
    TMessageType,
    TType,
)
from thrift.TRecursive import fix_spec
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport

all_structs = []


class Iface(object):
    def putMetadata(self, request):
        """
        Parameters:
         - request

        """
        pass

    def getMetadata(self, request):
        """
        Parameters:
         - request

        """
        pass

    def listMetadata(self, request):
        """
        Parameters:
         - request

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def putMetadata(self, request):
        """
        Parameters:
         - request

        """
        self.send_putMetadata(request)
        return self.recv_putMetadata()

    def send_putMetadata(self, request):
        self._oprot.writeMessageBegin("putMetadata", TMessageType.CALL, self._seqid)
        args = putMetadata_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_putMetadata(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = putMetadata_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.invalid_request_error is not None:
            raise result.invalid_request_error
        if result.internal_server_error is not None:
            raise result.internal_server_error
        raise TApplicationException(
            TApplicationException.MISSING_RESULT, "putMetadata failed: unknown result"
        )

    def getMetadata(self, request):
        """
        Parameters:
         - request

        """
        self.send_getMetadata(request)
        return self.recv_getMetadata()

    def send_getMetadata(self, request):
        self._oprot.writeMessageBegin("getMetadata", TMessageType.CALL, self._seqid)
        args = getMetadata_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getMetadata(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getMetadata_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.invalid_request_error is not None:
            raise result.invalid_request_error
        if result.internal_server_error is not None:
            raise result.internal_server_error
        if result.not_found_error is not None:
            raise result.not_found_error
        raise TApplicationException(
            TApplicationException.MISSING_RESULT, "getMetadata failed: unknown result"
        )

    def listMetadata(self, request):
        """
        Parameters:
         - request

        """
        self.send_listMetadata(request)
        return self.recv_listMetadata()

    def send_listMetadata(self, request):
        self._oprot.writeMessageBegin("listMetadata", TMessageType.CALL, self._seqid)
        args = listMetadata_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_listMetadata(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = listMetadata_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.invalid_request_error is not None:
            raise result.invalid_request_error
        if result.internal_server_error is not None:
            raise result.internal_server_error
        raise TApplicationException(
            TApplicationException.MISSING_RESULT, "listMetadata failed: unknown result"
        )


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["putMetadata"] = Processor.process_putMetadata
        self._processMap["getMetadata"] = Processor.process_getMetadata
        self._processMap["listMetadata"] = Processor.process_listMetadata
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(
                TApplicationException.UNKNOWN_METHOD, "Unknown function %s" % (name)
            )
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_putMetadata(self, seqid, iprot, oprot):
        args = putMetadata_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = putMetadata_result()
        try:
            result.success = self._handler.putMetadata(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidRequestError as invalid_request_error:
            msg_type = TMessageType.REPLY
            result.invalid_request_error = invalid_request_error
        except InternalServerError as internal_server_error:
            msg_type = TMessageType.REPLY
            result.internal_server_error = internal_server_error
        except TApplicationException as ex:
            logging.exception("TApplication exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception("Unexpected exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(
                TApplicationException.INTERNAL_ERROR, "Internal error"
            )
        oprot.writeMessageBegin("putMetadata", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getMetadata(self, seqid, iprot, oprot):
        args = getMetadata_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getMetadata_result()
        try:
            result.success = self._handler.getMetadata(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidRequestError as invalid_request_error:
            msg_type = TMessageType.REPLY
            result.invalid_request_error = invalid_request_error
        except InternalServerError as internal_server_error:
            msg_type = TMessageType.REPLY
            result.internal_server_error = internal_server_error
        except NotFoundError as not_found_error:
            msg_type = TMessageType.REPLY
            result.not_found_error = not_found_error
        except TApplicationException as ex:
            logging.exception("TApplication exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception("Unexpected exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(
                TApplicationException.INTERNAL_ERROR, "Internal error"
            )
        oprot.writeMessageBegin("getMetadata", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_listMetadata(self, seqid, iprot, oprot):
        args = listMetadata_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = listMetadata_result()
        try:
            result.success = self._handler.listMetadata(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except InvalidRequestError as invalid_request_error:
            msg_type = TMessageType.REPLY
            result.invalid_request_error = invalid_request_error
        except InternalServerError as internal_server_error:
            msg_type = TMessageType.REPLY
            result.internal_server_error = internal_server_error
        except TApplicationException as ex:
            logging.exception("TApplication exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception("Unexpected exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(
                TApplicationException.INTERNAL_ERROR, "Internal error"
            )
        oprot.writeMessageBegin("listMetadata", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES


class putMetadata_args(object):
    """
    Attributes:
     - request

    """

    def __init__(
        self,
        request=None,
    ):
        self.request = request

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.request = PutMetadataRequest()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("putMetadata_args")
        if self.request is not None:
            oprot.writeFieldBegin("request", TType.STRUCT, 1)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(putMetadata_args)
putMetadata_args.thrift_spec = (
    None,  # 0
    (
        1,
        TType.STRUCT,
        "request",
        [PutMetadataRequest, None],
        None,
    ),  # 1
)


class putMetadata_result(object):
    """
    Attributes:
     - success
     - invalid_request_error
     - internal_server_error

    """

    def __init__(
        self,
        success=None,
        invalid_request_error=None,
        internal_server_error=None,
    ):
        self.success = success
        self.invalid_request_error = invalid_request_error
        self.internal_server_error = internal_server_error

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PutMetadataResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.invalid_request_error = InvalidRequestError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.internal_server_error = InternalServerError.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("putMetadata_result")
        if self.success is not None:
            oprot.writeFieldBegin("success", TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.invalid_request_error is not None:
            oprot.writeFieldBegin("invalid_request_error", TType.STRUCT, 1)
            self.invalid_request_error.write(oprot)
            oprot.writeFieldEnd()
        if self.internal_server_error is not None:
            oprot.writeFieldBegin("internal_server_error", TType.STRUCT, 2)
            self.internal_server_error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(putMetadata_result)
putMetadata_result.thrift_spec = (
    (
        0,
        TType.STRUCT,
        "success",
        [PutMetadataResponse, None],
        None,
    ),  # 0
    (
        1,
        TType.STRUCT,
        "invalid_request_error",
        [InvalidRequestError, None],
        None,
    ),  # 1
    (
        2,
        TType.STRUCT,
        "internal_server_error",
        [InternalServerError, None],
        None,
    ),  # 2
)


class getMetadata_args(object):
    """
    Attributes:
     - request

    """

    def __init__(
        self,
        request=None,
    ):
        self.request = request

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.request = GetMetadataRequest()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("getMetadata_args")
        if self.request is not None:
            oprot.writeFieldBegin("request", TType.STRUCT, 1)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(getMetadata_args)
getMetadata_args.thrift_spec = (
    None,  # 0
    (
        1,
        TType.STRUCT,
        "request",
        [GetMetadataRequest, None],
        None,
    ),  # 1
)


class getMetadata_result(object):
    """
    Attributes:
     - success
     - invalid_request_error
     - internal_server_error
     - not_found_error

    """

    def __init__(
        self,
        success=None,
        invalid_request_error=None,
        internal_server_error=None,
        not_found_error=None,
    ):
        self.success = success
        self.invalid_request_error = invalid_request_error
        self.internal_server_error = internal_server_error
        self.not_found_error = not_found_error

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = GetMetadataResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.invalid_request_error = InvalidRequestError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.internal_server_error = InternalServerError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.not_found_error = NotFoundError.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("getMetadata_result")
        if self.success is not None:
            oprot.writeFieldBegin("success", TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.invalid_request_error is not None:
            oprot.writeFieldBegin("invalid_request_error", TType.STRUCT, 1)
            self.invalid_request_error.write(oprot)
            oprot.writeFieldEnd()
        if self.internal_server_error is not None:
            oprot.writeFieldBegin("internal_server_error", TType.STRUCT, 2)
            self.internal_server_error.write(oprot)
            oprot.writeFieldEnd()
        if self.not_found_error is not None:
            oprot.writeFieldBegin("not_found_error", TType.STRUCT, 3)
            self.not_found_error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(getMetadata_result)
getMetadata_result.thrift_spec = (
    (
        0,
        TType.STRUCT,
        "success",
        [GetMetadataResponse, None],
        None,
    ),  # 0
    (
        1,
        TType.STRUCT,
        "invalid_request_error",
        [InvalidRequestError, None],
        None,
    ),  # 1
    (
        2,
        TType.STRUCT,
        "internal_server_error",
        [InternalServerError, None],
        None,
    ),  # 2
    (
        3,
        TType.STRUCT,
        "not_found_error",
        [NotFoundError, None],
        None,
    ),  # 3
)


class listMetadata_args(object):
    """
    Attributes:
     - request

    """

    def __init__(
        self,
        request=None,
    ):
        self.request = request

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.request = ListMetadataRequest()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("listMetadata_args")
        if self.request is not None:
            oprot.writeFieldBegin("request", TType.STRUCT, 1)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(listMetadata_args)
listMetadata_args.thrift_spec = (
    None,  # 0
    (
        1,
        TType.STRUCT,
        "request",
        [ListMetadataRequest, None],
        None,
    ),  # 1
)


class listMetadata_result(object):
    """
    Attributes:
     - success
     - invalid_request_error
     - internal_server_error

    """

    def __init__(
        self,
        success=None,
        invalid_request_error=None,
        internal_server_error=None,
    ):
        self.success = success
        self.invalid_request_error = invalid_request_error
        self.internal_server_error = internal_server_error

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ListMetadataResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.invalid_request_error = InvalidRequestError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.internal_server_error = InternalServerError.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("listMetadata_result")
        if self.success is not None:
            oprot.writeFieldBegin("success", TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.invalid_request_error is not None:
            oprot.writeFieldBegin("invalid_request_error", TType.STRUCT, 1)
            self.invalid_request_error.write(oprot)
            oprot.writeFieldEnd()
        if self.internal_server_error is not None:
            oprot.writeFieldBegin("internal_server_error", TType.STRUCT, 2)
            self.internal_server_error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(listMetadata_result)
listMetadata_result.thrift_spec = (
    (
        0,
        TType.STRUCT,
        "success",
        [ListMetadataResponse, None],
        None,
    ),  # 0
    (
        1,
        TType.STRUCT,
        "invalid_request_error",
        [InvalidRequestError, None],
        None,
    ),  # 1
    (
        2,
        TType.STRUCT,
        "internal_server_error",
        [InternalServerError, None],
        None,
    ),  # 2
)
fix_spec(all_structs)
del all_structs
