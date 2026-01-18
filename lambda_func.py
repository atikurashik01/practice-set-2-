import functools

# lamda function in python ai ml 
#anonymous functionx   --> unnnamed


square = lambda x : x*x 
print(square(5))


# multiple arguments
add = lambda a,b : a+b
print(add(4,6))


# practice 

student = [ ("ashik",23),("atikur",21),("khan",25) ]
sorted_student= sorted(student, key = lambda x:x[1])  # sort by age
print(sorted_student)


# amp() , filter(), reduce()


# using map() function with lambda
nums = [1,2,3,4,5,6,7,8,9,10]
squared_nums= map(lambda x: x*x, nums)
print(list(squared_nums))


# using filter() function with lambda
even_nums = list(filter(lambda x: x%2==0, nums)) # filter even numbers akane lambda sorto use kora hoise
print(even_nums)

# using reduce() function with lambda


sum = functools.reduce(lambda x,y : x+y , nums)
print(sum)

#answer is 55 