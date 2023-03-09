import grpc
import route_guide_pb2
import route_guide_pb2_grpc

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = route_guide_pb2_grpc.MyServiceStub(channel)

        file_path = "newfile.txt"

        request = route_guide_pb2.ReadFileRequest(file_path=file_path)
        response = stub.ReadFile(request)

        file_contents = response.file_contents
        if file_contents:
            print(f"Contents of the file {file_path}:")
            print(file_contents.decode())
        else:
            print (response)
            print(f"Failed to read file {file_path}.")
