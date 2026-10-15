from tablestats import *
with open('events.csv', encoding="utf-8") as table:

    lines = read_rows(table)



types = count_types(lines)
line_count = 0

for cnt in types:
    line_count += float(types[cnt])



print()
print(line_count)
print(len(types))
print(total_minutes(lines,'ошибка'))

with open("summary.csv")


#python main.py
