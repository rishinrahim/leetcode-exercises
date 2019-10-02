

class unionfind:


    def __init__(self,l):
        self.l = l
        self.sz = [0]*len(l)



    def union(self,c1,c2):
        if not self.find(c1,c2):
            self.l[self.find_root(c1)] = self.find_root(c2)

    def find(self,c1,c2):
        if self.find_root(c1) == self.find_root(c2):
            return True
        return False

    def find_root(self,c):
        while c != self.l[c]:
            c = self.l[c]
        return c


def getList(n):
    l = []
    for i in range(n):
        l.append(i)
    return l

if __name__=="__main__":
    n = 10


    u1 = unionfind(getList(10))
    u2 = unionfind(getList(5))

    print("u1:",u1.l)

    u1.union(4,3)
    u1.union(3,8)
    u1.union(6,5)
    u1.union(9,4)

    print(u1.find(8,9))
    print(u1.find(5,4))



    print("Result",u1.l)


