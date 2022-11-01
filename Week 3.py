## There is list L containing some numbers. Write a program to create a new list which contains the numbers which are either
## divisible by 5 or 7 or both. Print that new list in ascending order.

L = [int(i) for i in input().split()]
ans = [ z for z in L if z%5==0 or z%7==0]
print(sorted(ans),end="")

## Write a function rev which takes a list L and integer n and print the first n largest numbers of the list.

## Input is managed for you, please write the required function only.
def rev(L,n):
  print(sorted(L)[::-1][:n],end="")
  
## Write a program to count and print the number of odd numbers in a list L

L = [int(i) for i in input().split()]
odd=[a for a in L if a%2!=0]
print(len(odd),end="")
