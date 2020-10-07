'''

obj serilization
reg expression
pip
'''

import pickle;   #obj serilization

'''
dumps -> obj to binary    serial
loads  -> bin to obj      deserial
dump -> obj to bin but save as file
load -> load bin data from file and convert back to obj
'''
'''
L1= list(range(100));

print(L1); 

L1_b=pickle.dumps(L1);

print(L1_b);

L2=pickle.loads(L1_b);
print(L2);
'''

class Test():
	def __init__(self):
		self.i =100;
		self.f =111.23;
		self.b =True;
		self.s ="printndk";
	def display(self):
		print("{],{},{},{}".format(self.i,self.f,self.b,self.s));
'''		
t1=Test();
t1_b= pickle.dumps(t1);
t2=pickle.loads(t1_b);


t1=Test();
file=open("MyTest.dat","wb");
pickle.dump(t1,file);

'''
t1=Test();
file=open("MyTest.dat","rb");
pickle.load(t1);
file.close();