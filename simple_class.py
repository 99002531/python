
'''
class <classname>([base classes]):
	instance methods
	class methods.
'''
'''
class Employee():
	def display(self):
		self.i=10;
		print("Employee.display",self.i);
		self.i=20;
		print("Employee.display",self.i);
	
e1=Employee();	
e1.display();     #e1.display(e1)


class Employee():
	def set_value(self):
		self.i=10;
	def display(self):
		print("Employee.display",self.i
		
e1=Employee();	
e1.set_value();
e1.display(); 
e2=Employee();
e2.set_value();	
e2.display(); 
'''
'''
class Employee():
	def _init_self:
		print("employeee init")
	def display(self):
		print("Employee.display",self.i);
		
e1=employee();
e1.display();

'''

'''
class Employee():
	def _init_(self,i):  #constuctor
		print("employeee init")
	def display(self):
		print("Employee.display",self.i);
		
e1=employee(11);   #e1.init(e1,11)
e1.display();
'''




'''
class Employee():
	def _init_(self,i,j):  #constuctor
		print("employeee init")
		self.i=i;
		self.j=j;
	def display(self):
		print("Employee.display",self.i);
		
e1=employee(11,12);   #e1.init(e1,11,12)
e1.display();

'''

class Employee():
	def _init_(self,i,j):  #constuctor
		print("employeee init")
		self.__i=i;
		self.j=j;
	def display(self):
		print("Employee.display".format(self.i,self.j));
		
e1=Employee(11,12);   #e1.init(e1,11,12
print(e1.__dict__);
e1.i2=200;
print(e1.__dict__);
e1.display();
print(e1.i);