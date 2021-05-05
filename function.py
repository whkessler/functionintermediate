#update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)
students[0]['last_name']= 'Bryant'
print(students)
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)
z[0]['y']= 30
print(z)

# iterate through a list of dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for key in some_list:
        print(key)
iterateDictionary(students)
def iterateDictionary2(key_name, some_list):
    for key in some_list:
        print(key[key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#iterate through a dictionary with list value
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(some_dict):
    print (len(some_dict['locations']))
    for x in some_dict['locations']:
        print(x)
    print (len(some_dict['instructors']))
    for x in some_dict['instructors']:
        print(x)
printinfo(dojo)


