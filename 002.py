# 1. What will be printed to the console?
#       (DO NOT RUN THE CODE)

num = 42


def add_one():
    num = 1
    print(num)


add_one()

# 1


# 2. Place an [ X ] for the correct answer.
#       When running the following code, what will get outputted to the console.
#       (DO NOT RUN THE CODE)

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

for value in prices:
    print(value)

# [X] apple orange banana
# [  ] 0.40 0.35 0.25
# [  ] 'apple': 0.40 'orange': 0.35 'banana': 0.25


# 3. Place an [ X ] next to all correct answers.
#       What does the following code do?

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

for key, value in prices.items():
    prices[key] = round(value * 0.9, 2)

# [  ] Rounds all values to 90%
# [X] Applies a 10% discount
# [  ] Rounds the decimal place to the 100th place


# 4. Place an [ X ] next to one of the following that is an invalid variable name?
#   [  ] my_string_1
#   [X] 1st_string
#   [  ] foo
#   [  ] _

# 5. What will be the output of the following code?

say_hello = "Hello, World!"
print(say_hello[:2])

# "Hello, World!Hello, World!"