#Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
n=int(input())
sum=0

for i in range(n):
    char=input()
    sum+=ord(char)


print(f"This sum is equal: {sum}")