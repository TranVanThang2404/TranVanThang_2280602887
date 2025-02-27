def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List nhập vào là: ", numbers)
print("Tuple tạo từ list là: ", my_tuple)