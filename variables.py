"""
table
object reference count
"""


# -- 8 --

cars = ["bmw","honda","audi"]
empty_lis= []
print(cars)
print(empty_lis)

print (cars[0])
print (cars*20)

print (len(cars))

cars.append("jeep")
cars.insert(0,"bnz")
print ( cars)

x= cars.index("honda")
print(cars.index("honda"))
cars.pop()
print(cars)
#cars.remove("jeep")
print(cars)

slicing = cars[0:2]
print (slicing)

cars.sort()
print(cars)
# -- 7  --
# mor emethods on string

# replace
# a = "1abc2abc3abc"
# print(a.replace('abc','ABC',2))
#
# # substring
#
# sub = a[1:6]
# step = a[1:6:2]
#
# print(sub)
# print(step)
#
# a= "This is string"
# print(a[:] )
# print(a[1:] )
# print(a[-1:] )
#
# print(a[::-1] )
#
# print("hello %s  %s "  %(1,2))
# print("hello %s %s "%("aaa",2))


# -- 6 --
# accessing character sin srtring
# first = "nyc"[0]
# city = "sfo"
# print(first)
#
# """
# len()
# lower()
# upper()
# str()
# """
#
# s= "abc"
# print (len(s))
# print (s.lower())
# print (s.upper())
# print ( "aa" + str(2) )
#


# -- 5 --
# strings
# in "" or ''
# a= "This is simple str"
# b= 'in single quates'
#
# print(a)
# print(b)
#
# c = "need to use 'quates' inside string"
# c = 'need to use "quates" inside string'
# print (c)
#
# d = "anther way to use \"quates\""
# print (d)
#
#
# a = "This is  \
# string"
#
# print(a)


# -- 3 --
# exponanntation
# exponents = 10 ** 20
# print (exponents)
#
# rem = 100%3
# print(rem)
#


# -- 2 --
# import keyword
# print (keyword.kwlist)
#
# x,y = 10,20
# print(x)
# print(y)



# -- 1 --
#  a="nyc"
# b="nyc"
#
# a=123
#
#
# print(a)
# print(b)
# b=456
# print(b)
#
# c='nyc'
# d=c
# print (c==d)
#
# print (c is d)
