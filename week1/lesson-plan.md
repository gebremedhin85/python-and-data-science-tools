# Week 1 : Introduction about course and Python 

## Pre-requisites:
Installation Python and Pycharm

## Lesson Plan:
### 1.	Introduction to Machine learning + application
### 2.	Python installation + Pycharm

Installation Guide : Install [python 3.75](https://www.python.org/downloads/release/python-375/) and [Pycharm community (free) version for practical concepts](https://www.jetbrains.com/pycharm/download/). 

### 3.	Python basic course.  Cheat sheets with syntax and examples will be provided.

#### Variables
- - - -

We use variables to temporarily store data in the computer’s memory

  &emsp; &emsp; price = 10
<br>  &emsp; &emsp; rating = 4.9
<br>  &emsp; &emsp; course_name = ´Python for Begginers´
<br>  &emsp; &emsp; is_published = True

In the example above, <br>

<space>      &emsp; &emsp; <strong>price</strong> is an integer, a whole number without a decimal point;
<br>  &emsp; &emsp; <strong>rating</strong> is a float, a number with a decimal point;
<br>  &emsp; &emsp; <strong>course_name</strong> is a string, a sequence of characters;
<br>  &emsp; &emsp; <strong>is_published</strong> is a boolean. Boolean values can be True or False.

#### Comments
- - - -

We use comments to add notes to our code. Good comments explain the how’s and why’s, not what the code does. That should be reflected in the code itself. Use comments to add reminders to yourself or other developers, or also to explain your assumptions and the reasons you have written code in a certain way.<br>
<br>  &emsp; &emsp; \# This is a comment and it won’t get executed.
<br>  &emsp; &emsp; \# Our comments can be multiple lines.

#### Receiving Input
- - - -

We can receive input from the user by calling the <strong>input()</strong> function.<br>
<br>  &emsp; &emsp; birth_year = int(input(‘Birth year: ‘))

The <strong>input()</strong> function always returns data as a string. So, we’re converting the result into an integer by calling the built-in <strong>int()</strong> function.


#### Strings   
- - - -

We can define strings using single (‘ ’) or double (“ ”) quotes.

To define a multi-lined string, we surround our string with triple quotes (“ “ “).

We can get individual characters in a string using square brackets [ ]. <br> 

 &emsp; &emsp; course  = ‘Python for Begginers’
<br>  &emsp; &emsp; course [0]     \# returns the first character
<br>  &emsp; &emsp; course [1]     \# returns the second character
<br>  &emsp; &emsp; course [-1]    \# returns the first character from the end
<br>  &emsp; &emsp; course [-2]    \# returns the second character from the end


We can slice a string using a similar notation:

 &emsp; &emsp; course [1:5]

The above expression returns all the characters starting from the index position of 1 to 5 (but excluding 5).<br>
The result will be <strong>ytho</strong>

If we leave out the start index, 0 will assumed
If we leave out the end index, the length of the string will be assumed.

We can use formatted strings to dynamically insert values into our strings:

 &emsp; &emsp; name = ‘Mosh’
<br> &emsp; &emsp; message = f’Hi, my name is {name } ’

<br> &emsp; &emsp; message.upper() &emsp; &emsp; &emsp; &emsp; &emsp; \# to convert to uppercase
<br> &emsp; &emsp; message.lower() &emsp; &emsp; &emsp; &emsp; &emsp; \# to convert to lowercase
<br> &emsp; &emsp; message.title()     &emsp; &emsp;&emsp; &emsp; &emsp; \# to capitalise the first letter of every word
<br> &emsp; &emsp; message.find(‘p’)   &emsp; &emsp; &emsp; &emsp; &emsp; \# return the index of the first occurrence of p (or -1 not found)
<br> &emsp; &emsp; message.replace(‘p’, ‘q’) &emsp; &emsp; \# replaces all the p's for q's

To check if a string contains a character or a sequence of characters, we use the <strong> in </strong> operator<br>
<br>  &emsp; &emsp; contains = ‘Python’ in course

#### Arithmetic Operations
- - - -

| Operator | Name               | Example  |  Result |
| ----     | -------------- | -----------------------------------| -------- |
| +	| Addition |	x + y |  |
| -	| Subtraction	| x - y |  |
| *	| Multiplication	| x * y | |
| /	| Division	| x / y | returns a float |
| //	| Floor division	| x // y | returns an int |
| %	| Modulo 	| x % y  | returns the remainder of a division|
| %	| Exponentiation | x ** y = x to the power of y <br> or <br> pow(x,y) (pow(base, exponent)) | returns the result of raising the first operand <br>to the power of the second operand.| 


Augmented assignment operator:

&emsp; &emsp;  x = x + 10<br>
&emsp; &emsp;  x += 10

Operator precedence
1. Parenthesis
2. Exponentiation
3. Multiplication/Division
4. Addition/Subtraction


#### If Statements     
- - - -

```
if is_hot: 
  print(“hot day”)
elseif is_cold
  print(“cold day”)
else: 
  print(“beautiful day”)
  ```

Logic operators

```
if has_high_income and has_good_credit:
	…
if has_high_income or has_good_credit:
	…
is_day = True
is_night = not is_day
```

#### Comparison operators    
- - - -

| Comparison | Description               | Example  |  Result |
| ----     | ------------------ | ---------| -------- |
| a > b	 |  If the value of a is less than the value of b, then condition becomes true. |	6 > 3 | true  |
| a >= b |  If the value of a is greater than or equal to the value of b, then condition becomes true. |	6 >= 6 | true  |
| a < b  |  If the value of a is less than the value of b, then condition becomes true. |  3 < 6  | true  |
| a <= b |  If the value of a is less than or equal to the b, then condition becomes true. | 6 <= 6 | true  |
| a == b |  If a and b are equal, then the condition becomes true. |6 == 6 | true  |
| a != b |  If a and b are not equal, then condition becomes true. | 6 != 3 | true  |
| a <> b |  If a and b are not equal, then condition becomes true. | 6 <> 3 | true (this operator is deprecated so use != instead) |



#### While loops
- - - -

```
i = 1
while i < 5; 
   print(i)
   i += 1
```

#### For loops     
- - - -

```
for i in range(1, 5):
	print(i)
```
* range(5):     &emsp; &emsp;   \# generates 0,1,2,3,4
* range(1,5):     &emsp; &emsp; \# generates 1,2,3,4
* range(1,5,2):   &emsp; &emsp; \# generates 1,3



#### Lists
- - - -

* numbers = [1, 2, 3, 4, 5]
* numbers = [0]  &emsp; &emsp;    \#  returns the first item of the list
* numbers = [1]   &emsp; &emsp;    \#  returns the second item of the list
* numbers = [-1]   &emsp; &emsp;    \#  returns the first item from the of the list
* numbers = [-2]   &emsp; &emsp;    \#  returns the second item from the of the list
<br>

* numbers.append(6)    &emsp; &emsp;    \#  adds a single element with the value 6 to the end
* numbers.insert(0,6)  &emsp; &emsp;    \#  adds a single element with the value 6 to the index position 0
* numbers.remove(6)    &emsp; &emsp;    \#  removes a single and the first element that has the value 6 
* numbers.pop()        &emsp; &emsp;    \#  removes the last item
* numbers.clear()      &emsp; &emsp;    \#  removes all the items
* numbers.index(8)     &emsp; &emsp;    \#  returns the index of the first item with the value 8
* numbers.sort()       &emsp; &emsp;    \#  returns the list sorted alphabetically 
* numbers.reverse()    &emsp; &emsp;    \#  returns the list reversed without taking into account the content
* numbers.copy()       &emsp; &emsp;    \#  returns a copy of the list  

#### Tuples     
- - - -

#### Dictionaries    
- - - -
 
