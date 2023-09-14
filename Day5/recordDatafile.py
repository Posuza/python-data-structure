db={}

global email_exit
email_exit=-1

def main_sector():
#fixing the integer input to string input 
    print("\n # Press number Option # ")
    main_option =(input(" Press 1 register:\n Press 2 to login:\n Press 3 to exit:\n Enter here :> "))
    if main_option== "1":
        registration()
    elif main_option=="2":
        login()
    elif main_option=="3":
        recording_all_data()
        exit(1)
    else:
        print("Invalid Option")
        main_sector()

def registration():
    user_email = input("Enter your email:")
    email_get = Email_exit(user_email)

    if email_get!=None:
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
# integer input error Handling
        user_phone = integerValueChange("phone")
        user_age= integerValueChange("age")
        id = len(db)
        to_insert = {id: {"email": user_email,"u_name":user_name, "password": user_password,"phone":user_phone,"age":user_age}}
        db.update(to_insert)
        print(db)

def integerValueChange(word): 
    try:
         value = int(input("Enter your "+ word+":"))
         return value
    except ValueError:
        print(word +" Value must be digit")
        return integerValueChange(word)  
    
def login():
    user_found=-1
    print("\n This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")
    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"]==l_user_password:
            user_found=i

    if user_found!=-1:
        print("\n * Login Successful * ")
        user_profile(user_found)
    else:
        print(user_found +" Not Found ")
        login()

def user_profile(user_found):
    print(" &&Welcome: ",db[user_found]["u_name"])
    print("1# Username: ",db[user_found]["u_name"])
    print("2# Email : ",db[user_found]["email"])
    print("3# Password ",db[user_found]["password"])
    print("4# Phone : ",db[user_found]["phone"])
    print("5# Age : ",db[user_found]["age"])
    print("# Press number Option # ")
    option = int(input(" Press between 1 to 5 to update any  User Profile:\n Press 10 to Log Out:\n Enter here :> "))
    
    if option == 1:
        updateData(user_found,"u_name")
    elif option == 2:
        # updateProfile(db[user_found])
        updateData(user_found,"email")
    elif option == 3:
        updateData(user_found,"password")
    elif option == 4:
        updateData(user_found,"phone")
    elif option == 5:
        updateData(user_found,"age")    
    elif option == 10:
        recording_all_data()
        print("Data is recorded")
        print("User is log Out")
        main_sector()
    else:
        print("Invalide keyword ! \n")
        user_profile(user_found)
      
def updateData(userdata,updaInfo):
    print("Your curent "+updaInfo+":",db[userdata][updaInfo])
    if updaInfo == "phone" or updaInfo == "age":
        newData= integerValueChange(updaInfo)  
    else:
        newData = input("Enter your new "+updaInfo+": \n > ")
    if newData != "":
        db[userdata][updaInfo] = newData
        print(db[userdata][updaInfo])
        print("Your "+updaInfo+" is update to ",db[userdata][updaInfo])
        print(db)
    user_profile(userdata)


def Email_exit(email):
    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:
            return i

def recording_all_data():
    with open("new.txt", 'w') as dbfile:
        for i in range(len(db)):
            email = db[i]["email"]
            user_name = db[i]["u_name"]
            password = db[i]["password"]
            phone = db[i]["phone"]
            age = db[i]["age"]
            total_user_data = email + ' ' + user_name + ' ' + password + ' ' + str(phone) + ' ' + str(age) + ' '
            dbfile.write(total_user_data)
            dbfile.write("\n")


def loading_all_data():
    try:
        with open("new.txt",'r') as dbfile:
            datas=dbfile.readlines()
            for one in datas:
                oneData = one.split(" ")
                id = len(db)
                data_form = {id:{"email":oneData[0],"u_name":oneData[1],"password":oneData[2],
                                "phone":oneData[3],"age":oneData[4]}}
                db.update(data_form)
    except IOError:
        newFile()
 
def newFile():
    with open("new.txt","w") as note:
        print("newt file is creating")       

if __name__ == '__main__':
   loading_all_data()
   print(db)
   while True:
       main_sector()