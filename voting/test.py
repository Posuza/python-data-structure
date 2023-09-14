from votinglib import Voting
db ={0: {'email': '12', 'name': '12', 'phone': '12', 'address': '12', 'password': '12'},
                         1: {'email': '12', 'name': '12', 'phone': '12', 'address': '12', 'password': '12'}}
student = {0: {"name": "James", "v_mark": 0, "voter": []},
                         1: {"name": "John", "v_mark": 0, "voter": []},
                         2: {"name": "Rooney", "v_mark": 0, "voter": []},
                         3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                         4: {"name": "Messi", "v_mark": 0, "voter": []}
                         }

maindb = {0:db,1:student}


def recording_all_data():
    with open("new.txt","w") as note:
        for element in maindb:
            note.write(str(maindb[element]))
            note.write("\n")  
    print("data is recoreded")


def loadAllData():
    try:
        with open("new.txt","r") as note:
          id = 0
          for line in note: 
                text = line.strip()
                result= eval(text)
                data = {id:result} 
                id += 1
                maindb.update(data) 
        db.update(maindb[0])
        student.update(maindb[1])
    except IOError:
        newFile()

def newFile():
    with open("new.txt","w") as note:
        print("newt file is creating")       

if __name__ == '__main__':
    
    # voting = Voting()
    # studentDb = voting.students
    # userDb = voting.db
    # db = userDb
    recording_all_data()

    maindb ={}
    student ={}
    db ={}
    loadAllData()
    print(maindb)
    print("db",db)
    print("student",student)

    # loading_all_data()
    # print(newdb)
    # print(newdb2)
    # voting.main_option()
    