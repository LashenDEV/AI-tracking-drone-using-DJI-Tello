import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8890))

while True:
    try:
        data, addr = sock.recvfrom(1024)
        print(data.decode())
    except Exception as e:
        print(e)
        sock.close()
        break
