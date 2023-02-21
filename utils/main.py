class Node:

    #Объявление функции, которая будет инициализировать создание узлов

    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Добавление элемента """
        newnode = Node(data)
        newnode.nextnode = self.top
        self.top = newnode


if __name__ == '__main__':
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2.nextnode)


    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)
    print(stack.top.nextnode.data)
    print(stack.top.nextnode.nextnode.data)
    print(stack.top.nextnode.nextnode.nextnode)
    print(stack.top.nextnode.nextnode.nextnode.data)




