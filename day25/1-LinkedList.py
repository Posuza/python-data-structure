class Node:
    # data structure
    def __init__(self, data, info: str):
        self.data = data
        self.ncc = info  # user input
        self.next = None
class Linked:

    def __init__(self):
        self.head = None
if __name__ == "__main__":
    linkedList = Linked()
    linkedList.head= Node(10,"first")

    second = Node(20,"second")
    third = Node(30,"third")

    linkedList.head.next = second
    second.next = third

    # print(linkedList.head.data)
    # print(linkedList.head.ncc)
    # print(linkedList.head.next.data)
    # print(linkedList.head.next.ncc)
    # print(linkedList.head.next.next.data)
    # print(linkedList.head.next.next.ncc)

    while linkedList.head is not None:
        print(linkedList.head.data)
        print(linkedList.head.ncc)
        linkedList.head = linkedList.head.next


