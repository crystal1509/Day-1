#WAP that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


name=input("enter your name:")
age=int(input("enter your age:"))
year=int(input("enter the current year:"))
a=age;
b=100-a;
sol=year+b;
print("after",b,"years you will turn 100 in ",sol,"year");
