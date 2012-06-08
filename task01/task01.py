import sys    
def flip_str1(s):
    for i in range(len(s)):
        sys.stdout.write(s[-i-1])
    sys.stdout.write('\n')


def flip_str2(s):
    for i in range(len(s)):
        print(s[-i-1]),
    print('\n')
        
s=raw_input('Enter string:')
flip_str1(s)
flip_str2(s)