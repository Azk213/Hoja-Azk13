import requests
print("________________________________________________________________________________")
#Question 1
print("What is an API in simpler words?")
print("An API is the link of communication between a client and a server")
print("________________________________________________________________________________")
#Question 2
print("Explain the diffrence between GET and POST resquests.")
print("A POST request, updates information while a GET request grabs information from the server")
print("________________________________________________________________________________")
#Question 3
print("What library do we commonly use to call APIs in Python?")
print("requests library is commonly used ")
print("________________________________________________________________________________")
#Question 4
print("What does reponse.json do ?")
print("response.json converts responses into dictionaryies")
print("________________________________________________________________________________")
#Question 5
response = requests.get("https://api.github.com")
date = response.json()
print(date)
print("________________________________________________________________________________")
#Question 6
print("What is JSON? Why do APIs use it?")
print("JSON is a data format ,APIs commonly use it because it is simple")
print("________________________________________________________________________________")
#Question 7
print("What is an API key and why is it needed?")
print("An API key is a key like a password  to access a server with a python code it allows for authentication ")
print("________________________________________________________________________________")
#Question 8



print("________________________________________________________________________________")
#Question 9
print("How does try-except help when calling APIs?")
print("Try expect help to deal with API keys expiring or not functioning properly")
print("________________________________________________________________________________")
#Question 10
print("What happens when an API returns a 404 response? How will your code handle it?")
print("A 404 is an error caused by a API key issue it can be dealt with with the usage of try-expect.")