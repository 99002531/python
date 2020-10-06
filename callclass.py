#callable class

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
		print("deleting obj",self.n);
	def __call__(self):
		print("mynumber call");
def test():
	print("test");
	
i=10;
print(callable(i));
print(callable(test));

n1=MyNumber(10);

n1();  #n1.__call(n1)
print(callable(n1));