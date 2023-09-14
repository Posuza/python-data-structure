def transferUser():
            count = 0
            while True:
                email = input("Enter your transfer email :")
    
                if email == "invalid_email!":
                    count = +1
                else:
                    print("email_exit ")
                    return 1
                    b