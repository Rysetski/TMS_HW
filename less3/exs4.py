def replace_h(s):
    first_h = s.find('h')
    last_h = s.rfind('h')
    new_s = s[:first_h+1] + s[first_h +
                              1:last_h].replace('h', 'H') + s[last_h:]
    return new_s


original_string = 'hhhabchghhh'
result_string = replace_h(original_string)
print(result_string)
