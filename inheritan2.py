class A():
	def __init__(self):
		print("self type in A:",type(self));
		self.i=10;
	def display(self):
		print("A.display",self.i);
		
class B(A):
	def __init__(self):
		super().__init__();     #__init__(self)
		print("B__init__");
	def display(self):
		print("B.display",self.i);

	
#b=B();
#b.display();   #concept MRO  #b.display(b)
#print(B.mro)


class C(B):
	def display(self):
		print("c.display",self.i);
c1=C();			#c1.__init__(c1);
c1.display();    #c1.display(c1)
