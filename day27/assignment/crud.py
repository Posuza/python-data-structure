from binarySearchTree import BST
import random
# from dbModel import bSTModel # line 8
import json


class cRUD:
    def __init__(self):
        # self.databse = bSTModel()     
        # self.data = {1:{ "name": "hi","phone": 345610234,"email":"hhh@gmail.com","password": "123asdASD@","cash": 100},
        #              2:{ "name": "he","phone": 12424637234,"email":"hhe@gmail.com","password": "123asdASD@","cash": 100},
        #              3:{ "name": "her","phone": 12424637234,"email":"herh@gmail.com","password": "123asdASD@","cash": 100},
        #              4:{ "name": "helo","phone": 12424637234,"email":"hhelo@gmail.com","password": "123asdASD@","cash": 100},
        #              5:{ "name": "becon","phone": 12424637234,"email":"hbecon@gmail.com","password": "123asdASD@","cash": 100}
        #              }
        self.bs_Tree = BST()
        self.id = 0

#UserMenue
    def mainMenue(self):
        confirm = input("Type \'reg\',\'login\',\'users\',\'exit\' to stop! >")
        if confirm == "reg":
            crud.register()
        elif confirm == "login":
            crud.login()
        elif confirm == "users":
             self.bs_Tree.showdatas()
        elif confirm == "exit":
            exit(1)
            # print("@You have stop the operation..")
            # self.load_to_mongo()
        else:
            print("Invlid Input")
        self.mainMenue()

    def load_from_postGr(self):
        databse = self.databse.user()
        for i in databse.find({}, {"_id": 0,"name":1, "phone": 1,"email":1, "password": 1, "cash": 1}):
        # for i in self.data:
            self.id += 1
            # print(self.id,i["name"],i["phone"],i["email"],i["password"],i["cash"])
            # self.id += 1
            self.bs_Tree.addData(self.id,self.data[i]["name"],self.data[i]["phone"],self.data[i]["email"],self.data[i]["password"],self.data[i]["cash"])

    def load_to_mongo(self):
        databse = self.databse.user()
        itr = self.bs_Tree
        if itr is not None:
            
            while itr:
                itr = itr.left
                print(itr.id,itr.name,itr.phone,itr.email,itr.password,itr.cash)
                data_form = {"name":itr.name,"phone":int(itr.phone),"email":itr.email,"password":itr.password,"cash":int(itr.cash)}
                ids = databse.insert_one(data_form)

                print("Candidate Registration success for :", ids.inserted_id)
  
                itr = itr.right
            exit(1)

#profile
    def profile(self,user_info):
        print("\n@you are login...")
        print("Userame: ",user_info.name)
        print("Phone: ",user_info.phone)
        print("Cash :", user_info.cash)
        print(" @Main Option.. ")
        try:
            new_info = input("Press 1 @More Option..:\nPress 2 @Add cash..:\nPress 3 @TransferCash..: \nPress 4 @Logout..: >")
            if new_info == '1':
                self.user_option(user_info)
            elif new_info == '2':
                self.addMoreCash(user_info)
            elif new_info == '3':
                self.transferCash(user_info)
            elif new_info == '4':
                print(" \n @you are loging out..")
                self.mainMenue()  # to write more new_info
            else:
                print("Invalid input")
                self.profile(user_info)

        except Exception as err:
            print(err)

#user Option
    def user_option(self,user_info):
        try:
            new_info = input("\n    *** Option ***\nPress 1 to change user information \nPress 2 to Delete Acc:\nPress 3 to MainOption:")
 
            if new_info == '1':
                self.user_info_change(user_info)
            elif new_info == '2':
                self.account_delete(user_info)
            elif new_info == '3':
                self.profile(user_info)
            else:
                print("Invalid new_info")
                self.user_option(user_info)

        except Exception as err:
            print(err)
            self.user_option(user_info)

#User Info change
    def user_info_change(self,user):
            print("\n  @Your Information.. ")
            print("username :", user.name)
            print("Email :", user.email)
            print("Password :", user.password)
            print("Phone no :", user.phone)

            try:
                new_info = int(input("\n@Enter relative numbers for update a particular informationb\nPress 1 for username :\nPress 2 for email :\nPress 3 for password :\nPress 4 for phone :\nPress 5 for Bio :\nPress 6 for exit \n  > " ))

                if new_info == 1:
                    name = self.username_exitDB("Enter Your new username :> ")
                    self.bs_Tree.update(user.id,"name",name)

                elif new_info == 2:
                    email = self.email_Exist("Enter Your new eamil :> ")
                    self.bs_Tree.update(user.id,"email",email)

                elif new_info == 3:
                    Valid_password = self.password_check("Enter Your old password :> ")
                    if Valid_password != -1:
                        check_old_pass = self.password_check_inDB(Valid_password,user,0)
                        print(check_old_pass) 
                        self.bs_Tree.update(user.id,"password",check_old_pass)
                    else:
                        print("invalid emal..")
                        self.user_info_change(user)

                elif new_info == 4:
                    phone = self.phoneVali("Enter Your new Phone no :> ",user.phone)
                    self.bs_Tree.update(user.id,"phone",phone)

                # elif new_info == 5:
                #     info =self.update_information("Enter Your new info :> ","info",user_info)
                #     new_info = info.replace(" ","_")
                #     data = "info"+ " " + new_info

                elif new_info == 6:
                    self.user_option(user)

                else:
                    print("Invalid new_info")
                    
                print("update successfully ")
                update_user=self.bs_Tree.searchBykey("id",user.id)
                self.user_info_change(update_user)

            except Exception as error:
                print(error,"invalide number! ")
                self.user_info_change(user)

#Login
    def login(self):
        try:
            print("\n @login Form..")
            l_email = self.email_check("Enter your email: >")
            l_pass = self.password_check("Enter your password to login: >")

            while True:
                confirm = input("Type \'yes\' to login or \'cancel\' to go back: >")
                if confirm == "cancel":
                    print("@You have cancel login..")
                    self.mainMenue()

                elif confirm == "yes":
                    element1 =self.bs_Tree.searchBykey("email",l_email)
                    if element1 != -1:
                        if element1.password == l_pass:
                            print("Register successfully")
                            self.profile(element1)
                        else:
                            print("Incorrect password...")
                            self.login()
                    print("Incorrect email...")
                    self.login()
        except Exception as err:
            print("Incorrect email or password")
            self.login()

#register         
    def register(self):
        print("\n  @registration Form... ")
        try:
            name = self.username_exitDB("Enter Your Usename: ")
            phone =self.phoneVali("Enter Your phone no or \'skip\' to skip :> ",99999999)
            email = self.email_Exist("Enter Your email: ")
            while True:
                passwrd1 = self.password_check("Enter Your passwrd: ")
                passwrd2 = self.password_check("Retype your Your password: ")
                if passwrd1 == passwrd2:
                    cash = 0
                    while True:
                        confirm = input("Type \'yes\' to confirm or \'cancel\' to go back: >")
                        if confirm == "cancel":
                            print("@You have cancel the Registeration..")
                            self.mainMenue()

                        elif confirm == "yes":
                            self.id = random.randrange(0,100,1)
                            self.bs_Tree.addData(self.id,name,phone,email,passwrd1,cash)
                            print("Register successfully")
                            self.login()

                else:
                    print("Password don't match pleze try again..")
        except Exception as err:
            print(err,"pleze try again")
            self.register()

#delet account
    def account_delete(self,user_info):
            print(user_info.email ," try to delete")
            while True:
                confirm = input("Type \'yes\' to confirm or \'no\' to cancel: >")
                if confirm == "no":
                    print("@You have cancel the confirmation..")
                    self.profile(user_info)
                    break

                elif confirm == "yes":
                    print(user_info.id)
                    self.bs_Tree.delete(user_info.id)
                    print("Your account is permenant deleted")
                    self.mainMenue()
                
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

#Username checking in DB
    def username_exitDB(self,text):
        while True:
            userName =input(text)
            if userName !="":
                # print("enter")
                result =self.bs_Tree.searchBykey("name",userName) #return dat & None
                # print(result)
                if result == None :
                    return userName
                else:
                    print("This username was alredy existed pls try another")
            else:
                print("Username must not be empty!")    

#checking Email in DB 
    def email_Exist(self, text):
        while True:
            email =input(text)
            if email !="":
                valid_email = self.email_validation(email)
                if valid_email == 1:
                    result =self.bs_Tree.searchBykey("email",email) #return dat & None
                    if result == None :
                        return email
                    else:
                        print("This email was alredy taken pls try another")
            else:
                print("Username must not be empty!") 

#checking Email 
    def email_check(self, text):
        while True:
            email =input(text)
            if email !="":
                valid_email = self.email_validation(email)# 1 or -1
                # print(valid_email)
                if valid_email == 1 :
                    return email
                else:
                    print("Invlid email")
            else:
                print("Email must not be empty!") 

#email validation
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
#password checking in db
    def password_check_inDB(self,vali_pass,user,count):
        count = count
    #update password
        try:
            new1 = vali_pass
            if count == 3:
                counter = 0
                while  True:
                    email = input("Incorrect password Enter your email: >")
                    if email == user.email:
                        new1 = user.password
                        break
                    else:
                        counter = counter +1
                        if counter ==3:
                            print("@Your attempt being denied..")
                            self.login()
                        print("@Invalid email pls try again!... ")

            if new1 == user.password:
                print("@Enter Your new password...")

                #password validation
                while  True:
                    passwrod1 = self.password_check("Type your new password: >")
                    password2 = input("Retype new password Again: >")
                    if passwrod1 == password2:
                        newPassword = password2
                        break
                    else:
                        print("@Password don't match try again!... ") 
                print(newPassword)          
                return newPassword   
                
            else:
                self.password_check_inDB(vali_pass,user,count+1)

        except Exception as err:
            print(err,"Invalid password!")
            self.password_check_inDB(vali_pass,user,0)

#Pssword checking
    def password_check(self,text):
        while True:
            password =input(text)
            result =self.password_valid(password)
            if password == result:
                return password
            print("invlid pssword plz try again..")

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

#Add More cash
    def addMoreCash(self,user):
        cash = int(user.cash)
        try:
            new_cash = int(input("Enter your amount..."))
            if new_cash != "" and new_cash > 0:
                cash = cash + new_cash
                self.bs_Tree.update(user.id,"cash",cash)
                update_user=self.bs_Tree.searchBykey("id",user.id)
                print(update_user.id,update_user.cash)
                self.profile(update_user)
            else:
                print("invlide value..")
                return self.addMoreCash(user)
        except Exception as err:
            print(err)
            self.addMoreCash(user)

#transter Cash
    def transferCash(self,user):
        print("\n @Transfer Section..")
        receiver_cash = 0
        sender_cash = int(user.cash)
        flag = True
        user
        try:
            new_email = input("Enter transter userEmail..: ")
            if new_email != "":
                new_user=self.bs_Tree.searchBykey("email",new_email)
                if new_user != None:
                    receiver_cash = int(new_user.cash)

                    while flag:
                        amount = int(input("Enter Amount..: "))
                        if amount <= sender_cash:
                            flag = False
                            receiver_cash = receiver_cash + amount
                            sender_cash = sender_cash - amount
                            #update receiver
                            self.bs_Tree.update(new_user.id,"cash",receiver_cash)
                            #update sender
                            self.bs_Tree.update(user.id,"cash",sender_cash)
                            #Sender Updated info
                            update_user=self.bs_Tree.searchBykey("name",user.name)
                            self.profile(update_user)
                        else:
                            print("Unsufficient amount..")
                else:
                    print("Invalid reveicer try again..")
                    self.transferCash(user)
                print("Receiver must not be Empty..")
                self.transferCash(user)
        except Exception as err:
            print(err)
            self.transferCash(user)

if __name__ == "__main__":
    crud = cRUD()
    # crud.load_from_mongo()  #Database model for loading and store datas
    #of coure unproper installing into mac model not avaliable
    BSTree = crud.bs_Tree

    while True:
        crud.mainMenue()
        
