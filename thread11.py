
'''
import threading
import time
def my_task():
	for i in range(5):
		print("in my task.....");
		time.sleep(1);
	
print("main thread/task is running");
time.sleep(1);

th1= threading.Thread(target=my_task);  #only thread created
th1.start();
for i in range(5):
		print("in main.....");
		time.sleep(1);							#start
print("main thread ends...")
'''
'''
import threading
import time
def my_task():
	print("child thread id",threading.currentThread().ident)
	print("child thread id",threading.currentThread().name)
	for i in range(5):
		print("in my task.....");
		time.sleep(1);
	
print("main thread/task is running");
print("main thread id",threading.currentThread().ident)
print("main thread id",threading.currentThread().name)
time.sleep(1);

th1= threading.Thread(target=my_task);  #only thread created
th1.start();
for i in range(5):
		print("in main.....");
		time.sleep(1);							#start
print("main thread ends...")
'''

import threading
import time
def my_task(i,j):
    print("mytask:{},{}".format(i,j))
    print("child thread id:",threading.currentThread().ident)
    print("child thread name:",threading.currentThread().name)
    for i in range(5):

            print("in my_thread....\n")
            time.sleep(1)
   
print("main thread is running...\n")
th1=threading.Thread(target=my_task,args=(10,20),name="CHILDTHREAD")
th1.start()
th1.join()
print("parent thread id:",threading.currentThread().ident)
print("parent thread name:",threading.currentThread().name)
for i in range(5):
           
            print("in main...")
            time.sleep(1)
           
print("main thread ends...")


