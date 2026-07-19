print("________________________________________________________________________________")
#Question 1
num = [x for x in range(1,11)]
print(num)
print("________________________________________________________________________________")
#Question 2
num_even = [x for x in range(0,21,2)]
print(num_even)
print("________________________________________________________________________________")
#Question 3
s = "programming"
unique = {ch for ch in s}
print(unique)
print("________________________________________________________________________________")
#Question 4
cube = {x:x**3 for x in range(1,6)}
print(cube)
print("________________________________________________________________________________")
#Question 5
fruit = ["apple","banana","cherry"]
print(fruit)
fruit_len = [len(x) for x in fruit]
print(fruit_len)
print("________________________________________________________________________________")
#Question 6
set = [1,2,3,4,5,6]
print(set)
set_square = [x for x in set if x**2 % 2 == 0]
print(set_square)
print("________________________________________________________________________________")
#Question 7
hello = "hello"
print(hello)
hello_ascii = {ch:ord(ch) for ch in hello} #asked ChatGPT for ord function
print(hello_ascii)
print("________________________________________________________________________________")
#Question 8
factors_2_3 = [x for x in range(1,31) if x % 2 and x % 2 == 0 ]
print(factors_2_3)
print("________________________________________________________________________________")
#Question 9
nested = [[1,2],[3,4],[5,6]]
print(nested)
unnested = [num for list in nested for num in list]
print(unnested)
print("________________________________________________________________________________")
#Question 10
tuple_num = (1,2,3,4,5)
print(tuple_num)
gen = tuple(x**2 for x in tuple_num)
print(gen)