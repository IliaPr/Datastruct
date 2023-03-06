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
        newnode = Node(data)
        if self.first is None:
            self.first = newnode
            self.last = newnode
        else:
            self.last.nextnode = newnode
            self.last = newnode
    def dequeue(self):
        '''Удаление элементов из очереди по принципу FIFO'''
        if self.first is None:
            return
        value = self.first.data
        self.first = self.first.nextnode
        return value

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
