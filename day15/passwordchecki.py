def password_valid(password):
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
    print(count,"count")
    print(found,"found")
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
             

if __name__ == '__main__':
        
    while True:
        password =input("Enter password email ")
        result =password_valid(password)
        if password == result:
            print(password)
