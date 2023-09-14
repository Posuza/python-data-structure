def phoneVali(text):
        digits = "0123456789"
        found = 0
        text =""
        phone = input(""+ text + "\n > ")
        if phone != '':
            lenght = len(phone)
            for b in phone:
                for digit in digits:
                    if digit == b:   
                        found += 1 
            if lenght == found and lenght >= 8 and lenght <= 15:
                return int(phone)
            else:
                print("phone must contain only number and \n should no t be under 8 or more than 15")
                return phoneVali(text)
        else:
            return phoneVali(text)
    
if __name__ == '__main__':
   result = phoneVali("Enter your phone")
   print(result)

   