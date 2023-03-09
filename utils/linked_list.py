class Node:
    #Объявление функции, которая будет инициализировать создание узлов
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode

class LinkedList:
    def __init__(self, first = None, last = None):
        '''Инициализация переменных хранения данных очереди'''
        self.first = first
        self.last = last

    def insert_beginning(self, data):
        '''Добавление данных в начало списка'''
        newnode = Node(data)
        if self.first == None:
            self.first = newnode
            self.last = newnode
        else:
            newnode.nextnode = self.first
            self.first = newnode

    def insert_at_end(self, data):
        '''Добавление данных в конец списка'''
        newnode = Node(data)
        if self.last == None:
            self.first = newnode
            self.last = newnode
        else:
            self.last.nextnode = newnode
            self.last = newnode

    def print_ll(self):
        '''Функция вывода данных'''
        ll_string = ''
        node = self.first
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.nextnode
        ll_string += ' None'
        print(ll_string)

