# This is ob program for servertcp and client actions
class Ob:
    def __init__(self):
        print("Starting OB Program!")
        # self.data_list = []

    def get_received(self,data):
        print("Received",data)
        # self.data_list.append(data)
        return data

    # def datas(self):
    #         while True:
    #             if len(self.data_list) > 0:
    #                 print(self.data_list)
    #                 self.data_list = []
    #             print

    def send_data(self,data):
        print("Sent:",data)
        return data

if __name__ == "__main__":
    ob = Ob()
    ob.datas()
