import socket
import subprocess
import os
import json

import pymongo

connection =pymongo.MongoClient("localhost",27017)
database =connection["ncc_dip2"]
col =database["user_info"]


class TCPserver():
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 9998
        self.data = {}

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
        data_list=[]
        with client_socket as sock:
            from_client = sock.recv(1024)
            data_list = from_client.decode("utf-8").split(' ') #login email password

            #data_list = ["login","email","password"]

            #     output = subprocess.getoutput("dir")
            #     # result = output.stdout.decode()
            #
            #     # return_valued = os.system(received_data)
            
            if data_list[0]=="gad":
                self.get_all_data(sock)

            elif data_list[0]=="login":
                self.login_checking(sock,data_list)

            elif data_list[0]=="reg":
                self.register_sector(sock)
                print("register info")
            
            elif data_list[0]=="profile":
                self.add_user(sock,data_list)
                
            
            else:
                sms = bytes("Invalid Option","utf-8")
                sock.send(sms)

#get all data
    def get_all_data(self,sock):
        data:dict ={}
        for i in col.find({},{'_id':0}):
            id = len(data)
            dataform={"email":i["email"],"password":i["password"],"info":i["info"]}
            data.update({id:dataform})

        str_data =json.dumps(data)
        str_data = bytes(str_data,'utf-8')
        sock.send(str_data)

#login 
    def login_checking(self,sock,data_list):
        l_email = data_list[1]
        l_password = data_list[2]
        flag = -1
        sms ={}
        for i in col.find({},{"_id":0,"email":1,"password":1,"info":1,"phone":1}):
            if i["email"] == l_email and i["password"]==l_password:
                flag=1
                id =i["info"].split(":")
                user_id = id[1].strip()
                sms.update({user_id:i})
                # print(sms)
                break
        if flag == 1:
            str_data =json.dumps(sms)
            str_data = bytes(str_data, 'utf-8')
            sock.send(str_data)
        else:
            str_data = bytes("User name and password not found!", 'utf-8')
            sock.send(str_data)

#register
    def register_sector(self,sock):
        data = self.data
        for i in col.find({},{'_id':0}):
            id = len(data)
            dataform={"email":i["email"]}
            data.update({id:dataform})
        data =json.dumps(data)
        data = bytes(data,'utf-8')
        sock.send(data)
#update database
    def add_user(self,sock,user):
        user_id = len(self.data)+1
        email: str = user[1]
        password: str = user[2]
        phone: int = user[3]
        info:str = "User data is "+ self.email_to_user_name(email) +" id : "+str(user_id)

        #update new user datas
        data_form = {"_id": user_id, "email": email, "password": password, "phone": phone,"info":info}
        ids = col.insert_one(data_form)
        print("inserted id :", ids.inserted_id)

        #send notify of updating data back to clients
        str_data = bytes("User data is successful recorded!", 'utf-8')
        sock.send(str_data)

# eamil to userName 
    def email_to_user_name(self,email):
        email= email
        a2 =""
        a2  = email.split("@")
        return a2[0]

if __name__ == '__main__':
    tcpserver = TCPserver()
    tcpserver.main()