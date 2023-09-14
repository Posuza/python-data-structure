import socket
import json


class TCPclient():
    def __init__(self, sms):
        self.target_ip = 'localhost'
        self.target_port = 9998
        self.input_checking(sms)
        self.emails ={}

    def client_runner(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        # client.send(self.client_sms)
        #
        #     received_from_server = client.recv(4096)
        #
        #     recv_sms = received_from_server.decode("utf-8")
        #
        #     print("$:", recv_sms)
        #
        #     client.close()
        return client  # to send and received data

    def input_checking(self, sms):
        if sms == "gad":
            self.get_all_data(sms)

        elif sms == "login":
            self.login(sms)

        elif sms == "reg":
            self.emailValidation(sms)

        elif sms == "logout":
            print(" # You are log out...")

        else:
            print("Invalid Option..")
            exit(1)
           
#get all data
    def get_all_data(self, sms):
        client = self.client_runner()
        sms = bytes(sms, "utf-8")
        client.send(sms)
        received_from_server = client.recv(4096)
        # print(received_from_server.decode("utf-8"))

        dict_data: dict = json.loads(received_from_server.decode("utf-8"))
        print(type(dict_data))
        print(dict_data)
        client.close()
#login
    def login(self, info):
        try:
            print("This is login Form")
            l_email = input("Enter your email to login:")
            l_pass = input("Enter your password to login:")

            client = self.client_runner()
            sms = info + ' ' + l_email + ' ' + l_pass  # login email password
            sms = bytes(sms, "utf-8")
            client.send(sms)
            received_from_server = client.recv(4096)
            dict_data: dict = json.loads(received_from_server.decode("utf-8"))
            client.close()
            self.userProfile(dict_data)

        except Exception as err:
            print(err)

#profile Page
    def userProfile(self,userinfo):
            info= []
            data = userinfo
            for key in data:
                print(key)
                info = data[key]["email"].split("@")
                print("  # Profile # \n username : {} \n Email   : {} \n Phone   : {}".format(info[0],data[key]["email"],data[key]["phone"]))

            # self.updateUserInfo(data)  

#update user Infomation 
    def updateUserInfo(self,userData):
                up_data = {'13': {'email': 'asfads@gag.com', 'password': 'sdfsdgsfd', 'phone': '1234342355', 'info': 'User data is asfads id : 13'}}
                user:str
                for i in userData:
                    user = i
                try:
                    key = int(input("Press 1 to update or 2 to logout ! \n > "))
                    if key == 1:
                        print("Press 1 to update your email")
                        print("Press 2 to updaate your phone number")
                        print("Press 3 to update your password")
                        num = input("> ")
                        for i in range(len(self.emails)):
                            if (self.emails[str(i)]["email"]) == userData[user]["email"]:
                                del self.emails[str(i)]
                                print(self.emails)

                                if num ==1:
                                    email = input("Enter your new email ")
                                    if email !="" and email != self.emails[str(i)]["email"]:
                                        up_data[user]["email"] = email
                                    else:
                                        print("Email is already taken! plz choose other") 
                                elif num ==2:
                                    phone = self.phoneVali("Enter your phone number.. >")
                                    up_data[user]["phone"] = phone
                                elif num ==3:
                                    password = input("Enter your new password ")
                                    up_data[user]["password"] = password       
                                else:
                                    print("invalid number")

                    elif key ==2:
                        self.input_checking("logout")
                    else:
                        print("Incorrect key press")   
                        self.updateUserInfo()
                except Exception as err:
                    print("Incorrect key press",err)   
                    self.updateUserInfo()
#update user data ivalidation
    # def upDataValidate():


#regitserValidation
    def emailValidation(self, sms): 
        sms2 =sms
        client = self.client_runner()
        sms = bytes(sms, "utf-8")
        client.send(sms)

        #rececive data from server
        received_from_server = client.recv(4096)
        self.emails: dict = json.loads(received_from_server.decode("utf-8"))
        client.close()
        print(sms2)
        print(type(sms2))
        if sms2 == "reg":
            self.register("profile")
        else:
            self.updateUserInfo()
        

#register
    def register(self,info):
        print("# This is registration form #")
        try:
            reg_email = input("Enter your email.. >")
            for i in range(len(self.emails)):
                if (self.emails[str(i)]["email"]) == reg_email:
                    print("Email is already taken!")
                    self.emailValidation("reg")     
                else:
                    reg_pass = input("Enter your password.. >")
                    reg_phone = self.phoneVali("Enter your phone number.. >")
                    break
            client = self.client_runner()
            reg_info =info+' '+reg_email +' '+ reg_pass +' '+str(reg_phone)
            print(reg_info)
            
            data= bytes(reg_info, "utf-8")
            client.send(data)  

            #rececive data from server
            received_from_server = client.recv(4096)
            print(received_from_server.decode("utf-8"))
            client.close()
            self.login("login")
        
        except Exception as err:
            print(err)
            self.register("reg")
            
#phone numbe validation
    def phoneVali(self,text):
            digits = "0123456789"
            found = 0
            phone = input(""+ text + " > ")
            if phone != '':
                lenght = len(phone)
                for b in phone:
                    for digit in digits:
                        if digit == b:   
                            found += 1 
                if lenght == found and lenght >= 8 and lenght <= 15:
                    return int(phone)
                else:
                    print("phone must contain only number and \n should not be under 8 or more than 15")
                    return self.phoneVali(text)
            else:
                return self.phoneVali(text)


if __name__ == "__main__":
    while True:
        sms = input("# MAIN OPTION #\n Enter some data to send:")
        tcp_client = TCPclient(sms)