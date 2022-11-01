## Write a program to take an input from the user and print that input
a = input()
print(a, end="")


## Write a program to take an input of two numbers A, and B and print the difference A-B

A = int(input())
B = int(input())

Z = A - B

print(Z,end="")


## Take a string S and an integer A as an input from a user. Write a program to print string S, A number of times.

# Input
# S: A string
# A: An integer

S = input()
A = int(input())

for i in range(1,A+1):
	print(S)
