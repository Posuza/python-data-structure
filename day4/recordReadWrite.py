db ={}
 
email_exist = -1

def mainSector():
    print("\n # Press number Option # ")
    option = int(input(" Press 1 register:\n Press 2 to login:\n Press 3 to exit:\n Enter here :> "))
    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        exit(1)
    else:
        print("Invalid Number")
        mainSector()

def register():
    user_email = input("Enter your email: ")
    email_get = emailExist(user_email)
    if email_get != None:
        print("Email already exist")
        register()
    else:
        user_name = input("Enter your name: ")
        user_pass = int(input("Enter your password: "))
        user_phone = input("Enter your phone: ")
        user_age = input("Enter your age: ")
        id = len(db)
        data = {id:{"u_email":user_email,"u_name":user_name,"u_pass":user_pass,"u_phone":user_phone,"u_age":user_age}}
        db.update(data)
        print(db)
        user_updated()
        login()

def login():
    user_found = -1
    print("# Login Sector #")
    loginUser_email = input("Enter your email:> ")
    loginUser_pass = int(input("Enter your password:> "))

    for i in range(len(db)):
        if db[i]["u_email"] == loginUser_email and db[i]["u_pass"] == loginUser_pass:
            user_found = i
    if user_found != -1:
        print("\n * Login Successful * ")
        userProfile(user_found)
    else:
        print("user: "+ loginUser_email + " not found")
        option = int(input("Press 1 to go back :__"))
        if option==1:
            mainSector()
        else:
            login()

def userProfile(user_found):
    print("\n * Profile * ")
    print("Welcome", db[user_found]["u_name"]+"\n")

    option = int(input("Press 1 to exit or any number to going back"))
    if option==1:
        recordAllData()
        print("Data is recorded")
        exit(1)
    else:
        mainSector()


def emailExist(email):
    length = len(db)
    for i in range(length):
        if db[i]["u_email"] == email:
            return i

def user_updated():
    print("  ## Successful Register ##") 
    for i in db:
        print("user :"+ db[i]["u_name"]+" updated")

#record all data from txt
def recordAllData():
     with open("newtext2.txt","a") as note:
        for element in db:
            note.write(str(db[element]))
            note.write("\n")

def loadAllData():
    try:
        with open("newtext2.txt") as note:
            for line in note:  
                id = len(db)
                text = line.strip()
                result= eval(text)
                data = {id:result} 
                db.update(data)
                print(db)
    except IOError:
        newFile()

def newFile():
    with open("newtext2.txt","w") as note:
        print("newtext2 file is creating")

#main            
if __name__ == '__main__':
    loadAllData()
   
    while True:
        mainSector()