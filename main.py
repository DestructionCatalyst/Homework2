

class CustomList(list):
    def __add__(self, other):
        res = CustomList()
        i = 0
        while i < len(self) and i < len(other):
            res.append(self[i] + other[i])
            i += 1
        while i < len(self):
            res.append(self[i])
            i += 1
        while i < len(other):
            res.append(other[i])
            i += 1
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-CustomList(other))
    
    def __rsub__(self, other):
        return (-self).__add__(other)

    def __neg__(self):
        return CustomList(map(lambda a: -a, self))

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

