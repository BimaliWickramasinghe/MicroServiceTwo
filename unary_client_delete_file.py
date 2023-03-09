import grpc
import route_guide_pb2
import route_guide_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = route_guide_pb2_grpc.MyServiceStub(channel)
    request = route_guide_pb2.DeleteFileRequest(file_name='newfile.txt')
    response = stub.DeleteFile(request)
    if response.success:
        print('File deleted successfully!')
    else:
        print('Failed to delete file.')