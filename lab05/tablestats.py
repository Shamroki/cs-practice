# def read_rows(lines):
#     work_lines = list(lines)
#     titles = list(map(lambda l:l.strip(),work_lines[0].split(',')))
#     result = []
#
#     for line in work_lines[1:]:
#         work = line.split(',')
#
#         if len(work) == len(titles):
#             result_line = {}
#
#             for i in range(len(work)):
#                 result_line.update({titles[i]:work[i].strip() })
#
#                 result.append(result_line)
#     return result



#python main.py

# def count_types(rows):
#     types = {}
#
#     for line in rows:
#         if line['тип'] in types:
#             types[line['тип']] += 1
#         else:
#             types:update({line['тип']:1})
#     return types
#
#
# def total_minutes(rows,kind):
#     sum = 0.0
#
#     for line in rows:
#         if line['тип'] == kind:
#             sum += float(line['минуты'])
#     return sum
        


#def to_csv(counts):
    #result = "тип;количество\n"
    #new_counts = sorted(counts,key = lambd c: c[0])

    #for type in new_counts:
        #result += f"{}"

def read_rows(lines):
    t = []
    lines = list(lines)
    for line in lines[1:]:
        line = line.strip().split(',')

        if len(line) == 3:
            line = {'дата':line[0],'тип':line[1],'минуты':line[2]}
            t += [line]
    return t

def count_types(rows):
    types = {}
    for line in rows:
        if line['тип'] not in types:
            types[line['тип']] = 0
        types[line['тип']] += 1
    return types

def total_minutes(rows,kind):
    sum = 0.0
    for line in rows:
        if line['тип'] == kind:
            sum += float(line['минуты'])
    return round(sum,1)

def to_csv(counts):
    stroka = 'тип,количество\n'
    stroka += f"выгрузка,{counts['выгрузка']}\n"
    stroka += f"запуск',{counts['запуск']}\n"
    stroka += f"ошибка,{counts['ошибка']}\n"
    stroka += f"проверка,{counts['проверка']}\n"
    return stroka























































