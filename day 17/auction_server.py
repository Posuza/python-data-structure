import socket


class Server():

    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9191

    def main(self):

        auction_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        auction_server.bind((self.server_ip, self.server_port))

        auction_server.listen()

        print("Server listen on port:{} and ip{}".format(self.server_port, self.server_ip))

        try:
            while True:
                client, address = auction_server.accept()
                print("Accepted Connection from -{} : {}".format(address[0],address[1]))

                self.client_control(client)

        except Exception as err:
            print(err)


    def client_control(self,client):

        with client as sock:
            from_client =sock.recv(1024)

            data_list = from_client.decode("utf-8").split(' ')

            print(data_list)

            sock.send(bytes("Connection from server:","utf-8"))



if __name__ == "__main__":
    auction :Server =Server()
    auction.main()