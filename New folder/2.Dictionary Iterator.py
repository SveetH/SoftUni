class dictionary_iter():
    def __init__(self, dic):
        self.dic = dic
        self.max_len = 0
        self.keys = [(k, v) for k, v in self.dic.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_len < len(self.dic.keys()):
            index = self.max_len
            self.max_len += 1
            return self.keys[index]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
