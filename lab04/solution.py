def winner(names , scores) :
    mx = -100000
    max_num = 0
    for i in range(len(names)):
        if scores[i] > mx:
            mx = scores[i]
            max_num = i
    return names[max_num]

def average(scores) :

    if len(scores) == 0:
        return 0.0

    sum = 0
    for i in range(len(scores)):
        sum += scores[i]
    average_ = sum/len(scores)
    return round(average_,2)

def ranking(names, scores) :
    result = []
    for i in range(len(scores)):
        result += [i]

    for i in range(len(result)):
        for j in range(i +1,len(result)):
            if scores[result[i]] < scores[result[j]]:
                result[i],result[j] = result[j],result[i]
    return [names[i] for i in result]


def above_average(names, scores):
    a = average(scores)
    t = []
    for i in range(len(names)):
        if scores[i] > a:
            t += [names[i]]
    return t
