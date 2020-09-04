def count_substring(string, sub_string):
     count = 0
     start = 0
     while start < len(string):
        pos = string.find(sub_string, start) 
        if pos != -1: 
            start = pos + 1
            count += 1
        else: 
            break
     return count 
  

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print (count)