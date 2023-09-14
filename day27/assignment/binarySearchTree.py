class Node:
    def __init__(self,id,name,phone,email,password,cash):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.cash = cash
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

 
#insertion
    def addData(self,id,name,phone,email,password,cash):
        if self.root is None:
            self.root = Node(id,name,phone,email,password,cash)
            return self.root
        else:
            self.__addChild(id,name,phone,email,password,cash,self.root)

    def __addChild(self,id,name,phone,email,password,cash,node):

        if node is None:
            # print(id)
            new_node = Node(id,name,phone,email,password,cash)
            return new_node
        
        if node.id == id:
            return node
        if id < node.id:
            node.left =self.__addChild(id,name,phone,email,password,cash,node.left)
        else:
            node.right =self.__addChild(id,name,phone,email,password,cash,node.right)
        return node
#Print
    def showdatas(self):
        if self.root is not None:
            self.__show_all_data(self.root,0,"")
        else:
            print("No value in database yet!")
            return None

    def __show_all_data(self,node,count,key):
        l = count
        R  = count
        
        # col = count*2
    #Preorder
    # if node:
    #     show_all_data(node.left,l+1,"l")
    #     show_all_data(node.right,R+1,"R")
    #     print(l*"-",R*"-",node.data)

    #Postorder
        # if node:
        #     print(l*"-",R*"-",node.data)
        #     self.__show_all_data(node.left,l+1,"l")
        #     self.__show_all_data(node.right,R+1,"R")
    #Inorder            
        if node is not None:
            col = R+l
            self.__show_all_data(node.left,l+1,"l")

            # print(l*"-",R*"-",">",node.id)
            # if col == R+l:
            #     self.i[col] +=[node.id]
            # i = +1
            # data = {i:{"space":col,"value":node.id}}
            # self.i.update(data)
            print(l*"-",R*"-",">",node.id,node.name,node.phone,node.email,node.password,node.cash)
            self.__show_all_data(node.right,R+1,"R")
        

#find miximum value
    def find_max(self):
        if self.root:
            return self.__find_max(self.root)
        print("Empty tree!")
        return -1
    
    def __find_max(self,node):
            if node.right is None:
                return node    #retun the whone max_node
            return self.__find_max(node.right)
            
#find minimum value
    def find_min(self):
        if self.root:
            return self.__find_min(self.root)
        print("Empty tree!")
        return -1
    
    def __find_min(self,node):
            if node.left is None:
                return node   #retun the whone min_node
            return self.__find_min(node.left)

#search value
    def search(self,value):
        if self.root:
            node=  self.__search(self.root,value)
            # print(node)
            if node is not None:
                return self.__search(self.root,value) 
            print("invalid search data!")
            return None
        print("Empty database!")
        return None
    
    def __search(self,node,value): 
     
        if node:
            if node.id == value or node.name == value or node.phone == value or node.email == value:
                # print(node.id)
                return node    
            else:
                return self.__search(node.left,value) or self.__search(node.right,value)  
        return None
    
#search value by key
    def searchBykey(self,key,value):
        if self.root:
            if self.__searchBykey(self.root,key,value):
                return self.__searchBykey(self.root,key,value)
            print("invalid value! ")
            return None
        print("Empty database!")
        return None
    
    def __searchBykey(self,node,key,value): 
     
        if node:
            # print(node.id)
            if key == "id":
                if node.id == value:
                    return node
            elif key == "name":
                if node.name == value:
                    return node
            elif key == "phone":
                if node.phone == value:
                    return node
            elif key == "email": 
                if node.email == value:
                    return node
            return self.__searchBykey(node.left,key,value) or self.__searchBykey(node.right,key,value) 
            
        return None

#deleting
    def leght(self,node):
        if node is None:
            return 0
        l=self.leght(node.left)
        r=self.leght(node.right)
        return 1+l+r
         


    def delete(self,id):
        if self.root:
           return self.__delete1(self.root,id)
          
        print("No value to delet in database")
        return None

    def __delete1(self,node,key):
        if not node: return None


        if node.id == key:
            # if pointer1.left.id == key or pointer1.right.id == id:
            #     node = pointer1.left or pointer1.right
            #     print("pointer",pointer1.id)
            #     print("node",node.id)
            print(key,"has deleted!")
            if not node.left and not node.right:
                print("delete leave node")
                node = None
                return node
            if not node.left and node.right: 
                if self.leght(self.root) == 2:
                    self.root = node.right
                    print("rheig")
                    return self.root
                else:
                    print("r")
                    node = node.right
                    return node 
            if not node.right and node.left:
                if self.leght(self.root) ==2:
                    self.root = node.left
                    print("lhe")
                    return self.root
                else:
                    print("l")
                    node = node.left
                    return node
            #if both exit
                #if both left,right exit
            pointer = node.right
            while pointer.left : pointer = pointer.left #return most left node
            print(node.id,"node")
            # print(node.right.data,"node right")
                 #replace valaue
            node.id = pointer.id 
            node.name = pointer.name   
            node.phone = pointer.phone
            node.email = pointer.email
            node.password = pointer.password
            node.cash = pointer.cash
            # print(node,"node")
            # print(node.right.data,"node right")
                #replace all most left node sub tree to root.rigth 
            node.right = self.__delete1(pointer.right,key)

        elif node.id > key:
            node.left = self.__delete1(node.left,key)
        else:
            node.right = self.__delete1(node.right,key)
        return node
     
#updating 
    def update(self,id,key:str,data):
        if self.root:
            infos =["name","phone","email","password","cash"]
            for info in infos:
                # print(info)
                if key == info:
                    return self.__updateData(id,key,data)  
                else:
                    print("Invalid key!")
            return None         
        print("No data to edit!")
        return None

    def __updateData(self,id,key,new_data):  
        node = self.searchBykey("id",id)
        if node is None:
            print("invlid data id !")
            return None
        if self.searchBykey(key,new_data):
            print(new_data,"is exist",self.search(new_data).id)
            return None
        # if node.id != self.search(new_data).id:
        if node:
            if key == "name":
                node.name = str(new_data)
            elif key == "phone":
                node.phone = int(new_data)
            elif key == "email":
                node.email = str(new_data)
            elif key == "password":
                node.password = str(new_data)
            elif key == "cash":
                node.cash = int(new_data)
            
            print("value edited")
            print(node.id, node.name,node.cash)
            return self.search(id)
        
        print("Invalid data for attriube !")
        return None
        
if __name__ == "__main__":
    # input("Press 1 to addData new cus:\nPress 2 to find cus info:")
    bst = BST()
    # bst.addData(24,"ko",2362623,"cagg@gmail.com","asgahh",0)
    # bst.addData(35,"b",2362622,"b@gmail.com","asgaha",1)
    bst.addData(29,"a",2362621,"a@gmail.com","asgahg",2)
    bst.addData(39,"c",2362624,"d@gmail.com","asgahl",3)
    # bst.addData(0,"d",2362625,"e@gmail.com","asgahh",0)
    # bst.addData(1,"e",2362626,"f@gmail.com","asgahh",0)
    # bst.addData(3,"f",2362627,"g@gmail.com","asgahh",0)
    # bst.addData(7,"d",2362625,"e@gmail.com","asgahh",0)
    # bst.addData(8,"e",2362626,"f@gmail.com","asgahh",0)
    # bst.addData(9,"f",2362627,"g@gmail.com","asgahh",0)
   
    print(bst.leght(bst.root))
    bst.showdatas()
    print("?¥¥¥¥")
    # print(bst.find_min().id,bst.find_min().name)
    # print(bst.find_max().id,bst.find_max().name)
    # print(bst.search(0).phone)
    # bst.delete(0)
    bst.delete(29)
    bst.showdatas()
    # bst.delete(35)
    # bst.delete(1)
    # # print("gg",node.id)

    # bst.showdatas()
    # print("?¥¥¥¥")
    # bst.update(9,"name","David")
    # bst.update(0,"name","David")

    # bst.update(2,"name",12)
    # bst.showdatas()
    # # bst.update(20,"phone",0)
    # # bst.showdatas()
    # print("search")
    # print(bst.searchBykey("phoe",2362623).id)
 





