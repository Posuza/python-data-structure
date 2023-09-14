import socket

import encry_decrypt


class Auction_client():

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9191

        self.encryption()

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client  # to send and received data

    def client_menu(self):
        print("This is client menu:")
        user_data = input("Press 1 to send data:")

        client = self.client_runner()
        client.send(bytes("A3", "utf-8"))

        recv_info = client.recv(4096)

        print(recv_info.decode("utf-8"))

    def encryption(self):
        userKey: str = input("Enter your encryption key for the whole process:")
        encry = encry_decrypt.A3Encryption()
        encrypted_data =encry.start_encryption("NationalCyberCity",userKey)
        print(encrypted_data)



if __name__ == "__main__":
    auction_client: Auction_client = Auction_client()

    while True:
        auction_client.client_menu()
