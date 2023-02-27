class Node:
    #Объявление функции, которая будет инициализировать создание узлов
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode

class Queue:

    def __init__(self, first = None, last = None):
        '''Инициализация переменных хранения данных очереди'''
        self.first = first
        self.last = last

    def enqueue(self, data):
        '''Создание очереди'''
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.nextnode = new_node
            self.last = new_node

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.first.data)
    print(queue.first.nextnode.data)
    print(queue.last.data)
    print(queue.last.nextnode)
    print(queue.last.nextnode.data)
