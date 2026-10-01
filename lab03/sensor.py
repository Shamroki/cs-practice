st1 = float(input('Введите порог в градусах Цельсия '))
n = int(input('Введте количество записей '))
count_error = 0
count_increase = 0
mx = -1000000000000
sr_sum = 0
for i in range(n):
    new_st = input()
    if new_st == 'error':
        count_error += 1

    if new_st != 'error':
        if  float(new_st)> st1 :
            count_increase  += 1


    if new_st != 'error'  :
        if float(new_st)> mx:
            mx = float(new_st)


    if new_st != 'error':
        sr_sum += float(new_st)

print(n)
print(count_error)
print(count_increase)
print(f'{mx:.1f}')
print(f'{(sr_sum/(n-count_error)):.1f}')
