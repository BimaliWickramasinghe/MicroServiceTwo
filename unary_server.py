import grpc
from concurrent import futures
import route_guide_pb2
import route_guide_pb2_grpc

class MyServiceServicer(route_guide_pb2_grpc.MyServiceServicer):
    def CreateFile(self, request, context):
        try:
            with open(request.file_name, 'wb') as f:
                f.write(request.file_contents)
            response = route_guide_pb2.CreateFileResponse(success=True)
        except:
            response = route_guide_pb2.CreateFileResponse(success=False)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
route_guide_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()