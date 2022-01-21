#Assignment 2
#                    QUESTION-1
print("\nQUESTION-1")
                                         #part a

x="Python is a case sensitive language"  #x=input string
a=len(x)                                #a=length of string a
print(f"a. Length of '{x}' is {a}")
                                        #part b

reverse_string=x[::-1]
print(f"b. '{reverse_string}' is reversed string")
#part c
new_string=x[10:26]
print(f"c. New string is '{new_string}'")
#part d
new_string="object oriented"
print(f"d. Replaced string is '{new_string}'")

#part e

_index=x.find("a")
print(f"e. Index of substring 'a' in given input string is: {_index}")
#part f
replace_white_space=x.replace(" ","")
print(f"f. String after removing white spaces is '{replace_white_space}'")

#                  QUESTION-2
print("\nQuestion-2")

#Taking input from the user
name=str(input("Enter your name:"))
sid=int(input("Enter your SID:"))
dname=str(input("Enter your department name:"))
cgpa=float(input("Enter your CGPA:"))
#string formatting
statement="Hey, %s Here! My SID is %s I am from %s department " \
          "and my CGPA is %s"%(name,sid,dname,cgpa)
print(statement)

#                 QUESTION-3
print("\nQuestion-3")

a=56
print(f"a={a}")
b=10
print(f"b={b}")
#part a

_a=a&b
print(f"A. a&b is {_a}")
#part b

_b=a|b
print(f"B. a|b is {_b}")
#part c

_c=a^b
print(f"C. a^b is {_c}")
#part d

_d1=a<<2
print(f"D1. Left shift a with 2 bits  is {_d1}")
_d2=b<<2
print(f"D2. Left shift b with 2 bits is {_d2}")
#part e

_e1=a>>2
print(f"E1. Right shift a with 2 bits is {_e1}")
_e2=b>>4
print(f"E2. Left shift b with 4 bits is {_e2}")



#                     QUESTION-4
print("\nQuestion-4")


#Taking input()
i1=float(input("Enter first number:"))
i2=float(input("Enter second number:"))
i3=float(input("Enter third number:"))
#Logic to get greatest of three number
#logic when all are equal
if i1==i2==i3:
    print("\All numbers entered are equal.")
#Logic when two number are equal
elif i1==i2 and i2>i3:
    print(f"{i1} is greatest of all numbers entered.")
elif i2==i3 and i3>i1:
    print(f"{i2} is greatest of all numbers entered.")
elif i3==i1 and i3>i2:
    print(f"{i3} is greatest of all numbers entered.")
#Logic when all nubers are different
elif i1>i2 and i2>i3:#logic when i1 is greatest
    print(f"{i1} is greatest of all numbers entered.")
elif i2>i3 and i2>i1:#logic when i2 is greatest
    print(f"{i2} is greatest of all numbers entered.")
elif i3>i2 and i3>i1:#logic when i3 is greatest
    print(f"{i3} is the greatest of all numbers entered.")




#               QUESTION-5
print("\nQuestion-5")

#Taking string input from the user
a=str(input("Enter a Statement:"))
#Applying in to check if name is present in string or not
b="name" in a
#printing the result after checking
if b==True:
    print(f"YES 'name' word is present in '{a}'")
else:
    print(f"NO 'name' word is not present in '{a}' ")


#                QUESTION-6
print("\nQuestion-6")

#taking input
s1=int(input("Enter length of 1st side of triangle:"))
s2=int(input("Enter length of 2nd side of triangle:"))
s3=int(input("Enter length of 3rd side of triangle:"))
#applying condition to form a triangle
if (s1+s2)<s3 or (s2+s3)<s1 or (s1+s3)<s2:
    print(f"NO given sides {s1},{s2},{s3} can't form a triangle")
else:
    print(f"YES given sides {s1},{s2},{s3} can form a triangle")



























