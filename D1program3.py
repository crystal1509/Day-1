#Python Program to Calculate the Area of a Triangle, square, and rectangle, circle by taking user input


h=int(input("enter the height for the triangle:"))
b=int(input("enter the base for it:"))
t=1/2*b*h;
print("area of triangle is:",t);

s=int(input("enter the side for the square:"))
q=s*s;
print("area of sqaure:",q);

l=int(input("enter the length for the rectangle:"))
b=int(input("enter the width for the rectangle:"))
r=l*b;
print("area is:",r);

a=int(input("enter the radius for the circle:"))
c=3.14*a*a;
print("area of circle:",c);
