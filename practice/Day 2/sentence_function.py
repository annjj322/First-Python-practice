python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))  #if there's no Java == -1
# print(python.index("Java")) #index == error // its done

print(python.count("n")) #how many "n"
