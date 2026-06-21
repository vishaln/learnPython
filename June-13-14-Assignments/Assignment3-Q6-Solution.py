from sys import getsizeof

# Integer - Data Type
print("Enter Numaric Value")
x = int(input())
print("Data Type : ", type(x))
print("Memory Address  : ",id(x))
print("Memory Size  : ",getsizeof(x))

# Float - Data Type
print("Enter Float Value")
y = float(input())
print("Data Type  : ", type(y))
print("Memory Address  : ",id(y))
print("Memory Size  : ",getsizeof(y))

# Complex - Data Type
print("Enter Complex Value")
z = complex(input())
print("Data Type  : ", type(z))
print("Memory Address  : ",id(z))
print("Memory Size  : ",getsizeof(z))


# String - Data Type
print("Enter String Value")
s = input()
print("Data Type  : ", type(s))
print("Memory Address  : ",id(s))
print("Memory Size  : ",getsizeof(s))