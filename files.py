#Open a file
myFile = open('myfile.txt', 'w')

#Get some info
print('Name: ', myFile.name)
print('Is Closed ', myFile.closed)
print('Opening Mode ', myFile.mode)


#write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

#Append to file 
myFile = open('myfile.txt', 'a')
myFile.write('I also like PHP')
myFile.close()

# Read from file 
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text + '\n')


#JSON is commonly used with data APIS. Here how we parse JSON into Python dictionary

import json 

#sample json
userJSON = '{"firstname": "Jhon", "last_name": "Doe", "age": 30}'

#Parse to dic

user = json.loads(userJSON)
print(user)
print(user['first_name'])

#Trasform dictionary into JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 19970}

carJSON = json.dumps(car)

print(carJSON)