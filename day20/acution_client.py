import socket
import encry_decrypt


class Auction_client():

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9190
        self.userKey = self.getting_key()
        self.client_menu()

    def getting_key(self):
        userKey: str = input("Enter your encryption key for the whole process:")
        return userKey

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client  # to send and received data

    def client_menu(self):
        print("This is client menu:")
        user_data = input("'get:Get_all_information\n"'login:to login''reg:to register'
                          "'Press 1 to get auction info:\nPress 2 To Exit:")
        client = self.client_runner()
        if user_data == '1':
            raw_data: str = 'info'
            self.sending_encrypted(client, raw_data)

        elif user_data == 'login':
            pass

        elif user_data == 'reg':
            pass

        elif user_data == 'get':
            pass

    def sending_encrypted(self, client, raw_data: str):
        encry = encry_decrypt.A3Encryption()
        decry = encry_decrypt.A3Decryption()
        encrypted_data = encry.start_encryption(raw_data, self.userKey)
        client.send(bytes(encrypted_data, "utf-8"))
        recv_info = client.recv(4096)
        recv_encrypted = recv_info.decode("utf-8")
        print("Received Encrypted Data : ", recv_encrypted)

        recv_decrypted = decry.startDecryption(recv_encrypted)
        print("$:", recv_decrypted)


if __name__ == "__main__":
    auction_client: Auction_client = Auction_client()

    while True:
        auction_client.client_menu()
