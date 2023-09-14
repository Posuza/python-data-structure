import socket
import encry_decrypt
import json


class Auction_client():

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9191
        self.userKey = self.getting_key()
        self.client_menu()

    def getting_key(self):
        userKey: str = input("Enter your encryption key for the whole process:")
        return userKey

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client  # to send and sms data

    def client_menu(self):
        print("\n @This is client menu:")
        user_data = input(" get: Get_all_information, \n login: to login, \n reg: to register, \n 1: to get auction info: \n exit: To Exit:\n > ")
        
        if user_data == '1':
             pass      
  
        elif user_data == 'login':
            self.login(user_data)

        elif user_data == 'reg':
            self.register()

        elif user_data == 'get':
            self.itemsInfo()

        elif user_data == 'exit':
            exit(1)

#Send & Receive with en_decription data
    def sending_encrypted(self,raw_data):
        client = self.client_runner()

        encry = encry_decrypt.A3Encryption()
        decry = encry_decrypt.A3Decryption()
  
        encrypted_data = encry.start_encryption(raw_data, self.userKey)
        client.send(bytes(encrypted_data, "utf-8"))

        sms_info = client.recv(4096)
        sms_encrypted = sms_info.decode("utf-8")
        # print("sms Encrypted Data : ", sms_encrypted)
        rec_descript_sms = decry.startDecryption(sms_encrypted) 
        #Descriptiondata is uncoccupied the old existed data
        decry.emptyDescript()  

        client.close()
        #Caution! : rec_descript_sms could different data types       
        return rec_descript_sms

# @item
#Request Items information    
    def itemsInfo(self):
        raw_data: str = 'ItemsInfo'
        sms:dict = self.sending_encrypted(raw_data)  
        dic_items: dict = json.loads(sms)
        print("\n @List of items")  
        print("No: ", "Name: ", "   price") 
        
        for i in dic_items:
            space = " " * int(10 - len(dic_items[i]["name"]))
    
            print( i,": ",dic_items[i]["name"],space, dic_items[i]["price"])

# @Candidate
#Userlogin
    def login(self,info): 
        try:
            print("\n @login Form..")
            l_email = input("Type\n\'email'\ to login: \n\'reg\' to register: \n\'exit\' to exit: >")
            if l_email == "exit":
                exit(1)
            elif l_email == "reg":
                self.register()

            l_pass = input("Enter your password to login: >")

            sms = info + ' ' + l_email + ' ' + l_pass  # login email password
            sms:dict = self.sending_encrypted(sms) 
            user_info: dict = json.loads(sms)

            self.user_authenticated(user_info)
            print(user_info)

        except Exception as err:
            print("Incorrect email or password")
            self.login(info)

#User Authenticated
    def user_authenticated(self,user_info):
        print("\n@you are login...")
        print("Userame: ",user_info["name"])
        print("Point :", user_info["point"])
        print("Bio  :", user_info["info"])
        print(" @Main Option.. ")
        try:
            new_info = input("Press 1 @User Option..:\nPress 2 @Logout..: >")
            if new_info == '1':
                self.user_option(user_info)
            elif new_info == '2':
                print(" \n @you are loging out..")
                self.client_menu()  # to write more new_info
            else:
                print("Invalid new_info [X]")
                self.user_authenticated(user_info)

        except Exception as err:
            print(err)

#User Option
    def user_option(self, user_info):
        try:
            new_info = input("\n    *** Option ***\nPress 1 to change user information \nPress 2 to Delete Acc:\nPress 3 to logout:")
 
            if new_info == '1':
                self.user_info_change(user_info)
            elif new_info == '2':
                self.account_delete(user_info)
            elif new_info == '3':
                self.login("login")
            else:
                print("Invalid new_info")
                self.user_option(user_info)

        except Exception as err:
            print(err)
            self.user_option(user_info)

#User Info change
    def user_info_change(self,user_info):
            print("\n  @Your Information.. ")
            print("username :", user_info["name"])
            print("Email :", user_info["email"])
            print("Password :", user_info["password"])
            print("Phone no :", user_info["phone"])
            print("Bio :", user_info["info"])

            data =""
            flag=0
            try:
                new_info = int(input("\n@Enter relative numbers for update a particular informationb\nPress 1 for username :\nPress 2 for email :\nPress 3 for password :\nPress 4 for phone :\nPress 5 for Bio :\nPress 6 for exit \n  > " ))

                if new_info == 1:
                    name = self.update_information("Enter Your new username :> ","name",user_info)
                    data = "name" +" "+ name

                elif new_info == 2:
                    email = self.update_information("Enter Your new eamil :> ","email",user_info)
                    data = "email" + " " + email

                elif new_info == 3:
                    password = self.update_information("Enter Your old password :> ","password",user_info)
                    print("uodat",password)
                    data = "password" + " " + password

                elif new_info == 4:
                    phone =self.phoneVali("Enter Your new phone no :> ",user_info["phone"])
                    data = "phone" + " " + str(phone)

                elif new_info == 5:
                    info =self.update_information("Enter Your new info :> ","info",user_info)
                    new_info = info.replace(" ","_")
                    data = "info"+ " " + new_info

                elif new_info == 6:
                    self.user_option(user_info)
                else:
                    print("Invalid new_info")
                    self.user_info_change(user_info)

                data_form = "update_info" + " " + user_info["email"] + " " + data
                print(data_form)
                
                sms:dict = self.sending_encrypted(data_form) 
                user_info: dict = json.loads(sms)

                print(user_info)
                self.user_info_change(user_info)

            except Exception as error:
                print(error,"invalide number! ")
                self.user_info_change(user_info)

#update user information
    def update_information(self,text,info,user_info):  
            count = 0
            newInfo = info.split(" ")
            print(len(newInfo))
            if len(newInfo)>1:
              info = newInfo[0]
              count = int(newInfo[1])
            else:
                info = info

            try:
                new = input(text)
                if new != "":
        #update name
                    if info == "name":
                        newName = self.userName_checking_inDB(new)
                        if newName == new:
                            return new
                        else:
                            self.update_information(text,info,user_info)
                    
        #update email         
                    elif info == "email":
                        check =self.email_validation(new)
                        email_exit = self.email_checking_inDB(new)
                        print(check,"check",email_exit,"exit")
                        if check == 1 and email_exit == 1:
                            return new
                        else:
                            print("invalid email ..")
                            self.update_information(text,info,user_info)
        #update password
                    elif info == "password":
                        new1 = new
                        if count == 3:
                            counter = 0
                            while  True:
                                email = input("Enter your email: >")
                                if email == user_info["email"]:
                                    new1 = user_info["password"]
                                    break
                                else:
                                    counter = counter +1
                                    if counter ==3:
                                        print("@Your attempt being denied..")
                                        self.login("login")
                                    print("@Invalid email pls try again!... ")

                        if new1 == user_info["password"]:
                            print("@Enter Your new password...")
                            #password validation
                            
                            
                            while  True:
                                passwrod1 = self.password_check("Enter your new password: >")
                                password2 = input("new password Again: >")
                                if passwrod1 == password2:
                                    newPassword = password2
                                    break
                                else:
                                    print("@Password don't match try again!... ") 
                            print(newPassword)          
                            return newPassword   
                           
                        else:
                            count =count +1
                            text = "@Password incorrect pls try again!: >"
                            info = info + " " + str(count)
                            self.update_information(text,info,user_info)
        #update info
                    elif info == "info":
                        return new
                else:       
                    return user_info[info]
                
            except Exception as error:
                print(error,"invalid information")
                self.update_information(text,info,user_info)
    
#delet account
    def account_delete(self,user_info):
            print(user_info["email"]," try to delete")
            while True:
                confirm = input("Type \'yes\' to confirm or \'no\' to cancel: >")
                if confirm == "no":
                    print("@You have cancel the confirmation..")
                    self.user_authenticated(user_info)
                    break

                elif confirm == "yes":
                    data_form = "delete_user" + " " + user_info["email"]
                    sms = self.sending_encrypted(data_form) 
                    print(sms)
                    self.client_menu()

#UserRegisteration
    def register(self):
        print("\n  @registration Form... ")
        r_email = ''
        while True:
            r_email = input("Enter \'email\' for registration: or \nEnter \'login\' to go back: >")
            if r_email=="login":
                self.login("login")
            flag = self.email_validation(r_email)  # 1 or -1

            if flag == 1:
                break
            else:
                print("Email Form Invalid\nTry Again! ")

        print("Email From Valid ")
        self.user_register(r_email)

#Register voter
    def user_register(self, r_email):

        if self.email_checking_inDB(r_email) == 1:
            try:
                username = self.username_check("Enter your username:")

                pass1 = self.password_check("Enter your password to register:")
                pass2 = input("Enter your password Again  to register:")

                if pass1 == pass2:
                
                    print("Password Was match!")
                    phone =self.phoneVali("Enter Your phone no or \'skip\' to skip :> ",99999999)

                    data_list = [username,r_email, pass1, phone]
                    print(data_list)
                    self.final_registration(data_list)

                else:
                    print("Password not match:")
                    self.user_register(r_email)


            except Exception as err:
                print(err)

        else:

            print("Your email was already register!")
            self.register()

#Registeration confirmation
    def final_registration(self, data_list):
        while True:
            confirm = input("Type \'yes\' to confirm or \'no\' to cancel: >")
            if confirm == "no":
                print("@You have cancel the confirmation..")
                self.register()
                break
            elif confirm == "yes":
                data_form = "candidate_register" + " " + data_list[0] + " " + data_list[1] + " " + data_list[2] + " " + str(data_list[3]) + " " + "Update_your_user_info" + " " + "0"
                print(data_form)

                sms = self.sending_encrypted(data_form) 

                if sms:
                    print("Registration Success!",sms)
                    info="login"
                    self.login(info)
                    break
            else:
                print("@Invalid input for the confirmation..")
    
#phone numbe validation
    def phoneVali(self,text,old_phone):
            
            digits = "0123456789"
            found = 0
            phone = input(""+ text)
            if phone == "skip":
                return old_phone
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
                    return self.phoneVali(text,old_phone)
            else:
                return int(old_phone)   

#Pssword checking
    def password_check(self,text):
        while True:
            password =input(text)
            result =self.password_valid(password)
            if password == result:
                return password

 #Pssword vlid
    def password_valid(self,password):
        if len(password) < 8:
            print("@Password must be more than 8 and contain different character types..")
            return -1
        check = {"number" : 0,
                "uppercase" : 0,
                "lowercase" : 0,
                "special_character" : 0}
        count = 0
        found = 0
    #  special_character = ["!","#","$","%","&","*",".", ",","/",":",";","?","@","\","_","|","~"]
        special_characters = [33,35,36,37,38,42,44,46,47,58.59,63,64,92,95,124,126]
        for i in range(len(password)):
                aChar = password[i]
                if  (ord(aChar) >47 and ord(aChar) < 58): #1241235
                    check["number"]= 1

                elif (ord(aChar) >64 and ord(aChar) < 91): #ASFGDNJ
                    check["uppercase"]= 1

                elif (ord(aChar) >95 and ord(aChar) < 123): #asfshcb   
                    check["lowercase"]= 1

                else:
                    found = found+1
                    for j in special_characters:
                        if ord(aChar) == j:
                            print(ord(aChar))
                            count = count+1
                            break
        # print(count,"count")
        # print(found,"found")
        if count != 0 and count == found :
            check["special_character"] = 1
        else:
            print("disallow special_character")

        counter = 3
        for i in check:
            if check[i] == 0:
                print("password must contain a",i)
                counter = -1

        if counter == 3:
            return password
        else:
            return -1

#email check
    def email_validation(self, r_email):
        name_counter = 0
        for i in range(len(r_email)):
            if r_email[i] == '@':
                # print("Name End Here")
                break
            name_counter += 1

        print("Name counter: ", name_counter)

        email_name = r_email[0:name_counter]
        email_form = r_email[name_counter:]

        # print(email_name)
        print(email_form)

        # checking for name
        name_flag = 0
        email_flag = 0
        for i in range(len(email_name)):
            aChar = email_name[i]
            if (ord(aChar) > 31 and ord(aChar) < 48) or (ord(aChar) > 57 and ord(aChar) < 65) or (
                    ord(aChar) > 90 and ord(aChar) < 97) or (ord(aChar) > 122 and ord(aChar) < 128):
                name_flag = -1
                break

        domain_form = ["@facebook.com", "@ncc.com", "@mail.ru", "@yahoo.com", "@outlook.com", "@apple.com", "@zoho.com",
                       "@gmail.com"]

        for i in range(len(domain_form)):

            if domain_form[i] == email_form:
                email_flag = 1
                break

        if name_flag == -1 or email_flag == 0:
            return -1

        else:
            return 1


#checking Email in DB 
    def email_checking_inDB(self, email):
        data = "email" + " " + email
        sms = self.sending_encrypted(data)
        print(sms)

        if sms == "notExist":
            return 1
        else:
            return -1  

#Username checking
    def username_check(self,text):
        while True:
            userName =input(text)
            if userName !="":
                result =self.userName_checking_inDB(userName) #return 1 & -1
                if result == userName :
                    return userName
                else:
                    print("This username was alredy existed pls try another")
            else:
                print("Username must not be empty!")            
#checking username in DB 
    def userName_checking_inDB(self, userName):
        data = "name" + " " + userName
        sms = self.sending_encrypted(data)
        print(sms)

        if sms == "notExist":
            return userName
        else:
            return -1  

if __name__ == "__main__":
    auction_client: Auction_client = Auction_client()

    while True:
        auction_client.client_menu()
