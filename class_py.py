class Person:
	
	def __init__(self,age,name):
		self.age=age
		self.name=name
	
	def display(self):
		print("Person Age = ", self.name, self.age)

def main():
    P1=Person(18,"Kundan")
    P2=Person(22,"Lucky")
    P1.display()
    P2.display()

main()

'''class A:
	def dis(self):
		print ("\n\n\t Im from A")
		
class B:
	def dis(self):
		print("\n\n\t I am from B")
		
class C:
	def dis(self):
		print("\n\n\t I am from C")
		
class D(A,B,C):
	pass

kundan=D()
print(kundan.dis())'''
