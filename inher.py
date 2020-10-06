'''
class A():
	def display(self):
		print("A.display");
		
class B(A):
	pass;

	
b=B();
b.display();
'''
'''
class Test():
	def __init__(self):   #instance methods
		self.i=10;			#instance variables	
	def display(self):
		print("test",self.i);
t1=Test();
t1.display();
'''
'''
class Test():
	count=10;
	def __init__(self):   #instance methods
		self.i=10;			#instance variables	
	def display(self):
		print("test",self.i);
	
	def mod_count(self):
		self.count=self.count +100;
t1=Test();
print(Test.count);
print(t1.count);
print(t1.__dict__);
t1.mod_count();
print(t1.__dict__);
print(t1.count);
print(Test.count);
'''

class Test():
	count=10;
	def __init__(cls):   #instance methods
		cls.i=10;			#instance variables	
	def display(cls):
		print("test",cls.i);
	@classmethod
	def mod_count(cls):
		cls.count=cls.count +100;
		
t1=Test();
print(t1.__dict__);
Test.mod_count();
print(t1.__dict__);
print(Test.count)
