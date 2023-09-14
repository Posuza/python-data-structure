import socket
import s_encrypt_and_decrypt
import ob
import json

from dbModel import NccAuctionModel



toReturn = None


class Server():

    def __init__(self):
        self.ob = ob.Ob()
        self.decrypt = s_encrypt_and_decrypt.A3Decryption()
        self.encrypt = s_encrypt_and_decrypt.A3Encryption()
        self.server_ip = "localhost"
        self.server_port = 9191
        self.items_Controller: ItemsController = ItemsController()
        self.users_Controller: UsersController = UsersController()

#Main
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

#Client control
    def client_control(self, client):
        with client as sock:
            #receive info from client request
            from_client = sock.recv(1024)
            data_list = from_client.decode("utf-8")

            decrypted = self.decrypt.startDecryption(data_list)
        #Descriptiondata is uncoccupied the old existed data
            self.decrypt.emptyDescript()
            print("#:", decrypted)

            decrypted_list:list = decrypted.split(' ')

            ob_recv = self.ob.get_received(decrypted_list[0])

            print("Ob data:", ob_recv)

            data = ''

 #Collection: item and price
            if decrypted_list[0] == 'ItemsInfo':
                info_data = self.items_Controller.info(decrypted_list)
                data += info_data

 #Collection: Candidate          
            elif decrypted_list[0] == 'login':
                info_data = self.users_Controller.login(decrypted_list)
                data += info_data

            elif decrypted_list[0] == 'delete_user':
                info_data = self.users_Controller.delete_user(decrypted_list)
                data += info_data
    
            elif decrypted_list[0] == 'update_info':

                info_data = self.users_Controller.update_user_info(decrypted_list)
                data += info_data

#Checking email already exited            
            elif decrypted_list[0] == 'email':
                info_data = self.users_Controller.email_checking(decrypted_list)
                data += info_data

#Checking name alredy exited
            elif decrypted_list[0] == 'name':
                info_data = self.users_Controller.email_checking(decrypted_list)
                data += info_data
            
            elif decrypted_list[0] == 'candidate_register':
                info_data = self.users_Controller.registration(decrypted_list)
                data += info_data
            
            else:
                info_data = "Invalid Option"

            #sending enscription
            encrypted = self.encrypt.start_encryption(info_data, 'servertcp')
            sock.send(bytes(encrypted, "utf-8"))
            ob_send = self.ob.send_data(data)
            print("Ob send:", ob_send)

    # def for_observer(self):
    #     # to_return = self.decrypted_data
    #     #
    #     # self.decrypted_data='n'
    #     return self.decrypted_data

#Item controller
class ItemsController():
    def __init__(self):
        self.database = NccAuctionModel()


    def info(self,dataList):
        itemCollection = self.database.item()
        data = {}
        id=0
        for i in itemCollection.find({},{"_id":0,"name":1,"price":1}):
            id = len(data) +1
            dataform = {"name":i["name"],"price":i["price"]}
            data.update({id:dataform})

        print("items",data)
        str_data =  json.dumps(data)
        return str_data
    
#Users Controller
class UsersController():
    def __init__(self):
        self.database = NccAuctionModel()
#login
    def login(self,dataList):

        usersCollection = self.database.candidate() 
        l_email = dataList[1]
        l_password = dataList[2]
        flag = -1
        sms = {}
        str_data = ""
       
        for i in usersCollection.find({},{"_id": 0,"name":1, "email": 1, "password": 1, "phone":1, "info": 1, "point": 1}):
            if i["email"] == l_email and i["password"] == l_password:
                print("for ", i["email"],l_email)
                flag = 1
                bio = i["info"].replace("_"," ")

                sms = {"name":i["name"], "email": i["email"],"password": i["password"],"phone":i["phone"],"info": bio,"point":i["point"]} 

                print(sms)
                sms = json.dumps(sms)

                break 
      
        if flag == 1:
            str_data = sms
        else:
            str_data = "User name and password not found!"

        return str_data
    
#Register user
    def registration(self,data_list):
        col = self.database.candidate() 
        print(data_list)

        if data_list[0] == "candidate_register":
            data_form = {"name": data_list[1],"email": data_list[2], "password": data_list[3], "phone": int(data_list[4]), "info": data_list[5],"point": int(data_list[6])}
            print(data_form,"server")  

            ids = col.insert_one(data_form)
            print("Candidate Registration success for :", ids.inserted_id)
            return str(ids.inserted_id)

#Update user Infomation
    def update_user_info(self,data_list):
        col = self.database.candidate() 

        if data_list[0] == "update_info":
            if data_list[2] == "phone":
                data_list[3] =int(data_list[3])
            col.update_one({"email":data_list[1]},{"$set":{data_list[2]:data_list[3]}})
            if data_list[2] == "email": 
                data_list[1] = data_list[3]
            print(data_list[1]," update")

        else:
            col.update_one({"email":data_list[1]},{"$set":{"point":int(data_list[2])}})
            print("userpoint update")

        sms = {}
        for i in col.find({}, {"_id": 0,"name":1, "email": 1, "password": 1, "phone":1, "info": 1, "point": 1}):
            if i["email"] == data_list[1]:
                bio = i["info"].replace("_"," ")
                sms = {"name":i["name"], "email": i["email"],"password": i["password"],"phone":i["phone"], "info": bio, "point": i["point"]}   
        
        jsms = json.dumps(sms)

        return jsms

#Delete user
    def delete_user(self,data_list):
        usersCollection = self.database.candidate() 

        email = data_list[1]
        for i in usersCollection.find({}, {"_id": 0, "email": 1}):
            if i["email"] == email:
                print(email)
                usersCollection.delete_one({"email":email})    
                break
        return "successful deleted!"

#email checking
    def email_checking(self, email):
        col = self.database.candidate() 
        email_exist = 0
        ch_email = email[0]
        # print("chekcking",email)
        # print(type(email))
        for i in col.find({}, {"_id": 0, ch_email: 1}):
            # print(i[ch_email])
            # print(email)

            if i[ch_email] == email[1]:
                email_exist = 1

        if email_exist == 0:  # email not already exist
            return "notExist"

        else:
            return "exist"
        

#Start program
if __name__ == "__main__":
    auction: Server = Server()
    auction.main()
