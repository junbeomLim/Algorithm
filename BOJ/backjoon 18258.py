class Queue(object):
    def __init__(self):
        self.queue = []
    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    def push(self, n):
        self.queue.append(n)
        pass
    def printQueue(self):
        print(self.queue)
    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    def size(self):
        return len(self.queue)
    def front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    def back(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
N = int(input())
q = Queue()
for i in range(N):
    s = input().split(' ')
    if s[0] == 'push':
        q.push(s[1])
        print(s[1])
    elif s[0] == 'pop':
        print(q.pop())
    elif s[0] == 'size':
        print(q.size())
    elif s[0] == 'empty':
        print(q.empty())
    elif s[0] == 'front':
        print(q.front())
    elif s[0] == 'back':
        print(q.back())
