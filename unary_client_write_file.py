import grpc
import route_guide_pb2
import route_guide_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = route_guide_pb2_grpc.MyServiceStub(channel)

    request = route_guide_pb2.CreateFileRequest(file_name='newfile.txt', file_contents=b'')
    response = stub.CreateFile(request)
    if not response.success:
        print('Failed to create file.')
    
    request = route_guide_pb2.WriteFileRequest(file_name='newfile.txt', data=b'This is a text message')
    response = stub.WriteFile(request)
    if not response.success:
        print('Failed to write to file.')