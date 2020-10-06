#magic methods
'''
class MyNumber():
	def __init__(self,n):
		self.n=n;
	def display(self):
		print(self.n);
	def _add__(self,other):
		print("calling add");
		temp=MyNumber(0);
		temp.n= self.n + other.n;
		return temp;
		
n1=MyNumber(10);
n2=MyNumber(20);
n1.display();
n3= n1 + n2;  #n1 add(self,n2)     #n3 add(self,n1,n2)
n3.display();
'''

#magic methods

class MyNumber():
	def __init__(self,n):
		self.n=n;
	def display(self):
		print(self.n);
	def _lt__(self,other):
		return self.n < other.n
		
	def __str__(self):
		return "N" +str(self.n);
	def __del__(self):
		print("deleting obj")
	
n1=MyNumber(10);
n2=n1;
del(n1);
del(n2);
'''
n2=MyNumber(20);
n1.display();
result= n1 < n2;  #n1 add(self,n2)     #n3 add(self,n1,n2)
n3.display();

i=10;
j=20;
print(dir());
del(i);   #only varibles
print(dir());
'''