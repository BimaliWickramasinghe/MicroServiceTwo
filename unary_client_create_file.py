import grpc
import route_guide_pb2
import route_guide_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = route_guide_pb2_grpc.MyServiceStub(channel)
    with open('test.txt', 'rb') as f:
        contents = f.read()
    request = route_guide_pb2.CreateFileRequest(file_name='newfile.txt', file_contents=contents)
    response = stub.CreateFile(request)
    if response.success:
        print('File created successfully!')
    else:
        print('Failed to create file.')