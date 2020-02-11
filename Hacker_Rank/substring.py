def count_substring(string, sub_string):
    if sub_string in string:
        print('yes')
        print(string.index(sub_string))

count_substring('I am an Indian, by birth.','Birth')