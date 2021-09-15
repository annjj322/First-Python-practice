# method 1
from functools import reduce
from typing import Collection


print("I'm %d years old" % 20)
print("I like %s" % "python")
print("Apple is start with %c" % "A")

# method 2
print("I'm {}years old" .format(20))
print("I like {} and {}" .format("blue", "red"))

# method 3
print("I'm {age}years old, I like {color}" .format(age = 20, color="red"))

# method 4
age = 20
color = "red"
print(f"I'm {age}years old, I like {color}")
