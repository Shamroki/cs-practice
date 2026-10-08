def winner(names , scores) :
    mx = -100000
    max_num = 0
    for i in range(len(names)):
        if scores[i] > mx:
            mx = scores[i]
            max_num = i
    return names[max_num]
