import grpc
import route_guide_pb2
import route_guide_pb2_grpc

def read_file(stub, file_name):
    # Read the contents of the file on the server
    request = route_guide_pb2.ReadFileRequest(file_name=file_name)
    response = stub.ReadFile(request)
    if response.success:
        return response.file_contents
    else:
        return None

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.MyServiceStub(channel)
        file_name = 'newfile.txt'
        file_contents = read_file(stub, file_name)
        if file_contents:
            print('Contents of the file {}:'.format(file_name))
            print(file_contents.decode())
        else:
            print('Failed to read file {}.'.format(file_name))
