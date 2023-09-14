class loop():
    def __init__(self):
        self.new = [[3,"mybook"],[1,"yjor"],[0,"gsd"],[8,"sdf"],[1,"sdg"]]
        self.mylist = [1,1,5,9,2,30,16,823,4]

    def main(self):
        her=[]
        localist = self.new
        for i in range(len(localist)):
            # her.append(localist[i])
            print(localist[i])
            for j in range(i+1,len(localist)):
                if localist[i][0] > localist[j][0]:
                    localist[i],localist[j] = localist[j],localist[i]

        return her
    
    

if __name__ == '__main__':
    tcpserver = loop()
    result=  tcpserver.main()
    print(result)