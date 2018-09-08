
# Client which which makes request to the calculator server using gRPC protocol


from __future__ import print_function

import grpc

import calculator_service_pb2
import calculator_service_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_service_pb2_grpc.CalculatorStub(channel)
        a_val = int(input(" Enter value of first number:"))
        b_val = int(input(" Enter value of second number:"))
        response = stub.Add(calculator_service_pb2.AddRequest(a=a_val, b = b_val))
    print("Add result received: %d" %response.result)


if __name__ == '__main__':
    run()
