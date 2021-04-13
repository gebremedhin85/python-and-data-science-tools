# Home work for week1

# 1. Print name and age
name = 'Gebremedhin'
age = 34
print(f'My Name: {name}')
print(f'My Age: {age}')

# 2.  list of your 5 favorite movies
favorite_movies = ['Spider man', 'Iron man', 'Salt', 'Titanic', 'Prison break']

# 3. Displaying the first and last colors from the following list
color_list = ["Red", "Green", "White", "Black"]
first_and_last_color = []
selected_color_indexes = [0, (len(color_list) - 1)]
for index in selected_color_indexes:
    first_and_last_color.append(color_list[index])
# print(first_and_last_color)

# .4 Adding a key to a dictionary
students_mobile_no = {'Alex': '123-456-23', 'Anna': '24-985-12'}
students_mobile_no['Jhon'] = '44-435-90'
# print(students_mobile_no)

# 5. Calculating BMI- body mass index
weight = input('Enter your weight in kg: >  ')
height = input('Enter your height in m: > ')
bmi = float(weight) / (float(height) ** 2)

# Additional Exercises

# 6. Guess a number game - between 1 to 9.
winner_number = 5
guessed_number = int(input('Guess any number from 1 to 9:> '))

while guessed_number != winner_number:
    if guessed_number in range(1, 10):
        guessed_number = int(input('Guess again any number from 1 to 9: > '))
    else:
        guessed_number = int(input('Number should be from 1 to 9, Guess again: > '))
print('Well guessed!!')

# 7. Tuple with different data types
mixed_tuple = (3, True, 'string type', [1, False, 'Python'],
               {'Jonas': 'jona_23@hot.mail', 'Viktoria': 'hadvik_96@gmail.com'})
# print(mixed_tuple)

# 8. Create a list of 5 city names and convert it into tuples
cities = ['Rome', 'Paris', 'London', 'Copenhagen', 'Berlin']
tuple_cities = tuple(cities)
# print(tuple_cities)

# 9. Remove duplicated from the list
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a.remove(80)
b = []
for num in a:
    if num not in b:
        b.append(num)
a = b
# print(a)

# 10. Accept a string from user and remove the ...
# characters which have odd index values of a given string and print them


def remove_odd_index(word):
    even_index_char = word[0::2]
    print(even_index_char)


remove_odd_index('Python')