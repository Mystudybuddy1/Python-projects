class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.len += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"

        value = self.front.data
        self.front = self.front.next
        self.len -= 1

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def is_empty(self):
        return self.len == 0

    def size(self):
        return self.len

    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print()


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Queue:", end=" ")
q.print_queue()
print("Peek:", q.peek())
print("Dequeue:", q.dequeue())
print("Queue after dequeue:", end=" ")
q.print_queue()
print("Is Empty:", q.is_empty())



    
    
 


    


    
    
        
 
    
