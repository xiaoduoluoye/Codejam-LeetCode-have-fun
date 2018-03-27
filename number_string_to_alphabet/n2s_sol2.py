import string
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--string', type=str, help='input string', default='1115123'
    )
    args = parser.parse_args()
    input_string = args.string
    print 'input string is : %s' % input_string
    s = set(string.ascii_lowercase)
    map_dict = {}
    for i, l in enumerate(s):
        map_dict.setdefault(l,i+1)

    stack = []
    node = {
        'string': input_string[0],
        'left': True,
        'right': True,
    }
    stack.append(node)
    i = 1

    while len(stack) > 0:
        if i >= len(input_string):
            print stack[-1]
            stack.pop()
            i -= 1
        last_node = stack[-1]
        if last_node['left']:
            last_node['left'] = False
            node = {
                'string': last_node['string'] + ',' + input_string[i],
                'left': True,
                'right': True,
            }
            stack.append(node)
            i += 1
            continue


        elif last_node['right']:
            last_node['right'] = False
            temp = last_node['string'].split(',')
            value = int(temp[-1] + input_string[i])
            if value <= 26:
                node = {
                    'string': last_node['string'] + input_string[i],
                    'left': True,
                    'right': True,
                }
                stack.append(node)
                i += 1
                continue
        else:
            stack.pop()
            i -= 1
