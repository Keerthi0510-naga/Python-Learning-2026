import sys
from collections import deque
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = deque()

    # Push character onto stack
    def pushCharacter(self, ch):
        self.stack.append(ch)

    # Enqueue character into queue
    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    # Pop character from stack
    def popCharacter(self):
        return self.stack.pop()

    # Dequeue character from queue
    def dequeueCharacter(self):
        return self.queue.popleft()
# read the string s