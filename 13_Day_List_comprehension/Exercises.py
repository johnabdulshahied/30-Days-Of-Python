# 1 - Filter only negative and zero in the list using list comprehension:

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([num for num in numbers if num <= 0])

# 2 - Flatten the following list of lists of lists to a one dimensional list:

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([item for outer_list in list_of_lists for list in outer_list for item in list])

# 3 - Using list comprehension create the following list of tuples:

''' Output: 
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)] '''

print([(i,1,i**2,i**3,i**4,i**5) for i in range(11)])

# 4 - Flatten the following list to a new list:

''' output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']] '''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[country.upper(),country.upper()[0:3],city.upper()] for list in countries for country,city in list])

# 5 - Change the following list to a list of dictionaries:

''' output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}] '''

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([{'country':country,'city':city} for list in countries for country,city in list])

# 6 - Change the following list of lists to a list of concatenated strings:

''' output: ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates'] '''

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([first_name + ' ' + last_name for name in names for first_name,last_name in name])

# 7 - Write a lambda function which can solve a slope or y-intercept of linear functions:
slope = lambda x1,x2,y1,y2: ((y2-y1)/(x2-x1))
y_intercept = lambda m, x, y: y - m * x
