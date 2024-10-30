import grpc
import example_pb2
import example_pb2_grpc
import numpy as np
import json
def run():
    #创建一个不使用 TLS（传输层安全协议）的连接通道。这意味着数据在传输过程中不会被加密，也可创建加密的
    with grpc.insecure_channel('localhost:50051') as channel:
        #Stub对应的是客户端，Service对应的是服务端，调用Stub()生成客户端stub
        stub = example_pb2_grpc.StudentServiceStub(channel)
        # 添加学生
        scoreNumpy = np.array([[1, 2], [3, 4]],dtype=np.int64)
        socreByte = scoreNumpy.tobytes()
        my_dict = {"key1": 1, "key2": 2, "key3": 3}
        student_request = example_pb2.Student(
                name="董",
                age=20,
                scores = socreByte,  # Numpy 数组转字节流
                shape = list(scoreNumpy.shape),
                attributes=json.dumps(my_dict)
        )
        add_response = stub.AddStudent(student_request)
        print(f"Add Student Response: {add_response.message}, Student ID: {add_response.student_id}")
        # 获取学生信息
        get_request = example_pb2.GetStudentRequest(id=add_response.student_id)
        print(get_request.id)
        get_response = stub.GetStudent(get_request)
        print(
            f"Retrieved Student:Name={get_response.name}, Age={get_response.attributes}")

if __name__ == '__main__':
    run()