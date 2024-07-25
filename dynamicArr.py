import ctypes

class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def __append__(self,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        #append
        self.A[self.n]=item
        self.n=self.n+1
    def __resize(self,new_capacity):
        #create an array with new size
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i]=self.A[i]
        #reassign A
        self.A=B
    def __str__(self):
        result=""
        for i in range(self.n):
            result=result+str(self.A[i])+","
        return result
    def __getitem__(self,index):
        if 0<= index <self.n:
            return self.A[index]
        else:
            return 'IndexError- Index out of bound'
    def pop(self):
        if self.n==0:
            return "empty list"
        print(self.A[self.n-1])
        self.n=self.n-1

    def clear(self):
        self.n=0
        self.size=1
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                print(i) 
        print("value error not in the list")
    def insert(self,pos,item):
        #resize
        if self.n==self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        self.A[pos]=item
        self.n=self.n+1
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n=self.n-1
            



        

L=MeraList()
# print(len(L))
L.__append__(90)
L.__append__("yellow")
L.__append__(34)
# L.find("hello")
# L.find(90)
# L.insert(0,"goodmorning")
del L[1]
print(L)


# L.pop()
# print(L[0])
# print(L)



