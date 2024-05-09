class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source.name} to {target.name}")
        target.push(source.pop())
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source.name} to {target.name}")
    target.push(source.pop())
    tower_of_hanoi(n-1, auxiliary, target, source)


# Function to solve Tower of Hanoi using stacks
def tower_of_hanoi_stack(n):
    source = Stack()
    source.name = "A"
    auxiliary = Stack()
    auxiliary.name = "B"
    target = Stack()
    target.name = "C"

    # Push disks onto source stack
    for i in range(n, 0, -1):
        source.push(i)

    tower_of_hanoi(n, source, target, auxiliary)


# Test the tower_of_hanoi_stack function
num_disks = 3
print(f"Solving Tower of Hanoi problem with {num_disks} disks:")
tower_of_hanoi_stack(num_disks)
