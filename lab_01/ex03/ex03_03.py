def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhap day so cach nhau boi dau phay: ")
numbers = list (map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple: ", my_tuple)