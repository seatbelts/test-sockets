import socket

if __name__ == '__main__':
    host = '192.168.0.16'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    
    print "Conexion desde (ip, puerto): " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print str(data)
    c.close()
    
