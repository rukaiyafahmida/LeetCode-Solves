class MyStack:

    def __init__(self):
        self.stck = []
        

    def empty(self) -> bool:
        if self.stck:
            return False
        return True

    def push(self, x: int) -> None:
        self.stck.insert(0,x)

    def pop(self) -> int:
        return self.stck.pop(0)

    def top(self) -> int:
        return self.stck[0]        



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
