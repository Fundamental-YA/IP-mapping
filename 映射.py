import socket
import threading
def port_forwarding(local_ip, local_port, remote_ip, remote_port):
    # 创建本地socket对象
    local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_socket.bind((local_ip, local_port))
    local_socket.listen(1)
    while True:
        # 接受本地客户端连接
        client_socket, client_address = local_socket.accept()
        print('本地客户端已连接：', client_address)
        # 创建远程socket对象
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((remote_ip, remote_port))
        print('已连接到远程服务器：', (remote_ip, remote_port))
        # 启动数据转发线程
        forward_thread = ForwardThread(client_socket, remote_socket)
        forward_thread.start()
class ForwardThread(threading.Thread):
    def __init__(self, client_socket, remote_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.remote_socket = remote_socket
    def run(self):
        while True:
            try:
                # 从本地客户端接收数据并转发到远程服务器
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.remote_socket.sendall(data)
            except:
                break
        self.client_socket.close()
        self.remote_socket.close()
# 设置本地IP及端口
local_ip = '192.168.1.100'
local_port = 8080
# 设置远程IP及端口
remote_ip = '外网IP'
remote_port = 8080
# 启动端口映射
port_forwarding(local_ip, local_port, remote_ip, remote_port)
