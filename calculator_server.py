# calculator server which is based on the gRPC protocol to provide its services

from concurrent import futures
import time

import grpc

import calculator_service_pb2
import calculator_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(calculator_service_pb2_grpc.CalculatorServicer):
    # function which services add requests
    def Add(self, request, context):
        sum = request.a + request.b;
        return calculator_service_pb2.AddReply(result=sum)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_service_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
