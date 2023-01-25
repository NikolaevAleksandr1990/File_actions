all = {}
dict_sum ={}
with open('1.txt', 'r', encoding='utf-8') as f:
    name = '1.txt'
    sum_str = 0
    str_l = []
    for line in f:
        sum_str += 1
        str_l.append(line)
        all[name] = str_l
    dict_sum.setdefault(name, sum_str)

with open('2.txt', 'r', encoding='utf-8') as f:
    name = '2.txt'
    sum_str = 0
    str_l = []
    for line in f:
        sum_str += 1
        str_l.append(line)
        all[name] = str_l
    dict_sum.setdefault(name, sum_str)

with open('3.txt', 'r', encoding='utf-8') as f:
    name = '3.txt'
    sum_str = 0
    str_l = []
    for line in f:
        sum_str += 1
        str_l.append(line)
        all[name] = str_l
    dict_sum.setdefault(name, sum_str)

import operator
sorter_dict = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))

print(all)
print(sorter_dict)

with open('all.txt', 'w', encoding='utf-8') as file:
    for key in sorter_dict.keys():
        file.write(key)
        file.write('\n')
        file.write(str(len(all[key])))
        file.write('\n')
        for i in all[key]:
            text = i.strip()
            file.write(text)
            file.write('\n')
            print(text)
