from concurrent import futures
import logging

import grpc

import hello_world_pb2
import hello_world_pb2_grpc


class Greeter(hello_world_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return hello_world_pb2.HelloReply(message='Hello {}'.format(request.name))
        
    # def SayHelloAgain(self, request, context):
    # 	return hello_world_pb2.HelloReply(message='Hello again '.format(request.name))



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

