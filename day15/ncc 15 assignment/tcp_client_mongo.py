import socket
import json


class TCPclient():
    def __init__(self, sms):
        self.target_ip = 'localhost'
        self.target_port = 9997
        self.input_checking(sms)

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
            self.register()
        else:
            print("Invalid new_info")

    def get_all_data(self, sms):
        client = self.client_runner()
        sms = bytes(sms + ' ', "utf-8")
        client.send(sms)
        received_from_server = client.recv(4096)
        # print(received_from_server.decode("utf-8"))

        dict_data: dict = json.loads(received_from_server.decode("utf-8"))
        print(type(dict_data))
        print(dict_data)
        client.close()

    def login(self, info):
        try:
            print("\n @login Form..")
            l_email = input("Enter your email to login: \nor \'reg\' to register: \nor \'exit\' to exit: >")
            if l_email == "exit":
                exit(1)
            elif l_email == "reg":
                self.register()

            l_pass = input("Enter your password to login: >")

            client = self.client_runner()
            sms = info + ' ' + l_email + ' ' + l_pass  # login email password
            sms = bytes(sms,"utf-8")
            client.send(sms)
            
            received_from_server = client.recv(4096)
            user_info: dict = json.loads(received_from_server.decode("utf-8"))
            self.new_info_choice(user_info, client)
            client.close()


        except Exception as err:
            print(err)

    def new_info_choice(self, user_info, client):
        print("\n@you are login...")
        print("Userame: ",user_info["name"])
        print("Point :", user_info["point"])
        print("Bio  :", user_info["info"])
        print(" @Main Option.. ")
        try:
            new_info = input("Press 1 @User Option..:\nPress 2 @Logout..: >")
            if new_info == '1':
                self.user_new_info(user_info, client)
            elif new_info == '2':
                print(" \n @you are loging out..")
                self.input_checking("login")  # to write more new_info
            else:
                print("Invalid new_info [X]")
                self.new_info_choice(user_info, client)

        except Exception as err:
            print(err)

    def user_new_info(self, user_info, client):
        try:
            new_info = input("\n    *** Option ****\nPress 1 To Vote:\nPress 2 to get more points:\nPress 3 to Transfer Point:\n"
                           "Press 4 To get Voting Ranking:\nPress 5 to change user information \nPress 6 to Delete Acc:\nPress 7 "
                           "to Exit:")

            if new_info == '1':
                self.votingSection(user_info,client)
            elif new_info == '2':
                self.get_more_point(user_info,client)
            elif new_info == '3':
                self.transfer_point(user_info,client)
            elif new_info == '4':
                self.voting_rank(user_info)
            elif new_info == '5':
                self.info_change(user_info,client)
            elif new_info == '6':
                self.account_delete(user_info,client)
            elif new_info == '7':
                self.new_info_choice(user_info, client)
            else:
                print("Invalid new_info")
                self.user_new_info(user_info, client)

        except Exception as err:
            print(err)
            self.user_new_info(user_info, client)

#delet account
    def account_delete(self,user_info,client):
            print(user_info["email"]," try to delete")
            while True:
                confirm = input("Type \'yes\' to confirm or \'no\' to cancel: >")
                if confirm == "no":
                    print("@You have cancel the confirmation..")
                    self.new_info_choice(user_info,client)
                    break

                elif confirm == "yes":
                    data_form = "delete_user" + " " + user_info["email"]
                    client = self.client_runner()
                    client.send(bytes(data_form, "utf-8"))

                    received = client.recv(4096).decode("utf-8")
                    client.close()
                    print(received)
                    self.login("login")
            
#¨Change user infomation
    def info_change(self,user_info,client):
            print("\n  @Your Information.. ")
            print("username :", user_info["name"])
            print("Email :", user_info["email"])
            print("Password :", user_info["password"])
            print("Phone no :", user_info["phone"])
            print("Info :", user_info["info"])

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
                    data = "password" + " " + password

                elif new_info == 4:
                    phone =self.phoneVali("Enter Your new phone no :> ",user_info["phone"])
                    data = "phone" + " " + str(phone)

                elif new_info == 5:
                    info =self.update_information("Enter Your new info :> ","info",user_info)
                    new_info = info.replace(" ","_")
                    data = "info"+ " " + new_info

                elif new_info == 6:
                    self.new_info_choice(user_info, client)
                else:
                    print("Invalid new_info")
                    self.user_new_info(user_info, client)

                data_form = "update_info" + " " + user_info["email"] + " " + data
                print(data_form)
                
                print(data_form)
                client = self.client_runner()
                client.send(bytes(data_form, "utf-8"))

                received_from_server = client.recv(4096)
                user_info: dict = json.loads(received_from_server.decode("utf-8"))
                client.close()
                print(user_info)
                self.info_change(user_info, client)

            except Exception as error:
                print(error,"invalide number! ")
                self.info_change(user_info,client)

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
                        return new
        #update email         
                    elif info == "email":
                        check =self.email_checking(new)
                        email_exit = self.email_check_inDB(new)
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
                            newPassword = ""
                            while  True:
                                passwrod1 = self.password_check("Enter your new password: >")
                                password2 = input("new password Again: >")
                                if passwrod1 == password2:
                                    newPassword = password2
                                    break
                                else:
                                    print("@Password don't match try again!... ")           
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

#Get more points
    def get_more_point(self,user_info,client):
        points = user_info["point"]
        print("your Point :", points)
        try: 
            morePoint= int(input("Enter amout of your point 1 for 10 Dollars :>  "))
            points = points + morePoint

            client = self.client_runner()
            sms = "more_point" + ' ' + user_info["email"] + ' ' + str(points)  # more point email password
           

            sms = bytes(sms,"utf-8")
            client.send(sms)
            received_from_server = client.recv(4096)
            user_info: dict = json.loads(received_from_server.decode("utf-8"))

            self.new_info_choice(user_info, client)
            client.close()
        
        except Exception as error:
            print(error,"invalid number")
            self.get_more_point(user_info, client)

#voting Ranking
    def voting_rank(self,user_info):
        client = self.client_runner()
        sms = bytes("candidate_info", "utf-8")
        client.send(sms)

        info = client.recv(4096)
        candi_info = json.loads(info.decode("utf-8"))
        client.close()

        rank_list = []
        for i in candi_info:
            rank_list.append((int(candi_info[i]["vote_point"]),candi_info[i]["name"]))
              
        for i in range(len(rank_list)):
            for j in range(i+1,len(rank_list)):
                if rank_list[i][0] < rank_list[j][0]:
                    rank_list[i],rank_list[j] = rank_list[j],rank_list[i]

        print("   # Candidates Ranking #   ") 
        for i in range(len(rank_list)):
            j = i+1
            print("No: ", j, "Name: ", rank_list[i][1], "vote", rank_list[i][0])
            i = i+1

        self.user_new_info(user_info, client)


#voting Section
    def votingSection(self, user_info, client):
        client = self.client_runner()
        sms = bytes("candidate_info", "utf-8")
        client.send(sms)

        info = client.recv(4096)
        candi_info = json.loads(info.decode("utf-8"))
        # print(candi_info)
        # print(type(candi_info))
        print(" $:1 vote for 10 points")
        for i in candi_info:
            print("No: ", i, "Name: ", candi_info[i]["name"], "vote", candi_info[i]["vote_point"])
        client.close()
        self.selec_candidate(candi_info,user_info, client)

#Select candidate Section
    def selec_candidate(self,candi_info,user_info, client):
        if user_info["point"] < 10:
            print("Unsuficient Point, plz add your point to vote!")
            self.new_info_choice(user_info, client)
        try:
            candidate =input("Choose number your canditate to vote type \'no\' to cancel \n   > ")
            if candidate == "no":
                self.user_new_info(user_info, client)
            candidate = int(candidate)   
            flag = -1
            candiName =""
            candiVote =0
            for i in candi_info: 
                if candidate == int(i):  
                    flag = 1
                    candiName =candi_info[i]["name"]
                    candiVote =candi_info[i]["vote_point"]
                    break
                else:
                    flag = -1
            if flag == 1:
                
                print(type(user_info["point"]))
                user_info["point"] = user_info["point"] - 10
                print(user_info["point"])

                candiVote = candiVote + 1
                print(candiVote)
                print(type(candiVote))
                vote_form = "vote" + " " + candiName + " " + str(candiVote) + " " + user_info["email"] + " " + str(user_info["point"])
                print(vote_form)

                client = self.client_runner()
                client.send(bytes(vote_form, "utf-8"))
                
                received_from_server = client.recv(4096)
                candi_info: dict = json.loads(received_from_server.decode("utf-8"))
                client.close()

                for i in candi_info:
                    print("No: ", i, "Name: ", candi_info[i]["name"], "vote", candi_info[i]["vote_point"])
                client.close()
                self.selec_candidate(candi_info,user_info, client)

            else:  
                print(" plz select a valid canditate ..")
                self.selec_candidate(candi_info,user_info, client)
            
        except Exception as err:
            print(err,"select candidate ! error plz select a valid canditate ..")
            self.selec_candidate(candi_info,user_info, client)

#Transfer Points 
    def transfer_point(self,user_info,client):
            print("your point Point :", user_info["point"])
            userPoint = int(user_info["point"])
            count = 0
            if userPoint > 0:
                try:
                    point = int(input("Enter your pioint to transfer :> "))
                    if  point <= userPoint:
                        trans_user =  self.transferUser(user_info,client)
                        tranUserPoint =int(trans_user["point"])
                      
                        tranUserPoint = tranUserPoint + point
                        userPoint = userPoint - point

                        data_form = "update_point" + " " + trans_user["email"] + " " + str(tranUserPoint) + " " + user_info["email"] + " " + str(userPoint)
                        
                        client = self.client_runner()
                        client.send(bytes(data_form, "utf-8"))
                        
                        received_from_server = client.recv(4096)
                        user_info: dict = json.loads(received_from_server.decode("utf-8"))
                        print(user_info)
                        print("@Transfering successful....")
                        self.new_info_choice(user_info, client)
                        client.close()

                    else:
                        print("U have unsficient point to transfer ...")
                        self.transfer_point(user_info,client)

                except Exception as error:
                    print(error,"invalid transfer plz try again")
                    self.transfer_point(user_info,client)
            else:
                print("unsficient point to transfer! buy more point..")
                self.user_new_info(user_info, client)

#transfer user Checking validation
    def transferUser(self,user_info,client):
            count =0
            while True:
                if count == 3:
                    self.user_new_info(user_info,client)
                    break
                email = input("Enter your transfer email :")
                client = self.client_runner()
                sms ="transfer_email" + ' ' + email 
                sms = bytes(sms,"utf-8")
                client.send(sms)

                received_from_server = client.recv(4096)
                data = received_from_server.decode("utf-8")
                print(data)
                if data == "invalid_email!":
                    count = count +1
                else:
                    user_info = json.loads(data)
                    print("email_exit ",user_info["email"])
                    return user_info
                    
#Register
    def register(self):
        print("\n  @registration Form... ")
        r_email = ''
        while True:
            r_email = input("Enter email for registration: \nor type login to go back: >")
            if r_email=="login":
                self.login("login")
            flag = self.email_checking(r_email)  # 1 or -1

            if flag == 1:
                break
            else:
                print("Email Form Invalid\nTry Again! ")

        print("Email From Valid ")

        try:
            new_info = input("Press 1 Registration for Voter:\nPress 2 Registration for Candidate!: >")

            if new_info == '1':
                self.reg_for_voter(r_email)
            elif new_info == '2':
                self.reg_for_candidate(r_email)

            else:
                self.register()
        except Exception as err:
            print(err)

#email check
    def email_checking(self, r_email):
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
        
#Register voter
    def reg_for_voter(self, r_email):

        if self.email_check_inDB(r_email):
            try:
                username = input("Enter your voter username :")
                if username =="":
                    username = "Candi_User"
                pass1 = self.password_check("Enter your password to register:")
                pass2 = input("Enter your password Again  to register:")

                if pass1 == pass2:
                
                    print("Password Was match!")
                    phone =self.phoneVali("Enter Your new phone no :> ","09000000")

                    data_list = [username,r_email, pass1, phone]
                    print(data_list)
                    self.final_registration(data_list,"voter")

                else:
                    print("Password not match:")
                    self.reg_for_voter(r_email)


            except Exception as err:
                print(err)

        else:

            print("Your email was already register!")
            self.register()

#register candidate
    def reg_for_candidate(self, r_email):

        if self.email_check_inDB(r_email):
            try:
                username = input("Enter your Candidate username :")
                if username =="":
                    username = "User"
                pass1 = self.password_check("Enter your password to register :")
                pass2 = input("Enter your password Again  to register:")

                if pass1 == pass2:

                    print("Password Was match!")
                    phone =self.phoneVali("Enter Your new phone no :> ","09000000")

                    data_list = [username,r_email, pass1, phone]
                    self.final_registration(data_list,"canditate")

                else:
                    print("Password not match:")
                    self.reg_for_candidate(r_email)


            except Exception as err:
                print(err)

        else:

            print("Your email was already register!")
            self.register()

#checking Email in DB
    def email_check_inDB(self, email):

        client = self.client_runner()
        data = "emailcheck" + " " + email

        client.send(bytes(data, "utf-8"))

        received = client.recv(4096).decode("utf-8")

        print(received)

        if received == "notExist":
            client.close()
            return 1
        else:
            client.close()
            return -1

#Registeration final
    def final_registration(self, data_list,userdata):
        while True:
            confirm = input("Type \'yes\' to confirm or \'no\' to cancel: >")
            if confirm == "no":
                print("@You have cancel the confirmation..")
                self.register()
                break
            elif confirm == "yes":
                if userdata == "canditate":
                    data_form = "candidate_register" + " " + data_list[0] + " " + data_list[1] + " " + data_list[2] + " " + str(data_list[3]) + " " + "Update_your_user_info" + " " + "0"
                    print(data_form)
                else:
                    data_form = "voter_register" + " " + data_list[0] + " " + data_list[1] + " " + data_list[2] + " " + str(data_list[3]) + " " + "UUpdate_your_user_info" + " " + "0"

                client = self.client_runner()
                client.send(bytes(data_form, "utf-8"))

                recv = client.recv(4096).decode("utf-8")
                client.close()
                print(recv)

                if recv:
                    print("Registration Success!",recv)
                    info="login"
                    self.login(info)
                    break
            else:
                print("@Invalid input for the confirmation..")

            

#phone numbe validation
    def phoneVali(self,text,old_phone):
            
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
                    return self.phoneVali(text,old_phone)
            else:
                return int(old_phone)
            
#checkig password in DB
    # def password_check_db(self):
    #     def email_check_inDB(self, email):

    #     client = self.client_runner()
    #     data = "emailcheck" + " " + email

    #     client.send(bytes(data, "utf-8"))

    #     received = client.recv(4096).decode("utf-8")

    #     print(received)

    #     if received == "notExist":
    #         client.close()
    #         return True
    #     else:
    #         client.close()
    #         return False

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


if __name__ == "__main__":
    while True:
        sms = input("Enter some data to send or type \'exit\' to exit: >")
        if sms == "exit":
            exit(1)
        tcp_client = TCPclient(sms)