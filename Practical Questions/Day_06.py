print("________________________________________________________________________________")
#Question 1
numbers ={1, 2, 3, 4, 5}
print(numbers)
print("________________________________________________________________________________")
#Question 2
numbers.add(6)
print(numbers)
print("________________________________________________________________________________")
#Question 3
numbers.update({7,8,9})
print(numbers)
print("________________________________________________________________________________")
#Question 4
numbers.remove(8)
print(numbers)
numbers.discard(7)
print(numbers)
print("________________________________________________________________________________")
#Question 5
fruits ={"apple","mango","starberry"}
fruits_1={"kiwi","melon"}
print(fruits.union(fruits_1))
print("________________________________________________________________________________")
#Question 6
print(fruits.intersection(fruits_1))
print("________________________________________________________________________________")
#Question 7
print(fruits.difference(fruits_1))
print("________________________________________________________________________________")
#Question 8
print(fruits.symmetric_difference(fruits_1))
print("________________________________________________________________________________")
#Question 9
nums = [1,2,3,4,5,5,6,6,7,7,8,]
print(nums)
print(set(nums))
print("________________________________________________________________________________")
#Question 10
alpha ={"a","b","c","d","e","f"}
print(alpha.pop())