# 1. Define an empty variable named "my_list".

my_list = None



# 2. Define an empty list with the variable name "your_list".

your_list = []


# 3. Convert "my_list" from NoneType to a list.
#       Then using a loop fill "my_list" with numbers 9 - 0.

my_list = []

loop = 9
while loop > -1:
    my_list.append(loop)
    loop = loop -1
   
print(my_list)

# 4. In the simplest way possible, sort "my_list" from least to greatest.

my_list.sort()
print(my_list)

# 5. Using "my_list" store only the even numbers into "your_list".

for shitwhatinthelist in my_list:
    # 3 / 2 = 1.5 | 0.5 == 0
    if shitwhatinthelist % 2 == 0:
        your_list.append(shitwhatinthelist)

print(your_list) 
