import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# BT01. Tháp Hà Nội
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

n = int(input('Nhap so dia: '))
TowerOfHanoi(n, 'A', 'C', 'B')

# BT02. Ước số chung lớn nhất

def uscln(a, b):
    if a < 0 or b < 0:
        return None
    if b == 0:
        return a
    return uscln(b, a % b)

a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))

# BT03. Tính giai thừa của 1 số

def tinhgiaithua(n):
    giai_thua = 1;
    if n < 0:
        return ('Không tồn tại')
    elif n == 0 or n == 1:
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua


n = int(input("Nhập số nguyên dương n = "))
print("Giai thừa của", n, "là", tinhgiaithua(n))


# BT06. Cài đặt danh sách liên kết đơn

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()

# BT07. Cài đặt danh sách liên kết kép

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

        def insert_in_emptylist(self, data):
            if self.start_node is None:
                new_node = Node(data)
                self.start_node = new_node
            else:
                print("list is not empty")

# BT08. Cài đặt ngăn xếp - stack

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Sử dụng phương pháp nối thêm danh sách để thêm phần tử
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Sử dụng chế độ xem trước để nhìn vào đầu ngăn xếp

    def peek(self):
	    return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())

# BT09. Cài đặt hàng đợi - queue

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Sử dụng phương pháp nối thêm danh sách để thêm phần tử
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Sử dụng chế độ xem trước để nhìn vào đầu ngăn xếp

    def peek(self):
	    return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())

# BT10. Cài đặt cây - duyệt cây theo thứ tự trước

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root)

# BT11. Cài đặt cây - duyệt cây theo thứ tự sau

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PreorderTraversal(root))



# BT12. Cài đặt đồ thị vô hướng
df = pd.DataFrame({'from': ['D', 'A', 'B', 'C', 'A'], 'to': ['A', 'D', 'A', 'E', 'C']})

G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())

nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("Directed")
plt.show()

# BT13. Cài đặt đồ thị có hướng
df = pd.DataFrame({'from': ['D', 'A', 'B', 'C', 'A'], 'to': ['A', 'D', 'A', 'E', 'C']})

G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
plt.title("UN-Directed")
plt.show()

# BT14.  Cài đặt thuật toán sắp xếp chọn
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)

# BT15.  Cài đặt thuật toán sắp xếp chèn
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
        # Compare the current element with next one

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = nxt_element


list = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(list)
print(list)


# BT16.  Cài đặt thuật toán sắp xếp nổi bọt
def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)
