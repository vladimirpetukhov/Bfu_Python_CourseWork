#Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:
n=int(input())

for i in range(n):
    for k in range(n):
        for l in range(n):
            char_one=chr(97+i)
            char_two=chr(97+k)
            char_tree=chr(97+l)

            print(f"{char_one}{char_two}{char_tree}")
