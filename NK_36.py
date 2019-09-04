import sys

big_bracket=0
mid_bracket=0
quotation=0
error_set = set()
lastline = ''
input_buff = []
while True:
    input_line = sys.stdin.readline().rstrip()
    if not input_line:
        break
    input_buff.append(input_line)

for i, input_line in enumerate(input_buff):
    if ':' in input_line:
        if i>0 and (input_buff[i-1][-1]!=',' and input_buff[i-1][-1]!='{' and input_buff[i-1][-1]!=':'):
            error_set.add('4')

        tmp = input_line.split(':')
        for string in tmp:
            quotation = 0
            for j, char in enumerate(string):

                if char == '{':
                    big_bracket += 1
                elif char == '[':
                    mid_bracket += 1
                elif char == '}':
                    big_bracket -= 1
                    if big_bracket < 0:
                        error_set.add('2')
                elif char == ']':
                    mid_bracket -= 1
                    if mid_bracket < 0:
                        error_set.add('1')
                if char == '"':
                    quotation+=1
            if quotation != 2 and quotation!=0:
                error_set.add('3')
    else:
        for j, char in enumerate(input_line):
            if char == '{':
                big_bracket += 1
                if i > 0:
                    if '}' in input_buff[i - 1] and input_buff[i - 1][-1] != ',':
                        error_set.add('4')

            elif char == '[':
                mid_bracket += 1
                if i > 0:
                    if ']' in input_buff[i - 1] and input_buff[i - 1][-1] != ',':
                        error_set.add('4')
            elif char == '}':
                big_bracket -= 1
                if big_bracket < 0:
                    error_set.add('2')
            elif char == ']':
                mid_bracket -= 1
                if mid_bracket < 0:
                    error_set.add('1')

if big_bracket != 0:
    error_set.add('2')

if mid_bracket != 0:
    error_set.add('1')

if error_set:
    errors = list(error_set)
    errors.sort()
    print(''.join(errors))
else:
    print(0)