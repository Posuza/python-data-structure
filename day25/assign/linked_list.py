class Node():

     def __init__(self,id,name,phone,email,password,cash,next):
          self.id = id
          self.name = name
          self.phone = phone
          self.email = email
          self.password = password
          self.cash = cash
          self.next = next

class linked_list:
     def __init__(self):
       self.head = None

#Prepend
     def prepend(self,id,name,phone,email,password,cash):
         node = Node(id,name,phone,email,password,cash,self.head)
         self.head  = node
     
#Append
     def append(self,id,name,phone,email,password,cash):
          if self.head is None:
               self.head = Node(id,name,phone,email,password,cash,self.head)
               return
          itr = self.head
          while itr.next:
               itr = itr.next
          itr.next =Node(id,name,phone,email,password,cash,None)
              

#search element 
     def findElement(self,id=None,name=None,phone=None,email=None,password=None,cash=None):
          if self.head is None:
             print("linked list is empty")
             return -1 
          
          itr = self.head

          while itr: 
               if id != None:
                  if  itr.id == id:
                       return itr
               if name != None:
                  if itr.name == name:
                     return itr      
               if phone != None:
                    if itr.phone == phone:
                         return itr
               if email != None:
                    if itr.email == email:
                         return itr
               if password != None:
                    if itr.password == password:
                         return itr  
               if cash != None:
                    if itr.cash == cash:
                         return itr

               if itr.next is None:
                    # print("invalid value")
                    return -1 
               itr = itr.next

#Print
     def print(self):
        if self.head is None:
             print("linked list is empty")
             return
        itr = self.head
        while itr:
            print(itr.id,itr.name,itr.phone,itr.email,itr.password,itr.cash)
            if itr.next is not None:
                    print("👇")      
            itr = itr.next

#length
     def length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
     
#Insert by index
     def insertByIndex(self,index,id,name,phone,email,password,cash):
          if index<0 or index >self.length():
               raise Exception("Invalid index")
          
          if index == 0:
               self.prepend(id,name,phone,email,password,cash)
               return
          if index == self.length:
               self.append(id,name,phone,email,password,cash)
               return

          count = 0
          itr = self.head
          while itr:
               if count == index -1:
                    node = Node(id,name,phone,email,password,cash,itr.next)
                    itr.next = node
                    break
               itr = itr.next
               count = count +1

#delete by idex
     def deleteByIndex(self,index):
          if index<0 or index >=self.length():
               raise Exception("Invalid index")
          
          if index == 0:
               print("Dleted ID:",self.head.id)
               self.head = self.head.next
               # print("deldNode next:",self.head.id)
               return
          
          count = 0
          itr = self.head
          while itr:
               if count == index -1:
                    # print("prev ID:",itr.id)
                    print("Dleted ID:",itr.next.id)
                    itr.next = itr.next.next
                    # print("deledNode.next:",itr.next.id)
                    itr = None
                    break
               itr = itr.next
               count = count +1

#delete by id
     def deleteById(self,id):
          if self.head is None:
             print("linked list is empty")
             return
          
          if self.head.id == id:
               print("Dleted ID:",self.head.id)
               self.head = self.head.next
               # print("deldNode next:",self.head.id)
               return
          
          itr = self.head     
          while itr:
               prev = itr  
               # print("preve",prev.id) 
               if prev.next is not None:
                    curent =itr.next
                    # print("current",curent.id,curent.name)
                    
                    if curent.id is id:
                         print("deleNode",curent.id,curent.name)
                         prev.next = curent.next
                         # print("prev update",prev.next.id)
                         curent = None

               else:
                    print("preint")
                    break
               itr = itr.next  
     
#update by index
     def updateByIndex(self,index,name=None,phone=None,email=None,password=None,cash=None):
          if index<0 or index >=self.length():
               raise Exception("Invalid index")
                
          if index == 0:
               if name != None:
                    self.head.name = name
               if phone != None:
                    self.head.phone = phone
               if email != None:
                    self.head.email = email
               if password != None:
                    self.head.password = password
               if cash != None:
                    self.head.cash = cash
               print("Updated id:",self.head.id)
               return
          
          count = 0
          itr = self.head
          while itr:
               if count == index:
                    if name != None:
                         itr.name = name
                    if phone != None:
                         itr.phone = phone
                    if email != None:
                         itr.email = email
                    if password != None:
                         itr.password = password
                    if cash != None:
                         itr.cash = cash
                    print("Updated id:",itr.id)
                    break
               itr = itr.next
               count = count +1

#update by id
     def updateById(self,id,name=None,phone=None,email=None,password=None,cash=None):
          if self.head is None:
             print("linked list is empty")
             return    
          # if self.head.id == id:
          #      self.head.name = name
          #      self.head.phone = phone
          #      self.head.email = email
          #      self.head.password = password
          #      self.head.cash = cash
          #      print("Updated id:",self.head.id)
          #      return
          itr = self.head
          while itr:
               if itr.id == id:
                    if name != None:
                         itr.name = name
                    if phone != None:
                         itr.phone = phone
                    if email != None:
                         itr.email = email
                    if password != None:
                         itr.password = password
                    if cash != None:
                         itr.cash = cash
                    print("Updated id:",itr.id)
                    break
               if itr.next is None:
                    print(id," is invalid id")  
               itr = itr.next


if __name__ == '__main__':
     ll = linked_list()
     lc = linked_list()
     # id = 0
     # def inset(id):
     #      name = input("Enter Your Name")
     #      phone = input("Enter Your phone")
     #      email = input("Enter Your email")
     #      passwrd = input("Enter Your passwrd")
     #      cash = input("Enter Your cash")
     #      ll.append(id,name,phone,email,passwrd,cash)

     # while True:
     #      confirm = input("Type \'no\' to stop: or any key to continue >")
     #      if confirm == "no":
     #            print("@You have stop the operation..")
     #            ll.print()
     #            break
     #      id = id+1
     #      inset(id)

     print("\n")
     ll.append(1,"MgMg",11,"mgmg@gmail.com","12435135",1000)
     ll.append(2,"Ko",14,"komg@gmail.com","12435135",0)
     ll.append(3,"KoMg",12,"komg@gmail.com","12435135",0)
     ll.prepend(4,"KoMg",13,"komg@gmail.com","12435135",0)
     ll.insertByIndex(0,0,"Mg",11,"mgmg@gmail.com","12435135",1000)
     ll.insertByIndex(5,5,"MgMg",11,"mgmg@gmail.com","12435135",1000)
     
     lc.append(1,"MgMg",11,"mgmg@gmail.com","12435135",1000)
     lc.append(2,"Ko",14,"komg@gmail.com","12435135",0)
     lc.append(3,"KoMg",12,"komg@gmail.com","12435135",0)
     lc.prepend(4,"KoMg",13,"komg@gmail.com","12435135",0)
     lc.insertByIndex(0,0,"Mg",11,"mgmg@gmail.com","12435135",1000)
     lc.insertByIndex(5,5,"MgMg",11,"mgmg@gmail.com","12435135",1000)
     
     ll.print()
     print("\n lc")
     lc.print()

     # element =ll.findElement(None,"jo",None,None,None,None)
     # print(type(element))
     # print(element.id,element.name)

     # # ll.deleteByValue(3)
     # # ll.deleteByValue(2)
     # # ll.deleteByIndex(1)

     # # ll.delete(3)
     # # ll.delete(2)
     # # ll.delete(1)
     # # ll.print()
     # # ll.delete(0)
     # # ll.deleteByValue(0)
     # ll.updateByIndex(0,"MgKO",None,"mgmg@gmail.com","12435135",1000)
     # ll.updateById(-1,11,)
     # ll.updateById(5,"Chit",11,None,None,5000)
     # ll.updateByIndex(5,7)
     # print("\n")
     # ll.print()


