#Python Program for compound interest


p=float(input("principle:"))
r=float(input("rate:"))
t=float(input("time:"))
amt=p*(pow((1+r/100),t))
i=amt-p       
print("total amount:",i)
