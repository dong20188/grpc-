from concurrent import futures
import grpc
import example_pb2
import example_pb2_grpc
import numpy as np
# 用于存储学生信息的简单数据库

class StudentService(example_pb2_grpc.StudentServiceServicer):
    students_db = {}
    next_student_id = 1
    def AddStudent(self, request, context):
        # 将接收到的字节流转换为 NumPy 数组
        scores = np.frombuffer(request.scores,dtype=np.int64).reshape(request.shape)
        print(scores)
        # 对数组进行某种处理，比如求平方
        sroces = scores ** 2
        print(sroces)
        student = request
        student_id = self.next_student_id
        self.next_student_id+=1
        # 存储学生信息
        self.students_db[student_id] = student
        return example_pb2.AddStudentResponse(
            message="Student added successfully.",
            student_id=student_id
        )

    def GetStudent(self, request, context):
        student_id = request.id
        student = self.students_db.get(student_id)
        # if student is None:
        #     context.set_details("Student not found!")
        #     context.set_code(grpc.StatusCode.NOT_FOUND)
        #     return student_pb2.GetStudentResponse()
        #不能省略name=
        return example_pb2.Student(name=student.name,age=student.age,scores=student.scores,shape=student.shape,attributes=student.attributes)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
