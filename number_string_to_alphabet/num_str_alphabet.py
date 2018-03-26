def str_print(alphabet,alphabet_string):
    print (alphabet_string + '//', end='')
    for index_i,i in enumerate(alphabet_string):
        if index_i < len(alphabet_string)-1:
            print (i + '=' + str(alphabet.index(i)+1),end=',')
        else:
            print (i + '=' + str(alphabet.index(i)+1))

def figure_out(num_str,alphabet):
    result = []
    n = len(num_str)
    if n == 1:
        return alphabet[int(num_str)-1]
    elif n == 2:
        if int(num_str) <= 26:
            return [alphabet[int(num_str[0])-1] + alphabet[int(num_str[1])-1], alphabet[int(num_str)-1]]
        else:
            return [alphabet[int(num_str[0])-1] + alphabet[int(num_str[1])-1]]
    if n > 2:
        # import ipdb; ipdb.set_trace()
        temp = figure_out(num_str[1:],alphabet)
        for i in temp:
            result.append(alphabet[int(num_str[0])-1] + i)
        if int(num_str[0:2]) <= 26:
            temp = figure_out(num_str[2:],alphabet)
            for i in temp:
                result.append(alphabet[int(num_str[0:2])-1] + i)
    return result
