class bb:
    def __init__(self,name,ID,salary):
        self.__name = name
        self.ID = ID
        self.salary = salary
    def gn(self):
        print(self.__name)
    def st(self,newname):
        self.__name = newname
        print('Name Updated Successfully')



class bl(bb):
    pass

cs1 = bb('Ryan' , 200,5000)
cs2 = bb('Atiya', 300,4000)

cs3 = bl('Zaheen', 400,5000)



#print(cs1.gn())

cs1.st('Rahul')
cs1.gn()











