import socket
import subprocess
import os
import json

import pymongo

connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip"]
col = database["user_info"]

candi = database["candidate"]


class TCPserver():
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 9997
        self.toSave = {}

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print("Server listen on port:{} and ip {}".format(self.server_port, self.server_ip))
        try:
            while True:
                client, address = server.accept()
                print("Accepted Connection from - {} : {} ".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client_socket):
        data_list = []
        with client_socket as sock:
            from_client = sock.recv(1024)
            data_list = from_client.decode("utf-8").split(' ')  # login email password

            # data_list = ["login","email","password"]

            #     output = subprocess.getoutput("dir")
            #     # result = output.stdout.decode()
            #
            #     # return_valued = os.system(received_data)

            if data_list[0] == "gad":
                print("received command :", data_list[0])
                self.get_all_data(sock)

            elif data_list[0] == "login":
                self.login_checking(sock, data_list)

            elif data_list[0] == "vote":
                self.candiVote(data_list,sock)

            elif data_list[0] == "candidate_info":
                self.candidate_info(sock)

            elif data_list[0] == "emailcheck":
                self.email_checking(data_list[1], sock)

            elif data_list[0] == "candidate_register":
                self.registration(data_list, sock)

            elif data_list[0] == "voter_register":
                self.registration(data_list, sock)

            elif data_list[0] == "transfer_email":
                self.transferEamilChecking(data_list, sock)
            
            elif data_list[0] == "update_point":
                self.updateUserPoint(data_list, sock)
              

            else:
                sms = bytes("Invalid Option", "utf-8")
                sock.send(sms)

    def get_all_data(self, sock):
        data: dict = {}
        id = 0
        for i in col.find({}, {"_id": 0, "email": 1, "password": 1,"point":1}):
            id = len(data)
            dataform = {"email": i["email"], "password": i["password"],"point": i["point"]}
            data.update({id: dataform})
        print(data)
        str_data = json.dumps(data)

        str_data = bytes(str_data, 'utf-8')
        sock.send(str_data)

    def login_checking(self, sock, data_list):
        l_email = data_list[1]
        l_password = data_list[2]
        flag = -1
        sms = {}
        for i in col.find({}, {"_id": 0, "email": 1, "password": 1, "info": 1, "point": 1}):
            if i["email"] == l_email and i["password"] == l_password:
                flag = 1
                sms = {"email": i["email"], "info": i["info"], "point": i["point"]}
                sms = json.dumps(sms)

                break

        if flag == 1:
            str_data = bytes(sms, 'utf-8')
            sock.send(str_data)
        else:
            str_data = bytes("User name and password not found!", 'utf-8')
            sock.send(str_data)
#votes candidate
    def candiVote(self,data_list, sock):
        candi.update_one({"name":data_list[1]},{"$set":{"vote_point":data_list[2]}})
        self.candidate_info(sock)

#transfer Email checking
    def transferEamilChecking(self,data_list,sock):
        tran_email = data_list[1]
        flag = -1
        sms = {}
        for i in col.find({}, {"_id": 0, "email": 1, "password": 1, "info": 1, "point": 1}):
            if i["email"] == tran_email :
                flag = 1
                sms = {"email": i["email"], "info": i["info"], "point": i["point"]}
                sms = json.dumps(sms)

                break

        if flag == 1:
            str_data = bytes(sms, 'utf-8')
            sock.send(str_data)
        else:
            str_data = bytes("invalid account name !", 'utf-8')
            sock.send(str_data)
#Update Point
    def updateUserPoint(self,data_list, sock):
            tranEmail = data_list[1]
            tranPoint = int(data_list[2])
         
            sendEmail = data_list[3]
            sendPoint = int(data_list[4])

            col.update_one({"email":tranEmail},{"$set":{"point":tranPoint}})
            print("tranUserUpdated")
            col.update_one({"email":sendEmail},{"$set":{"point":sendPoint}})
            print("sendUserUpdated")
                      
            for i in col.find({}, {"_id": 0, "email": 1, "password": 1, "info": 1, "point": 1}):
                if i["email"] == sendEmail:
                    sms = {"email": i["email"], "info": i["info"], "point": i["point"]}
                    sms = json.dumps(sms)
        
            str_data = bytes(sms, 'utf-8')
            sock.send(str_data)

    def candidate_info(self, sock):
        try:
            to_send = {}
            for i in candi.find({}, {"_id": 0, "name": 1, "vote_point": 1}):
                print(i["name"], i["vote_point"])
                id = len(to_send) + 1
                to_update = {id: {"name": i["name"], "vote_point": i["vote_point"]}}
                to_send.update(to_update)

            to_send = json.dumps(to_send)

            sock.send(bytes(to_send, "utf-8"))
        except Exception as err:
            print("candiate db access err:", err)

            sock.send(bytes("candi_db_error", "utf-8"))

    def email_checking(self, email, sock):
        email_exist = 0
        for i in col.find({}, {"_id": 0, "email": 1}):
            if i["email"] == email:
                email_exist = 1

        if email_exist == 0:  # email not already exist
            sock.send(bytes("notExist", "utf-8"))

        else:
            sock.send(bytes("exist", "utf-8"))

    def registration(self, data_list: list, sock):
        if data_list[0] == "candidate_register":
            
            data_form = {"name": data_list[1],"email": data_list[2], "password": data_list[3], "phone": int(data_list[4]), "info": data_list[5],"vote_point": int(data_list[6])}
            print(data_form,"server")   
            ids = candi.insert_one(data_form)
            print("Candidate Registration success for :", ids.inserted_id)

            sock.send(bytes(str(ids.inserted_id), "utf-8"))
        
        elif data_list[0] == "voter_register":
            data_form = {"name": data_list[1],"email": data_list[2], "password": data_list[3], "phone": int(data_list[4]), "info": data_list[5],"point": int(data_list[6])}
            
            ids = col.insert_one(data_form)
            print("Voter Registration success for :", ids)

            sock.send(bytes(str(ids.inserted_id), "utf-8"))


if __name__ == '__main__':
    tcpserver = TCPserver()
    tcpserver.main()