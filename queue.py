

class Node: # узел для реализации очереди
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue: # реализация очереди
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data): # добавление элемента в конец очереди
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return 'ok'

    def pop(self): # удаления в возврат элемента из начала очереди
        if self.head is None:
            return 'error'
        
        node = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        return node
                
    def front(self): # возврат элемента из начала очереди без удаления
        if self.head == None:
            return 'error'
        return self.head.data
    
    def length(self): # возврат длины очереди
        return self.size
    
    def clear(self): # удаляет полностью очередь
        self.head = self.tail = None
        self.size = 0
        return 'ok'
    
    def exit(self): # выход из программы
        return 'bye'

    
queue = Queue()
while True:
    command = input('Введите команду - ').strip().split()
    if not command:
        continue
    if command[0] == "push":
        if len(command) != 2:
            print("Неправильный ввод, чтобы добавить элемент в очередь, нужно написать команду и число.")
            continue
        n = int(command[1])
        print(queue.push(n))
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "size":
        print(queue.length())
    elif command[0] == "clear":
        print(queue.clear())
    elif command[0] == "exit":
        print(queue.exit())
        break
    else:
        print("Неправильная команда!")