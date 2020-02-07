# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pyvelociraptor import api_pb2 as pyvelociraptor_dot_api__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_stream(
        '/proto.API/Query',
        request_serializer=pyvelociraptor_dot_api__pb2.VQLCollectorArgs.SerializeToString,
        response_deserializer=pyvelociraptor_dot_api__pb2.VQLResponse.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_stream_rpc_method_handler(
          servicer.Query,
          request_deserializer=pyvelociraptor_dot_api__pb2.VQLCollectorArgs.FromString,
          response_serializer=pyvelociraptor_dot_api__pb2.VQLResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))