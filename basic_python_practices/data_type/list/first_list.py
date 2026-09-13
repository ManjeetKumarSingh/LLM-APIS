# This module is for the list data type in python

my_list = [1, 8, 3, 4, 5]

def my_function1(data):
    my_list.append(data)
    return my_list      

def my_function2(data):
      if data in my_list:
            my_list.remove(data)
      return my_list
    
def my_function3(data):
    my_list.extend(data)
    return my_list
 
def my_function4():
    return sorted(my_list)

if __name__ == "__main__":
    print("="* 160)  
    print(my_list)
#     print(my_function1([6, 7, 8]))
    print(my_function3([2, 3]))
    print(my_function4())
    print("="* 160)