import grpc
from concurrent import futures
import route_guide_pb2
import route_guide_pb2_grpc
import os

class MyServiceServicer(route_guide_pb2_grpc.MyServiceServicer):
    def CreateFile(self, request, context):
        try:
            with open(request.file_name, 'wb') as f:
                f.write(request.file_contents)
            response = route_guide_pb2.CreateFileResponse(success=True)
        except:
            response = route_guide_pb2.CreateFileResponse(success=False)
        return response
    
    def DeleteFile(self, request, context):
        try:
            os.remove(request.file_name)
            response = route_guide_pb2.DeleteFileResponse(success=True)
        except:
            response = route_guide_pb2.DeleteFileResponse(success=False)
        return response
    
    def WriteFile(self, request, context):
        try:
            with open(request.file_name, 'ab') as f:
                f.write(request.data)
            response = route_guide_pb2.WriteFileResponse(success=True)
        except:
            response = route_guide_pb2.WriteFileResponse(success=False)
        return response
    
    def ReadFile(self, request, context):
        try:
            with open(request.file_path, 'rb') as f:
                file_contents = f.read()
            return route_guide_pb2.ReadFileResponse(success=True, file_contents=file_contents.encode())
        except Exception as e:
            return route_guide_pb2.ReadFileResponse(success=False, error_message=str(e))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started and listening on port 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()