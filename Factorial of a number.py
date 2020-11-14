#Write a program which can compute the factorial of a given numbers.
a = input()
n=int(a)
for i in range (1,n):
    n = n*i
print(n)
print(fact(5))