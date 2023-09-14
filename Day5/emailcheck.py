def emailVali(test):
    acc=""
    valuereturner = False
    digits = "@."
    found =0
    tiker = 0
    a = input(""+ test+ " > ")
    acc = a
    for i in a:
        if i == "@":
            tiker += 1
        elif i ==".":
            tiker +=1
    

                  
    if a!= "" and tiker == 2:
        a2  = a.split(digits[0])
        # print(a2[0])
        # print(a2[1])
        # print(a2)
        print(a)
        for i in a2:
            if len(i) < 2:
               invalid("invalid email..",test)
            else:
                found +=1
        a3 = a2[1].split(digits[1])
        for i in a3:
            if len(i) < 2:
                invalid("invalid email..",test)
            else:
                found +=1
        if found == 4:
            valuereturner = True
            
        else:
            invalid("invalid email..",test)
            
    elif len(a) <=2 : 
        invalid("Email should be standard mail adress!",test)
    elif a =="": 
        invalid("Email should not be empty !",test)
    
    else:
        invalid("Email should be standard mail adress!",test)

    if valuereturner == True:
        return acc


def invalid(test,text):
    print(text)
    emailVali(test)
    # print(a3)
    # print(found)
    # for b in a2[0]:
    #     print(a2[0],"Informal email..")
    #     integerChange()
    # else:
    #     found= +1
    # for b in a2[0]:
    #     for b in range(len()):
    #         if digit == b:   
    #             found += 1 
    # if lenght == found:

    # print(a1[0]+"@"+"mail."+a2[1])  
    #     return a
    # else:
    #     print(a,"is invalid email")
    #     integerChange()
if __name__ == '__main__':
   result = emailVali("Enter Email")
   
   print("result",result)
   
   