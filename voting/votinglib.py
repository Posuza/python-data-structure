class Voting:
    
    def __init__(self):
        print("Working in Voting special method or constructor ")

        self.students = {0: {"name": "James", "v_mark": 0, "voter": []},
                         1: {"name": "John", "v_mark": 0, "voter": []},
                         2: {"name": "Rooney", "v_mark": 0, "voter": []},
                         3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                         4: {"name": "Messi", "v_mark": 0, "voter": []}
                         }
        self.db: dict = {}
        self.maindb: dict = {0:self.db,1:self.students}
        self.id: int = 0
        self.l_id: int = 0
        self.loadAllData()
        print("data is loaded")
        print(self.db)
        print(self.students)
        self.count = 0

#save data 
    def recording_all_data(self):
        with open("new.txt","w") as note:
            print("db \n",self.db)
            data={0:self.db,1:self.students}
            self.maindb.update(data)
            print("data \n",data)
            for element in self.maindb:
                note.write(str(self.maindb[element]))
                note.write("\n")  
        print("data is recoreded")

#retrieve data 
    def loadAllData(self):
        try:
            with open("new.txt","r") as note:
             id =0
             for line in note: 
                text = line.strip()
                result= eval(text)
                data = {id:result} 
                id += 1
                self.maindb.update(data)
            self.db.update(self.maindb[0])
            self.students.update(self.maindb[1])
        except IOError:
            self.newFile()

    def newFile(self):
        with open("new.txt","w") as note:
            print("newt file is creating") 

#main option
    def main_option(self):
        option = 0
        try:
            option = int(input("\nPress 1 to Register\nPress 2 to Login\nPress 3 to Exit \n >  "))
        except Exception as err:
            # print(err)
            print("Pls insert only Integer eg:1,2,3")

        if option == 1:
            self.register()
        elif option == 2:
            self.login()
        elif option == 3:
            self.recording_all_data()
            exit(1)
        else:
            print("Invalid Option")
            self.main_option()
#register
    def register(self):
        print(" # This is register option ")
        pass_match = False
        try:
            user_email = input("Enter your email! > ")
            r_email = self.Email_exit(user_email)
            if r_email != None:
                print("Email already exit:")
                self.register()
            else:
                r_name = input("Enter your name! > ")
                r_phone = int(input("Enter your phone! > "))
                r_address = input("Enter your address: > ")
                while pass_match is False:
                    r_pass1 = input("Enter your password! > ")
                    r_pass2 = input("Retype your password:")
                    if r_pass1 != r_pass2:
                        print("Your passwords not match")
                    else:
                        print("Your passwords was recorded!")
                        self.id = len(self.db)
                        data_form: dict = {self.id: {"email": user_email, "name": r_name, "phone": r_phone,"address": r_address, "password":r_pass1,"credit":0}}
                        self.db.update(data_form)
                        pass_match = True
        except Exception as err:
            print("Invalid User Input!Try Again Sir!")
            self.register()

        print("Registration success :", self.db[self.id]["name"])
        print(self.db)
        r_option = False
        while r_option is False:
            try:
                user_option = int(input("\nPress 1 to Login!\nPress 2 Main Option:\nPress3 to Exit!:\n > "))
                if user_option == 1:
                    self.login()
                    break
                elif user_option == 2:
                    self.main_option()
                    break
                elif user_option == 3:
                    self.recording_all_data()
                    exit(1)
                else:
                    print("Pls read again for option!")
            except Exception as err:
                print("Invalid Input!", err)
#login
    def login(self):
        print(" # This is login option ")
        length = len(self.db)
        try:
            l_email = input("Enter your email to Login:")
            l_pass = input("Enter your pass to Login:")
            self.l_id = -1
            
            for i in range(length):
                if l_email == self.db[i]["email"] and l_pass == self.db[i]["password"]:
                    self.l_id = i
                    break
            if self.l_id != -1:
                self.user_sector(self.l_id)
                
            else:
                print("Username or Password incorrect!")
                try:
                    self.option = int(input("Press 1 to exit > "))
                    if self.option ==1:
                            self.main_option()
                    else:
                        print("Invalid number")
                        self.login()
                except ValueError:
                     print("Invalid number")
                     self.login()

        except Exception as err:
            print(err, "\nInvalid input:")
#profile
    def user_sector(self, l_id):  
        print("Welcome", self.db[l_id]["name"])
        print("Your have: $"+ str(self.db[l_id]["credit"]))

    #buying coin 
        self.buyCoin(l_id,self.count)
        print(self.db[l_id]["credit"])

        print("Please select one!")
        for i in range(len(self.students)):
            print("Id: {} - Name: {} - Current Vote Mark: {}".format(i, self.students[i]["name"],self.students[i]["v_mark"]))
        try:
            v_id = int(input("Just Enter Id number to vote or Press 10 to leave!\n ")) 
            self.db[l_id]["credit"] = self.db[l_id]["credit"]-5000
            self.students[v_id]["v_mark"] += 1
            self.students[v_id]["voter"].append(self.db[l_id]["name"])
            
            print("Congratulation you are voted!")
            print("{} now voting mark is : {}".format(self.students[v_id]["name"],self.students[v_id]["v_mark"]))
            self.voterCount = 0
            for i in range(len(self.students[v_id]["voter"])): 
                if self.students[v_id]["voter"][i] == self.db[l_id]["name"]:
                    self.voterCount =self.voterCount+1
            print("You have already voted to {} for {} times".format(self.students[v_id]["name"],self.voterCount))            
        except Exception as err:
            print("Invalid Number")

        for i in range(len(self.students)):
            self.countvoter = 0
            print(self.students[i]["name"]) 
            for v in (self.students[i]["voter"]):   
                if v == self.db[l_id]["name"]:
                    self.countvoter =self.countvoter+1
            print("You have already voted to {} for {} times".format(self.students[i]["name"],self.countvoter))   

        while True:
            try:
                vote_option = int(input("Press 1 to Vote Again!\nPress 2 to get Main Option!\nPress 3 to Buy more coins!\nPress 4 to Force Quit:"))

                if vote_option == 1:
                    self.user_sector(l_id)
                    break
                elif vote_option== 2:
                    self.main_option()
                    break
                elif vote_option == 4:
                    self.recording_all_data()
                    self.main_option()
                elif vote_option == 3:
                    self.count= 1
                    self.user_sector(l_id)
                else:
                    print("Invalid option after vote!")
            except Exception as err:
                print(err)
#email already exist             
    def Email_exit(self,email):
        lenght = len(self.db)
        for i in range(lenght):
            if self.db[i]["email"] == email:
                return i
    
    def buyCoin(self,l_id,count):
        while self.db[l_id]["credit"] < 5000 or count == 1:
            print(self.db[l_id]["credit"])
            print("Your have $"+str(self.db[l_id]["credit"])+ " Plese purchase more coin to enjoin! ")
            try:
                coin = int(input("Buy Your coin for 1 is 5000kyat \n > "))
                self.db[l_id]["credit"] = self.db[l_id]["credit"]+coin
                count = 0 
            except ValueError:
                print("Invalid number")
        self.count = 0        

