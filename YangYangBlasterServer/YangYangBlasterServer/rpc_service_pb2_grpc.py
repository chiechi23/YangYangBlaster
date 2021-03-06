# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rpc_service_pb2 as rpc__service__pb2


class RpcServiceStub(object):
    """The rpc service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RpcServiceExample = channel.unary_unary(
                '/yyb.RpcService/RpcServiceExample',
                request_serializer=rpc__service__pb2.RpcServiceExampleRequest.SerializeToString,
                response_deserializer=rpc__service__pb2.RpcServiceExampleReply.FromString,
                )
        self.Login = channel.unary_unary(
                '/yyb.RpcService/Login',
                request_serializer=rpc__service__pb2.LoginRequest.SerializeToString,
                response_deserializer=rpc__service__pb2.LoginReply.FromString,
                )


class RpcServiceServicer(object):
    """The rpc service definition.
    """

    def RpcServiceExample(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RpcServiceExample': grpc.unary_unary_rpc_method_handler(
                    servicer.RpcServiceExample,
                    request_deserializer=rpc__service__pb2.RpcServiceExampleRequest.FromString,
                    response_serializer=rpc__service__pb2.RpcServiceExampleReply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=rpc__service__pb2.LoginRequest.FromString,
                    response_serializer=rpc__service__pb2.LoginReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yyb.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """The rpc service definition.
    """

    @staticmethod
    def RpcServiceExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yyb.RpcService/RpcServiceExample',
            rpc__service__pb2.RpcServiceExampleRequest.SerializeToString,
            rpc__service__pb2.RpcServiceExampleReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yyb.RpcService/Login',
            rpc__service__pb2.LoginRequest.SerializeToString,
            rpc__service__pb2.LoginReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
