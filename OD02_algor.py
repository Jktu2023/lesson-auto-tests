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

class Graph: # граф
    def __init__(self): # конструктор графа
        self.graph = {} # словарь графа

    def add_vertex(self, vertex): # добавление вершины
        if vertex not in self.graph:
            self.graph[vertex] = [] #

    def add_edge(self, vertex1, vertex2): # добавление ребра
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def get_neighbors(self, vertex): #
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

    def display(self):
        return self.graph

graph1 = Graph()
graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')
graph1.add_edge('A', 'B')
graph1.add_edge('B', 'C')
graph1.add_edge('C', 'A')

print()
print('Состояние графа', graph1.display())
print('Соседи вершины A', graph1.get_neighbors('A'))
print('Соседи вершины B', graph1.get_neighbors('B'))
print('Соседи вершины C', graph1.get_neighbors('C'))


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left:
                return self.left.search(value)
            return False
        if value > self.value:
            if self.right:
                return self.right.search(value)
            return False

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self): # вывод дерева
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f'{self.value}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f'{self.value}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f'{self.value}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f'{self.value}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

tree1 = Tree(5)
tree1.insert(3)
tree1.insert(7)
tree1.insert(2)
tree1.insert(4)
tree1.insert(6)
tree1.insert(8)

print()
print('Состояние дерева', tree1.display())
print('Поиск значения 4', tree1.search(4))
print('Поиск значения 9', tree1.search(9))
print('Состояние дерева', tree1.display())

