with open('files.txt', 'rt', encoding='utf-8') as file:
    cook_book  = {}
    for line in file:
        dish_name = line.strip()
        ingredients_in_a_dish = int(file.readline())
        _list = []
        for i in range(ingredients_in_a_dish):
            emp = file.readline().strip()
            ingredient_name,  quantity, measure = emp.split(' | ')
            _list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = _list
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    list_ = []
    vocabulary = {}
    vocabulary1 = {}
    for dish in dishes:
        list_.extend(cook_book[dish])
    for key in list_:
        food = key['ingredient_name']
        vocabulary1 = {'quantity': int(key['quantity']) * person_count,
               'measure': key['measure']}
        vocabulary[food] = vocabulary1

    print(vocabulary)


(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open('1.txt', 'r', encoding= 'utf - 8') as f:
    vocabulary1 = {}
    res = len(f.readlines())
    vocabulary1['1.txt'] = res

with open('2.txt', 'r', encoding= 'utf - 8') as f:
    res = len(f.readlines())
    vocabulary1['2.txt'] = res

with open('3.txt', 'r', encoding= 'utf - 8') as f:
    res = len(f.readlines())
    vocabulary1['3.txt'] = res

sorted_values = sorted(vocabulary1.values())
sorted_dict = {}
for i in sorted_values:
    for k in vocabulary1.keys():
        if vocabulary1[k] == i:
            sorted_dict[k] = vocabulary1[k]

for key in sorted_dict:
    with open(key, 'r',encoding= 'utf - 8') as f:
        with open(f'4.txt', 'a', encoding= 'utf - 8') as file:
            file.write(key + '\n')
            file.write(str(sorted_dict[key]))
            file.write('\n')
            file.write(f.read() + '\n')
            print(file)