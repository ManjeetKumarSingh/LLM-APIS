# First Set Example

# Creating a set
my_set = set([1, 2, 3, 4, 5])

# This function is used to add data to the set
def my_function1(data):
      # print("Adding data to the set:", data)
      my_set.add(data)
      return my_set
# This function is used to remove data from the set
def my_function2(data):
      # print("Removing data from the set:", data)
      my_set.discard(data)
      return my_set

# Function for removing the duplicates from the list and returning the unique values
def remove_duplicates(my_list):
    return list(set(my_list))

if __name__ == "__main__":
    print("Set:", my_set)
#     print("Adding 6 to the set:", my_function1(6))
    my_function1(6)
    #print("Adding 6 to the set:", my_function1(6))
    # print("Removing 6 from the set:", my_function2(6))
    my_function2(2)
    my_function2(7)
    print("Set:", my_set)
    
    print("Removing duplicates from the list [1, 2, 2, 3, 4, 4, 5]:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    