# THis file is for the use of list and map in python

numbers = [1, 2, 3, 4, 5]

# result = map(lambda x: x * x, numbers)


def square(listParam):
    return list(map(lambda x: x * x, listParam))

print(square(numbers))

if __name__ == "__main__":
      print("="* 100)  
      print(numbers)
      print(square(numbers))
      print("="* 100)