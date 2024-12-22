#this is my first python program
print("Hello World. i like kuku")
print("its really cool")

#variables- strings, boolean,float &integer
full_nam = "GG Wema"
print (f"hello {full_nam}")#fstring for outputting

age = 22
print(f"i am {age} years old")

gpa = 3.43
print(f" your gpa is {gpa}")

is_student = True
print(f"are you a student? {is_student}")

#Arithmetic- addition+=,subtracton-=,division/(returns a float)&multiplication*=,integer division//=, Remainder%=
friends = 2
friends //= 2
print(friends)

#Typecasting-converts from one data type to anotherstr(), int(), float(), bool()
#type()
print(type(is_student))
print(type(gpa))

gpa = int(gpa)
print(gpa)

#accepting user input -input()
name = input("enter your name: ")
#age = input(f"Enter your age: ")-THE AGE IS IN STRING AND REQUIRES TO BE CHANGED TO AN INTEGER
#ie age = int(input(Enter your age: "))
# age += 1
print (f"hi {name}")

#if statements