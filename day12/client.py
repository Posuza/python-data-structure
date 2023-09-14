
import socket

class TCPclient():

    def __init__(self,sms):
        self.target_ip = 'localhost'
        self.target_port = 9997
        self.send_and_rev_data = {}
        self.client_sms = bytes(sms,'utf-8')

    def run_client(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.target_ip,self.target_port))
        client.send(self.client_sms)
        received_form_server = client.recv(4096)
        recv_sms = received_form_server.decode('utf-8')
        
        self.send_and_rev_data.update({len(self.send_and_rev_data):recv_sms})
        print("Get Back data from Server: ",recv_sms)
        print(self.send_and_rev_data)
        client.close()

if __name__ == '__main__':
    while True:
        sms = input("Enter sms to send to server\n")
        tcp_client = TCPclient(sms)
        tcp_client.run_client()