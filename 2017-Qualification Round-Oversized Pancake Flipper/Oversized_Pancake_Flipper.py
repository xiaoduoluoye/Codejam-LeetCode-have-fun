# import ipdb
def judge_times(single_pancake, row_len, k):
    times = 0
    if '-' not in single_pancake:
        result = times
    elif '+' not in single_pancake:
        # ipdb.set_trace()
        if (row_len >= k) and (row_len % k == 0):
            result = row_len/k
        else:
            result = 'IMPOSSIBLE'
    else:
        single_pancake = single_pancake[single_pancake.index('-'):]
        row_len = len(single_pancake)
        while row_len > k:
            for t in range(k):
                if single_pancake[t] == '-':
                    single_pancake[t] = '+'
                else:
                    single_pancake[t] = '-'
            times += 1
            if '-' not in single_pancake:
                result = times
                break
            else:
                single_pancake = single_pancake[single_pancake.index('-'):]
                row_len = len(single_pancake) #length of the pancake
        if row_len <= k:
            if '-' not in single_pancake: #if the smallest num is 1, it's no need to flipper the pancake
                result = times
            elif '+' in single_pancake:
                result = 'IMPOSSIBLE'
            elif row_len == k:
                result = times + 1
            else:
                result = 'IMPOSSIBLE'
    return result

# with open('./A-small-practice.in','r') as f:
#     pancake = f.read()
with open('./A-large-practice.in','r') as f:
    pancake = f.read()

pancake = pancake.split('\n')
length = pancake[0]
pancake = pancake[1:]
result = ''
for i in range(int(length)):
    single_pancake = list(pancake[ i ].split()[0])
    k = int(pancake[ i ].split()[-1])
    row_len = len(single_pancake)  #length of the pancake
    single_result = judge_times(single_pancake, row_len, k)
    # ipdb.set_trace()
    res_str = 'Case #' + str(i + 1) + ': ' + str(single_result)
    result += res_str + '\n'
# with open('./small-result.out', 'w') as f:
#     f.write(result)
with open('./large-result.out', 'w') as f:
    f.write(result)
