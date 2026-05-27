
#List comprehension
# 列表推导式用于从一个可迭代对象（如列表、元组、字符串、range 等）快速生成一个新列表。

# 1.for loop
square = [i**2 for i in range(1,5)]
print(square)

# 2.if loop
evens = [i for i in range(1,10) if i % 2 == 0]
print(evens)

# 3.if else loop
result = [i**2 if i%2==0 else i for i in range(1,10)  ]
print(result)


# Dictionary Comprehension 它生成的是字典（键值对）。
# 它的外层使用花括号 {}，并且表达式部分需要写成 key: value 的形式。

# 1.最基本
square_dict = {i: i**2 for i in range(1,10) }
print(square_dict)


# 2.将两个列表合并为字典，zip的用法
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 18]
# 可以：
name_age_dict = {names[i]: ages[i] for i in range(len(names))}
# 更好：dictionary = {key:value for key,value in zip(list1, list2)}
name_age_dict = {name: age for name, age in zip(names, ages)}
# 结果: {'Alice': 24, 'Bob': 30, 'Charlie': 18}

# 3. 带条件筛选
children = {name:age for name, age in name_list() if age < 18}
