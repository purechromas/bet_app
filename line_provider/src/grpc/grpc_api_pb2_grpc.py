# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from line_provider.src.grpc import (
    grpc_api_pb2 as line__provider_dot_src_dot_grpc_dot_grpc__api__pb2,
)

GRPC_GENERATED_VERSION = "1.66.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in line_provider/src/grpc/grpc_api_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class LineProviderServiceStub(object):
    """Line Provider gRPC сервис"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEvent = channel.unary_unary(
            "/event_provider.LineProviderService/CreateEvent",
            request_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventRequest.SerializeToString,
            response_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventResponse.FromString,
            _registered_method=True,
        )
        self.GetEvent = channel.unary_unary(
            "/event_provider.LineProviderService/GetEvent",
            request_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventRequest.SerializeToString,
            response_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventResponse.FromString,
            _registered_method=True,
        )
        self.GetListEvents = channel.unary_unary(
            "/event_provider.LineProviderService/GetListEvents",
            request_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsRequest.SerializeToString,
            response_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsResponse.FromString,
            _registered_method=True,
        )
        self.UpdateEventStatus = channel.unary_unary(
            "/event_provider.LineProviderService/UpdateEventStatus",
            request_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusRequest.SerializeToString,
            response_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusResponse.FromString,
            _registered_method=True,
        )


class LineProviderServiceServicer(object):
    """Line Provider gRPC сервис"""

    def CreateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetListEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateEventStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_LineProviderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateEvent": grpc.unary_unary_rpc_method_handler(
            servicer.CreateEvent,
            request_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventRequest.FromString,
            response_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventResponse.SerializeToString,
        ),
        "GetEvent": grpc.unary_unary_rpc_method_handler(
            servicer.GetEvent,
            request_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventRequest.FromString,
            response_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventResponse.SerializeToString,
        ),
        "GetListEvents": grpc.unary_unary_rpc_method_handler(
            servicer.GetListEvents,
            request_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsRequest.FromString,
            response_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsResponse.SerializeToString,
        ),
        "UpdateEventStatus": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateEventStatus,
            request_deserializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusRequest.FromString,
            response_serializer=line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("event_provider.LineProviderService", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("event_provider.LineProviderService", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class LineProviderService(object):
    """Line Provider gRPC сервис"""

    @staticmethod
    def CreateEvent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_provider.LineProviderService/CreateEvent",
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventRequest.SerializeToString,
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.CreateEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetEvent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_provider.LineProviderService/GetEvent",
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventRequest.SerializeToString,
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetListEvents(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_provider.LineProviderService/GetListEvents",
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsRequest.SerializeToString,
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.GetListEventsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def UpdateEventStatus(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_provider.LineProviderService/UpdateEventStatus",
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusRequest.SerializeToString,
            line__provider_dot_src_dot_grpc_dot_grpc__api__pb2.UpdateEventStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
