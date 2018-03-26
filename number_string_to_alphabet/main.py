from num_str_alphabet import *

num_str = input('Input a number string( eg:1123 ):')
alphabet = [chr(i) for i in range(97,123)]
rst = figure_out(num_str,alphabet)
# import ipdb; ipdb.set_trace()
for i in rst:
    str_print(alphabet,i)
