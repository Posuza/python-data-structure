import socket
import s_encrypt_and_decrypt
import ob

toReturn = None


class Server():

    def __init__(self):
        self.ob = ob.Ob()
        self.decrypt = s_encrypt_and_decrypt.A3Decryption()
        self.encrypt = s_encrypt_and_decrypt.A3Encryption()
        self.server_ip = "localhost"
        self.server_port = 9190

    def main(self):

        auction_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        auction_server.bind((self.server_ip, self.server_port))

        auction_server.listen()

        print("Server listen on port:{} and ip{}".format(self.server_port, self.server_ip))

        try:
            while True:
                client, address = auction_server.accept()
                print("Accepted Connection from -{} : {}".format(address[0], address[1]))

                self.client_control(client)

        except Exception as err:
            print(err)

    def client_control(self, client):

        with client as sock:
            from_client = sock.recv(1024)
            data_list = from_client.decode("utf-8")
            decrypted = self.decrypt.startDecryption(data_list)
            print("#:", decrypted)
            decrypted_list = decrypted.split(' ')
            ob_recv = self.ob.get_received(decrypted_list[0])
            print("Ob data:", ob_recv)

            data = ''
            if decrypted_list[0] == 'info':
                data = 'data received from client:' + decrypted_list[0]


            #

            encrypted = self.encrypt.start_encryption(data, 'servertcp')

            sock.send(bytes(encrypted, "utf-8"))
            ob_send = self.ob.send_data(data)
            print("Ob send:", ob_send)

    # def for_observer(self):
    #     # to_return = self.decrypted_data
    #     #
    #     # self.decrypted_data='n'
    #     return self.decrypted_data


class Data:
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    auction: Server = Server()
    auction.main()
