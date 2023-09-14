db = {0:{"name":"koko","email":"gogo@gmail.com"},
    1:{"name":"koko","email":"gogo@gmail.com"},
    2:{"name":"koko","email":"gogo@gmail.com"}
    }
d={}
def recordAllData():
    
    # with open("newtext.txt","w") as note:
    #     for element in db:
    #         note.write(str(db[element]))
    #         note.write("\n")
    # write()
    try:
        with open("newtext.txt") as note:      
            for line in note:
                id = len(d)
                text = line.strip()
                result= eval(text)
                data = {id:result} 
                d.update(data)
                print(d)
    except IOError:
        write()
        recordAllData()
        print("New file is created")        
    for i in d:
        print(d[i])
        print(d[i]["u_email"])  
        print("the data is entering \n") 

def write():
    with open("newtext.txt","w") as note:
        print("file is creating")
    

def loadAllData():
    with open("newtext.txt","w") as note:
        for element in db:
            note.write(element)
            note.write('\n')

if __name__ == '__main__':
    recordAllData()