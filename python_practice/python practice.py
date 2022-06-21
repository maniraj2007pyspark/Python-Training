#Length of string
# x = "maniraj"
# print("Length of string:",len(x))

#Count characters in string
# x= "maniraj"
# print("Count characters in string",x.count("a"))

#String slicing
# x="maniraj"
# print("String slicing:",x[2])

#Replace first occurance character
# x="hello welcome to vn2 solution"
# print(x.replace("hello","hi"))

#Swapping chars in string
# def swap(string):
#     return string[-1:]+string[1:-1] + string[:1]
# str = input("Enter the String:")
# print(swap(str))

#Append chars to string at end
# a= "mani"
# b = "raj"
# c = (a+b)
# print("Append chars to string at end:",c)

#Substring replacement
# a = "united states"
# print(a.replace("states","kingdom"))
# print(a.replace("u","U"))

#Length of longest string in python
# a = "i worked with MPL Tecnologies,I have total 4 years Experiance"
# print(max(a))

#nth index character from string
# a = input("Enter any String:")
# print(a[2])

#First last chars swapping
# a = input("enter the string:")
# print(a[-1:]+a[1:-1]+a[:1])

# #Remove odd index values
# str1 = input("Please Enter your Own String : ")

# str2 = ''
# i = 0

# while(i < len(str1)):
#     if(i % 2 == 0):
#         str2 = str2 + str1[i]
#     i = i + 1
        
# print("Original String :  ", str1)
# print("Final String :     ", str2)
 
#Count words in a string

# x = "i am working in mpl technologies and i have four years experiance"
# str = x.split()
# print("Count words in a string:",len(str))

# a = input("enter a string using upper or lower:")
# print(a.isupper())
# print(a.islower())
# print(a.upper())
# print(a.lower())








'''
string = "maniraj"
x = ""
for char in string:
    if char not in x:
        x = x+char
print(x)
'''
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i +=1

# x= "hello welcome tok vn2"
# print(x.split("o"))
 
# Create a string made of the first, middle and last character       
str= "saravana"
res=str[0]
l = len(str)
mi = int(l//2)
res=res+str[mi]
res=res+str[l-1]
print("first,middle,last char in string:",res)



