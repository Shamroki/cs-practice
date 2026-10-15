from tablestats import *
with open('events.csv', encoding="utf-8") as table:

    list_dict = read_rows(table)
    count_types_ = count_types(list_dict)
    total_minutes_ = total_minutes(list_dict,kind)
    to_csv_ = to_csv(count_types_)

print(list_dict)
print(count_types_)
print(total_minutes_)
print(to_csv_)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(count_types_))





#python main.py
