# Функция для переписывания элементов из списка А в список В,
# исключая элементы, равные заданному значению K
def copy_without_k(lst, k):
    return [num for num in lst if num != k]


# Функция для вставки значения K в упорядоченный список lst
def insert_into_sorted_list(lst, k):
    index = 0
    for num in lst:
        if num > k:
            break
        index += 1
    lst.insert(index, k)


# Функция для заполнения заданного числа элементов списка заданным значением
def fill_with_value(lst, k, count):
    for _ in range(count):
        lst.append(k)


# Функция для подсчета количества элементов списка, превышающих значение K
def count_elements_above_k(lst, k):
    return sum(1 for num in lst if num > k)


# Функция для вычисления суммы значений элементов списка, меньших значения K
def sum_of_elements_below_k(lst, k):
    return sum(num for num in lst if num < k)


# Функция для вычисления произведения значений элементов списка
def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product


# Функция для удаления элемента с заданным порядковым номером из списка
def remove_element_by_index(lst, index):
    if index >= 0 and index < len(lst):
        del lst[index]


# Функция для замены значений элементов списка на заданное значение,
# исключая значения, равные заданному значению K
def replace_values(lst, k, m):
    for i in range(len(lst)):
        if lst[i] != k:
            lst[i] = m


# Функция для поиска элемента с наибольшим значением в списке
def find_max(lst):
    if len(lst) == 0:
        return None
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value


# Функция для подсчета количества максимальных элементов в списке
def count_max_elements(lst):
    max_value = find_max(lst)
    if max_value is None:
        return 0
    return sum(1 for num in lst if num == max_value)