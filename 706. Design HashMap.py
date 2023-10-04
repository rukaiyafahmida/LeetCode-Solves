class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            return self.dic[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.dic.keys():
            del self.dic[key]
