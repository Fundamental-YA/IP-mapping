import subprocess
def port_forwarding(local_ip, local_port, remote_ip, remote_port):
    # 构造命令行命令
    command = f"netsh interface portproxy add v4tov4 listenaddress={local_ip} listenport={local_port} connectaddress={remote_ip} connectport={remote_port}"
    
    try:
        # 执行命令行命令
        subprocess.run(command, shell=True, check=True)
        print("端口映射已成功设置！")
    except subprocess.CalledProcessError as e:
        print(f"端口映射设置失败：{e}")
if __name__ == "__main__":
    # 获取用户输入的参数
    local_ip = input("请输入内网IP地址：")
    local_port = input("请输入内网端口号：")
    remote_ip = input("请输入外网IP地址：")
    remote_port = input("请输入外网端口号：")
    
    # 调用函数进行端口映射
    port_forwarding(local_ip, local_port, remote_ip, remote_port)
#这是另一种方法，须管理员权限用cmd运行，路由器也要有相应的调整，我没弄明白。。。
