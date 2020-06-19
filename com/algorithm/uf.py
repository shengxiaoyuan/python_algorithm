class UF(object):
    def __init__(self,count:int):
        self._count=count
        self.size=[0]*count
        self.parent=[0]*count
        for i in range(len(self.parent)):
            self.parent[i]=i
    def find(self,x:int):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
    def union(self,p,q):
        rootp=self.find(p)
        rootq=self.find(q)
        if rootp == rootq:
            return
        #优化点(重量优化)
        if self.size[rootp]<=self.size[rootq]:
            self.parent[rootp]=rootq
            self.size[rootq]+=self.size[rootp]
        else:
            self.parent[rootq]=rootp
            self.size[rootp]+=self.size[rootq]
    def connected(self,p:int,q:int):
        rootp=self.find(p)
        rootq=self.find(q)
        if rootp == rootq:
            return True
        return False
if __name__ == '__main__':
    print( ord('b')-ord('a'))