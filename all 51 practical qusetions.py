# # Q1 Write a program to accepts two integers and print their sum.

# a=int(input('Enter the first integer:'))
# b=int(input('Enter the second integer:'))

# Sum=a+b

# print('The two integers are:', a, b)
# print('The sum of two integers are:', Sum)


# # 2.Write a program that accepts radius of a circle and prints its area.
# r=int(input('Enter the radius of circle:'))
# Area=3.14*r**2
# print('The area of the circle is:', Area)


# # 3.Write a program that accepts base and height and calculate the area of triangle

# b=float(input('Enter the base of triangle:'))
# h=float(input('Enter the height of triangle:'))

# Area=(1/2)*b*h

# print('The area of triangle is:', Area)


# # 4 Write a program that inputs a student’s marks in
# # three subjects (out of 100)and prints the percentage marks

# print('Enter the marks of three subject out of 100')
# a=float(input('Enter the marks of first subject:'))
# b=float(input('Enter the marks of second subject:'))
# c=float(input('Enter the marks of third subject:'))

# P=(a+b+c)/3
# print('The percentage marks are:', P,'%')



# #5.Write a program to compute area of square and triangle.

# a=float(input('Enter the value of side:'))

# A=a**2
# T=((3**0.5)/4)*a**2

# print('The area of square is:', A)
# print('The area of triangle is:', T)

# #6. Write a program to calculate simple interest.

# P=float(input('Enter the principal amount in : '))
# R=float(input('Enter the rate of interest: '))
# T=float(input('Enter the time in years: '))

# SI=(P*R*T)/100

# print('The simple interest is : ', SI)


# #7. Write a program to read two numbers and prints their quotient and reminder
# a=float(input('Enter the dividend:'))
# b=float(input('Enter the divisor:'))

# Q=a//b
# R=a%b

# print('The quotient is:', Q)
# print('The remainder is:', R)

# # 8.Write a program to find whether a given number is even or odd.

# a=int(input('Enter the number:'))
# if a%2==0:
#     print('The number is even')
# else:
#     print('The number is odd')



# #9. Write a program to find largest among three integers

# a=int(input('Enter the first integer:'))
# b=int(input('Enter the second integer:'))
# c=int(input('Enter the third integer:'))

# if a>b and a>c:
#     print(a, 'is the largest integer')
# if b>a and b>c:
#     print(b, 'is the largest integer')
# if c>a and c>b:
#     print(c, 'is the largest integer')

 
# # 10.Write a program to find lowest among three integer.
# a=int(input('Enter the first integer:'))
# b=int(input('Enter the second integer:'))
# c=int(input('Enter the third integer:'))

# if a<b and a<c:
#     print(a, 'is the smallest integer')
# if b<a and b<c:
#     print(b, 'is the smallest integer')
# if c<a and c<b:
#     print(c, 'is the smallest integer') 

  
# #11. Write a program to that accepts length and
# # breadth of rectangle and calculate its area.

# l=float(input('Enter the length of rectangle:'))
# b=float(input('Enter the breadth of rectangle:'))
# area=l*b

# print('Rectangle Specifications')
# print('Length=',l)
# print('Breadth=', b)
# print('Area=', area)
# print('Perimeter=', 2*(l+b))


# #12. Write a program that accepts weight in Kg
# # and height in meters and calculate the BMI.

# W = float(input('Enter the weight in Kg:'))
# H = float(input('Enter height in meters:'))
# BMI=W/(H**2)

# print('BMI is:', BMI)
# print('BMI is:', round(BMI, 2))


# #13. Write a program that reads the number n
# # and print the value of n², n³ and n⁴.

# a=float(input('Enter the value of n:'))
# b=a**2
# c=a**3
# d=a**4
# print('The value of n² is:', b)
# print('The value of n³ is:', c)
# print('The value of n⁴ is:', d)


# #14. Write a program to accept the marks of five subjects
# # and calculate the average marks.

# a=float(input('Enter the marks of first subject:'))
# b=float(input('Enter the marks of second subject:'))
# c=float(input('Enter the marks of third subject:'))
# d=float(input('Enter the marks of fourth subject:'))
# e=float(input('Enter the marks of fifth subject:'))
# Average=(a+b+c+d+e)/5
# print('The average marks are:', Average)



# #15. Write a program to accept the marks of five subjects
# # and calculate the average marks.

# a=float(input('Enter the marks of first subject:'))
# b=float(input('Enter the marks of second subject:'))
# c=float(input('Enter the marks of third subject:'))
# d=float(input('Enter the marks of fourth subject:'))
# e=float(input('Enter the marks of fifth subject:'))
# Average=(a+b+c+d+e)/5
# print('The average marks are:', Average)



# #16. Write a program that accepts the age and
# # print if one is eligible to vote or not.
# a=int(input('Enter your age:'))
# if a>=18:
#     print('You are eligible to vote')
# else:
#     print('You are not eligible to vote')


 
# # 17. Write a program that accepts two numbers and
# # check if the first number is fully divisible by second number or not.

# a=float(input('Enter the first number:'))
# b=float(input('Enter the second number:'))
# if a%b==0:
#      print('The first number is fully divisible by second number')
# else:
#      print('The first number is not fully divisible by second number')


   
# #18.Write a program to read base, width and height of
# #parallelogram and calculate its area and perimeter.

# b=float(input('Enter the base of parallelogram:'))
# w=float(input('Enter the width of parallelogram:'))
# h=float(input('Enter the height of parallelogram:'))

# Area=b*h
# Perimeter=2*(b+w)

# print('The area of parallelogram is:', Area)
# print('The perimeter of parallelogram is:', Perimeter) 



# #119. Write a program to accept the year and
# # check if it is a leap year or not.

# a=int(input('Enter the year:'))
# if a%4==0:
#      print('This year is a leap year')
# else:
#      print('This year is not a leap year')


     
# #20. Write a program to obtain x, y, z and calculate 4x⁴+3y³+9z+6π.

# import math
# print('To calculate 4x⁴+3y³+9z+6π')
# x=float(input('Enter the number x:'))
# y=float(input('Enter the number y:'))
# z=float(input('Enter the number z:'))

# b=(4*math.pow(x,4))+(3*math.pow(y,3))+(9*z)+(6*math.pi)
# print('The result of the above expression is:',b)


# #21. Write a program to input a number and print its
# # square if it is odd, otherwise print its square root.

# import math

# x=float(input('Enter the number:'))

# a=math.pow(x,2)
# b=math.sqrt(x)
# if x%2!=0:
#      print('The value of square is:',a)
# else:
#      print('The value of square root is:',b)


# #22. Write a program to input a number and check whether
# # it is positive, negative or zero.

# a=float(input('Enter the number:'))

# if a>=0:
#      if a==0:
#           print('The number is zero')
#      else:
#           print('The number is a positive number')
# else:
#      print('The number is a negative number')


# '''
# 23. Write a program to input percentage marks of a student and find the grade as per following criterion:
# Marks           Grade
# >=90             A
# 75-90            B 
# 60-75            C     
# Below 60         D
# '''
# a=float(input('Enter the percentage marks:'))
# if a>=90:
#      print('The student has got an A grade')
# elif a>=75 and a<90:
#      print('The student has got a B grade')
# elif a>=60 and a<75:
#      print('The student has got a C grade')
# else:
#      print('The student has got a D grade')

# #24. Write a program to enter a number and
# # check if it is a prime number or not.

# num=int(input('Enter the number:'))
# for i in range(2,num//2+1):
#      if num%i==0:
#         print('It is not a prime no.')
#      break
# else:
#     print('It is a prime number')

# #25.Write a program to display a menu for calculating
# # area of circle or perimeter of the circle.

# r=float(input('Enter the radius of the circle:'))
# print('1.Calculate perimeter')
# print('2.Calculate area')
# choice=int(input('Enter your choice (1 or 2):'))
# if choice==1:    
#      peri=2*3.14159*r
#      print('Perimeter of the circle with radius',r,':',peri)
# else:
#      area=3.14159*r*r
#      print('Area of the circle of the radius',r,':',area)

# #26.Write a program that reads two numbers and an
# # arithmetic operator and displays the computed result.
# a=float(input('Enter the first number:'))
# b=float(input('Enter the second number:'))
# c=input('Enter the operator[/,*,+,-]:')
# if c=='/':
#     r=a/b
# elif c=='*':
#     r=a*b
# elif c=='+':
#     r=a+b
# elif c=='-':
#     r=a-b
# else:
#      print('Invalid operator')
# print(a,c,b,'=',r)

# #27.Write a program to print whether a given character
# # is an uppercase or a lowercase character or a digit or any other character.


# ch=input('Enter a single character:')
# if ch>='A'and ch<='Z':
#      print('You have entered an uppercase character.')
# elif ch>='a'and ch<='z':
#      print('You have entered an lowercase character.')
# elif ch>='0'and ch<='9':
#      print('You have entered a digit.')
# else:
#      print('You have entered a special character.')
 

# #28.Write a program to calculate and print the roots of a
# # quadratic equation ax²+bx+c=0.(a≠0)

# import math
# print('For quadratic equation, ax²+bx+c=0,enter coefficents below')
# a=int(input('Enter a:'))
# b=int(input('Enter b:'))
# c=int(input('Enter c:'))
# if a==0:
#      print('Value of a should not be zero')
#      print('Aborting!!')
# else:
#     d=b*b-4*a*c
# if d>0:
#      root1=(-b+math.sqrt(d))/(2*a)
#      root2=(-b-math.sqrt(d))/(2*a)
#      print('Roots are real and unequal')
#      print('Root1=',root1,',Root2=',root2)
# elif d==0:
#      root1=-b/2*a
#      print('Roots are real and equal')
#      print('Root1=',root1,',Root2=',root1)
# else:
#      print('Roots are complex and imaginary')

# #29. Write a program to print the sum of natural numbers between 1 to 20.
# # Print the sum progressively i.e. after adding each natural number,
# # print sum so far.

# Sum=0
# for n in range(1,21):
#     Sum+=n
# print('Sum of natural numbers <=',n,'is',Sum)
 

# #30. Write a program to calculate the factorial of a number.

# num=int(input('Enter a number:'))
# fact=1
# a=1
# while a<=num:
#     fact*=a
#     a+=1
# print('The factorial of',num,'is',fact)

# #31.Write a program to create a triangle of stars using nested loop.

# for i in range(1,6):
#      print()
#      for j in range(1,i):
#           print('*',end=' ')

# #32. Write a Python script to print Fibonacci series’ first 10 elements.

# first=0
# second=1
# print(first, end=' ')
# print(second,end=' ')
# for a in range(1,9):
#      third=first+second
#      print(third,end=' ')
#      first,second=second,third
 

# #33.Write a program to read an integer>1000 and reverse the number.

# num=int(input('Enter a number (>1000):'))
# tnum=num
# reverse=0
# while tnum>0:
#     digit=tnum%10
#     reverse=reverse*10+digit
#     tnum=tnum//10
# print('Reverse of',num,'is',reverse)

# #34.Input three angles and determine if they form a triangle or not.

# angle1=angle2=angle3=0
# angle1=float(input('Enter the first angle:'))
# angle2=float(input('Enter the second angle:'))
# angle3=float(input('Enter the third angle:'))

# if angle1+angle2+angle3==180:
#      print('The angles form a triangle')
# else:
#      print('The angles do not form a triangle')

# #35.Write a Python script that displays first ten Mersenne numbers.
# print('First 10 Mersenne numbers are:')
# for a in range(1,11):
#      mersnum=2**a-1
#      print(mersnum,end=' ')
# print()

# #36.Write a Python script that displays first ten
# # Mersenne numbers and displays ‘Prime’ next to Mersenne Prime Numbers.
# for a in range(1,21):
#      mersnum=2**a-1
#      mid=mersnum//2+1
#      for b in range(2,mid):
#           if mersnum%b==0:
#                print(mersnum)
#                break
#      else:
#           print(mersnum,'\tPrime')

# #37. 
# '''

# # Write a program to calculate BMI and print
# # the nutritional status as per following table:
# Nutritional     WHO criteria

# Status         (BMI cut-off)
# Underweight         <18.5
# Normal            18.5-24.9
# Overweight        25-29.9
# Obese               ≥30
# '''

# w=float(input('Enter the weight in kgs:'))
# h=float(input('Enter the height in meters:'))
# BMI=w/h**2
# print('BMI is',BMI,end='')
# if BMI<18.5:
#      print('...Underweight')
# elif BMI>=18.5 and BMI<24.9:
#      print('...Normal')
# elif BMI>=25 and BMI<29.9:
#      print('...Overweight')
# else:
#      print('...Obese')

# #38. Write python script to print the following pattern.
# '''
# 1 
# 1 3 
# 1 3 5 
# 1 3 5 7
# '''
# for a in range(3,10,2):
#      print()
#      for b in range(1,a,2):
#           print(b, end=' ')
# print()

# #39. Write a program to find sum of series : s=1+x+x²+x³+x⁴…+xⁿ

# x=float(input('Enter the value of x:'))
# n=int(input('Enter the value of n (for x**n):'))
# s=0
# for a in range(n+1):
#     s+=x**a
# print('Sum of first' ,n,'terms:',s)
 
# #40.Write a python script to input two numbers
# #and print their lcm and hcf.
# x=int(input('Enter the first number:'))
# y=int(input('Enter the second number:'))
# if x>y:
#     smaller=y
# else:
#     smaller=x
# for i in range(1,smaller+1):
#      if x%i==0 and y%i==0:
#           hcf=i
#           lcm=(x*y)/hcf
# print('The HCF of',x,'and',y,'is:',hcf)
# print('The LCM of',x,'and',y,'is:',lcm)

# #41. Write a python script to calculate the
# # sum of the following series: S=(1)+(1+2)+(1+2+3)+……+(1+2+3+….+n)

# Sum=0
# n=int(input('How many terms?'))
# for a in range(2,n+2):
#      term=0
#      for b in range(1,a):
#           term+=b
#      print('Term',(a-1),':',term)
#      Sum+=term
# print('Sum of',n,'terms is:',Sum)


# '''
# 42.Write a program to print the following using a single loop (no nested loops)
# 1
# 11
# 111
# 1111
# 11111
# '''

# n=1
# for a in range(5):
#      print(n,end = ' ')
#      print()
#      n=n*10+1

# '''
# 43. Write a program to print a pattern like:
# 4 3 2 1 
# 4 3 2 
# 4 3 
# 4
# '''
# for i in range(4):
#      for j in range(4,i,-1):
#           print(j,end=' ')
#      else:
#           print()

# #44.Program that reads a line and print its statistics like:
# '''
# Number of uppercase letters:
# Number of lowercase letters:
# Number of alphabets:
# Number of digits:
# '''
# line=input('Enter a line:')
# lowercount=uppercount=0
# digitcount=alphacount=0

# for a in line:
#      if a.islower():
#         lowercount+=1
#      elif a.isupper():
#         uppercount+=1
#      elif a.isdigit():
#         digitcount+=1
#      if a.isalpha():
#         alphacount+=1

# print('Number of uppercase letters are:',uppercount)
# print('Number of lowercase letters are:',lowercount)
# print('Number of alphabets are:',alphacount)
# print('Number of digits are:',digitcount)
 

# #45.Write a program that reads a line and a substring
# #and displays the number of occurrences of the given substring in the line.

# line=input('Enter line:')
# sub=input('Enter substring:')
# length=len(line)
# lensub=len(sub)
# start=count=0
# end=length

# while True:
#      pos=line.find(sub,start,end)
#      if pos!=-1:
#         count+=1
#         start=pos+lensub
#      else:
#           break
#      if start>=length:
#           break
# print('No. of occurences of',sub,':',count)

# #46.Write a program that takes a string with multiple
# #words and then capitalizes the first letter of each word
# #and forms a new string out of it.

# string=input('Enter a string:')
# length=len(string)
# a=0
# end=length
# string2=''

# while a<length:
#      if a==0:
#         string2+=string[0].upper()
#         a+=1
#      elif(string[a]==' ' and string[a+1]!=' '):
#         string2+=string[a]
#         string2+=string[a+1].upper()
#         a+=2
#      elif (string[a]==',' and string[a+1]!=','):
#         string2+=string[a]
#         string2+=string[a+1].upper()
#         a+=2
#      else:
#         string2+=string[a]
#         a+=1
# print('Original string:',string)
# print('Capitalized words string:',string2)
 

# #47.Write a program that reads a string and
# #checks whether it is a palindrome string or not.

# string=input('Enter a string:')
# length=len(string)
# mid=length//2
# rev=-1
# for a in range(mid):
#      if string[a]==string[rev]:
#           print(string,'is a palindrome.')
#           break
#      else:
#           print(string,'is not a palindrome.')
#           break
     

# #48.Write a program that reads a string and displays
# #the longest substring of the given string having
# #just the consonants.

# string=input('Enter a string:')
# length=len(string)
# maxlength=0
# maxsub=''
# sub=''
# lensub=0
# for a in range(length):
#      if string[a] in 'aeiou' or string[a] in 'AEIOU':
#           if lensub>maxlength:
#             maxsub=sub
#             maxlength=lensub
#             sub=''
#             lensub=0
#      else:
#           sub+=string[a]
#           lensub=len(sub)
#           a+=1
# print('Maximum length consonant substring is:',maxsub,end=' ')
# print('with',maxlength,'characters')

# #49.Write a program that reads a string and then
# # prints a string that capitalizes every other letter in the string.

# string=input('Enter a string:')
# length=len(string)
# print('Original string:',string)
# string2=''
# for a in range(0,length,2):
#     string2+=string[a]
#     if a<length-1:
#         string2+=string[a+1].upper()
# print('Alternatively capitalized string:',string2)


# #50.Write a program that reads the email id of a person
# # in the form of a string and ensures that it belongs to
# # domain @learnpython4cbse.com(Assumption:no invalid characters
# # are there in email-id)

# email=input('Enter your email id:')
# domain='@learnpython4cbse.com'
# ledo=len(domain)       #ledo=length of domain
# lema=len(email)         #lema=length of email
# sub=email[lema-ledo:]

# if sub==domain:
#      if ledo!=lema:
#           print('It is valid email id')
#      else:
#           print('This is invalid email id- contains just the domain name')
# else:
#      print('This email-d is either not valid or belongs to some other domain')



# #51.WAP to remove all odd numbers from the given list.

# L= [2, 7,12, 5,10,15,23]
# for i in L: 
#      if i%2!=0: 
#           L.remove (i) 
# print (L) 