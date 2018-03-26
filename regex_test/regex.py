def f(pattern, string):
    index_i = 0
    index_j = 0
    while index_i < len(string):
        while index_j < len(pattern):
            if pattern[index_j]=='*':
                if index_i == 0:
                    index_j += 1
                    break
                else:
                    index_j += 1
                    index_i += 1
                    if index_j == len(pattern):
                        return True
                    else:
                        break
            elif pattern[index_j] == string[index_i]:
                index_j += 1
                index_i += 1
                if index_j == len(pattern):
                    return True
                else:
                    break
            else:
                if index_j == 0:
                    index_i += 1
                else:
                    index_j = 0
                break
    return False
