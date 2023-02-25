class Node:
    #Объявление функции, которая будет инициализировать создание узлов
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        '''Добавление элемента'''
        self.newnode = Node(data)
        self.newnode.nextnode = self.top
        self.top = self.newnode

    def pop(self):
        '''удаление элемента по принципу LIFO'''
        if self.top == None:
            return None
        else:
            self.pop_node = self.top
            self.top = self.pop_node.nextnode
            self.pop_node.nextnode = None
            return self.pop_node.data
