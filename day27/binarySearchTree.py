class Node:
    def __init__(self,myData):
        self.data = myData
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
 
#insertion
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            self._addChild(data,self.root)

    def _addChild(self,new_data,node):
        if node is None:
            new_node :Node =Node(new_data)
            return new_node
        if node.data == new_data:
            return node
        if new_data < node.data:
            node.left =self._addChild(new_data , node.left)
        else:
            node.right =self._addChild(new_data,node.right)
        return node
    
#Print
    def show(self):
        self._show_all_data(self.root,0,"")

    def _show_all_data(self,node,count,key):
        l = count
        R  = count
    #Preorder
    # if node:
    #     show_all_data(node.left,l+1,"l")
    #     show_all_data(node.right,R+1,"R")
    #     print(l*"-",R*"-",node.data)

    #Postorder
        # if node:
        #     print(l*"-",R*"-",node.data)
        #     self._show_all_data(node.left,l+1,"l")
        #     self._show_all_data(node.right,R+1,"R")

    #Inorder

        if node:
            self._show_all_data(node.left,l+1,"l")
            print(l*"-",R*"-",node.data)
            self._show_all_data(node.right,R+1,"R")

#find miximum value
    def find_max(self):
        if self.root:
            return self._find_max(self.root)
        print("Empty tree!")
        return -1
    
    def _find_max(self,node):
            if node.right is None:
                return node.data
            return self._find_max(node.right)
            
#find minimum value
    def find_min(self):
        if self.root:
            return self._find_min(self.root)
        print("Empty tree!")
        return -1
    
    def _find_min(self,node):
            if node.left is None:
                return node.data
            return self._find_min(node.left)

#search value
    def search(self,value:int):
        if self.root:
            if self._search(self.root,value) is not None:
                return self._search(self.root,value)   
        print("invalid search!")
        return None
    
    def _search(self,node,value):
        if node:
            if node.data == value:
                return node
            else:
                return self._search(node.left,value) or self._search(node.right,value)  


#deleting
    def delete(self,value):
        if self.root:

            return   self._delete1(self.root,value)

        print("No value to delet in database")
        return None

    def _delete(self,node, val):

        if val < node.data:
            if node.left:
                node.left = self._delete(node.left,val)
        elif val > node.data:
            if node.right:
                node.right = self._delete(node.right,val)
        else:
            if node.left is None and node.right is None:
                return None
            
            elif node.left is None:
                self.root = node.right
                print("node right")
                return self.root
            
            elif node.right is None:
                self.root = node.left
                print("node left")
                return self.root

            min_val = self._find_min(node.right)
            node.data = min_val
            node.right = None

            # max_val = self._find_max(node.left) #return min node
            # node.data = max_val
            # node.left = self._delete(node.left,min_val)

        return node

    def leght(self,node):
        if node is None:
            return 0
        l=self.leght(node.left)
        r=self.leght(node.right)
        return 1+l+r
    
    def _delete1(self,node,key):
        if not node: return None

        if node.data == key:
            print(key,"has deleted!")
            if not node.left and not node.right:
                print("delete leave node")
                node = None
                return node
            if not node.left and node.right: 
                if self.leght(node) ==2:
                    self.root = node.right
                    print("rheig")
                    return self.root
                else:
                    print("r")
                    node = node.right
                    return node 
            if not node.right and node.left:
                if self.leght(node) ==2:
                    self.root = node.left
                    print("lhe")
                    return self.root
                else:
                    print("l")
                    node = node.left
                    return node
            #if both exit
            pointer = node.right
            while pointer.left : pointer = pointer.left #return most left node
            # print(node,"node")
            # print(node.right.data,"node right")
            node.data = pointer.data      #replace valaue
            # print(node,"node")
            # print(node.right.data,"node right")
                #replace all most left node sub tree to root.rigth 
            node.right = self._delete1(pointer.right,key)
            

        elif node.data > key:
            node.left = self._delete1(node.left,key)
        else:
            node.right = self._delete1(node.right,key)

        return node

if __name__ == "__main__":

    # input("Press 1 to insert new cus:\nPress 2 to find cus info:")
    bst = BST()
    # bst.insert(4)

    bst.insert(4)
    # bst.insert(6)
    bst.insert(5)
    # bst.insert(20)
    # bst.insert(30)
    # # bst.insert(50)
    # bst.insert(6)
    # bst.insert(17)
    # bst.insert(16)
    # # bst.insert(4)
    # bst.insert(2)
    # bst.insert(1)
    # bst.insert(3) 
    # bst.insert(5)  
    # bst.insert(20)
    # bst.insert(5)

    bst.show()
    # print(bst.find_min())
    # print(bst.search(0))
    bst.delete(4)
    # bst.delete(5)
    # bst.delete(14)
    # bst.delete(4)
    # # print("gg",node.data)

    print("!!!")
    bst.show()
    # print(bst.search(20).data)





