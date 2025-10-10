# попробуй реализовать стек с помощью списка, а также очередь с помощью списка.
# Можно попробовать реализовать дерево и граф.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    def display(self):
        """Возвращает копию стека (от дна к вершине) для просмотра."""
        return self.stack.copy() # копия списка

    def serch(self, item):
        return item in self.stack  # поиск элемента в стеке

    def size(self):
        return len(self.stack)


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

print('Состояние стека', stack1.display())
print('Длина стека', stack1.size())

print('Удаляем последний элемент из стека', stack1.pop())
print('Сейчас последний элемент стека', stack1.peek())
print('Стек пустой?', stack1.is_empty())
print('Состояние стека', stack1.display())
print('Есть ли в секе элемент', stack1.serch(2))


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        """Возвращает копию очереди (от дна к вершине) для просмотра."""
        return self.queue.copy()

    def size(self):
        return len(self.queue)

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)

print()
print('Состояние очереди', queue1.display())
print('Длина очереди', queue1.size())

print('Удаляем первый элемент из очереди', queue1.dequeue())
print('Сейчас первый элемент очереди', queue1.peek())
print('Очередь пустая?', queue1.is_empty())
print('Состояние очереди', queue1.display())

