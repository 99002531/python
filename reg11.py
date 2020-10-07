#regular exp
import re
'''
print(re.match("the","the man"));  #only first 

print(re.search("the","i am the man"));   #everywhere

'''

'''
.			matches any one charcter in the string

?			preceeding charcter can repeat 0 or 1 only		

+			preceeding charcter can repeat 1 or more times	

*			preceeding charcter can repeat 0 or more times	

[]			matches any single character in the group

[^]			opp to[]

()      	combination of character 

|			either or condition

^			start of string

$			end of string

'''
'''
print(re.match(".....","hello"));

print(re.match("[aeiou]+","aeiouHell0")); 

print(re.match("[a-z]+","aeiouHell01234"));  #hello, heello
'''

#print(re.search("[0-37a-z]+","aeiouhell01234"));  #0-7

#print(re.search("[^a-z]+","aeiouHell01234")); 

#print(re.search("[a-z]{3,5}","aeiouHell01234"));   #min 3 max5 

#print(re.search("(ab)?c","ababc")); #abc  c

#print(re.match("[a-z]+ | [0-9]+","abcd1234"));

#print(re.match("^He","Hello"));


#ps number P1234567
#print(re.match("P[0-9]{7}$","P1234567"));

#srini@gmail.com
#print(re.match("[a-z0-9_]+@[a-z]+\.[a-z]{2,3}","srini123_@gmail.com"));

'''
with open("input.txt","r") as file:
	for line in file.readlines():
		if(re.search("name",line)
		print(line);
		
'''


'''
\d    decimal
\D   mon decimal
\s   anyone whitespace character 
\S   non whitespace character
\w   alpha numeric  includes underscore
\W   non alpha numeric
\b

'''
#print(re.search("\D+","1234abcd565"));    #any decimal

#print(re.search(r'\bthe\b',"i am the the man"));   #r is used since \b backslash cinvert into raw sting


#print(re.findall('\d+',"a12 34b cd 34 55 ab"))   #repeated search 

#print(re.findall('[a-z]+',"a12 34b cd 34 55 ab"))



















