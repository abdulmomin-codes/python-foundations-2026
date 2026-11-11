#Write a compound interest calculator ($A = P(1 + \frac{r}{n})^{nt}$) 
#prompting for Principal, Rate, Time, and Compound Frequency.
principal = float(input("enter principal:"))
rate = float(input("enter rate:"))
time = float(input("enter time:"))
compound_frequency = float(input("enter compound frequency:"))

P = principal
r = rate
t = time
n = compound_frequency

A = P * (1 + r / n) ** (n * t)
print(f"A is : {A}")