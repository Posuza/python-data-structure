import socket

class TCPserver():

    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 9997
        self.save_to = {}

    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip,self.server_port))
        server.listen()
        print("Server listen on port: {}  and  ip {}".format(self.server_port,self.server_ip))
        try:
            while True:
                client, address = server.accept()
                print("Accepted connection from - {} : {} ".format(address[0],address[1]))
                self.handle_client(client)
               
        except Exception as err:
            print(err)

    def handle_client(self,client_socket):
        with client_socket as sock:
            from_client = sock.recv(1024)
            receive_data = from_client.decode("utf-8")
            if receive_data == "gad":
                print(self.save_to)
                message = str(self.save_to)
                to_send = bytes(message,'utf-8')
                sock.send(to_send)
                
            else:
                print("Recived Data from client: {} ".format(receive_data))
                self.save_to.update({len(self.save_to):receive_data})

                message = "server got it:>" + receive_data
                to_send = bytes(message,'utf-8')
                sock.send(to_send)


if __name__ == '__main__':
    tcpserver = TCPserver()
    tcpserver.main()