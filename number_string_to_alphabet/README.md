If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

For example:
Input: "1123". You need to general all valid alphabet codes from this string.

Output List
aabc //a = 1, a = 1, b = 2, c = 3
kbc // since k is 11, b = 2, c= 3
alc // a = 1, l = 12, c = 3
aaw // a= 1, a =1, w= 23
kw // k = 11, w = 23


Test:
Input a number string( eg:1123 ):1123
aabc//a=1,a=1,b=2,c=3
aaw//a=1,a=1,w=23
alc//a=1,l=12,c=3
kbc//k=11,b=2,c=3
kw//k=11,w=23

Input a number string( eg:1123 ):6712
fgab//f=6,g=7,a=1,b=2
fgl//f=6,g=7,l=12

Input a number string( eg:1123 ):1234312
abcdcab//a=1,b=2,c=3,d=4,c=3,a=1,b=2
abcdcl//a=1,b=2,c=3,d=4,c=3,l=12
awdcab//a=1,w=23,d=4,c=3,a=1,b=2
awdcl//a=1,w=23,d=4,c=3,l=12
lcdcab//l=12,c=3,d=4,c=3,a=1,b=2
lcdcl//l=12,c=3,d=4,c=3,l=12
