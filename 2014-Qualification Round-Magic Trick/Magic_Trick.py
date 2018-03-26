
# import ipdb; ipdb.set_trace()

def return_result(first_row, second_row, first_array, second_array):
    first_array = to_list(first_array)
    second_array = to_list(second_array)
    first_row = int(first_row)
    second_row = int(second_row)
    same = []
    for i in first_array[ first_row - 1 ]:
        if i in second_array[ second_row - 1 ]:
            tmp = second_array[ second_row - 1 ].index(i)
            same.append(tmp)
    if len(same) == 0:
        re = 'Volunteer cheated!'
    elif len(same) == 1:
        re = second_array[ second_row - 1 ][same[0]]
    else:
        re = 'Bad magician!'
    return re

def to_list(str):
    ls = []
    for i in range(4):
        ls.append(str[i].split())
    return ls

with  open('./A-small-practice.in')  as f:
    data = f.read()
data = data.split('\n')
length = int(data[0])
result = ''
for n in range(length):
    first_row = data[n * 10 + 1]
    second_row = data[n * 10 + 6]
    first_array = data[(n * 10 + 2) : (n * 10 + 6)]
    second_array = data[(n * 10 + 7) : ((n + 1) * 10 + 1)]
    resu = return_result(first_row, second_row, first_array, second_array)
    stri_resu = 'Case #' + str(n+1) + ': ' + str(resu)
    result = result + (stri_resu) + '\n'
with open('./result.out','w') as f:
    f.write(result)
