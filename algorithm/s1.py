# s = input()
# list = [ i for i in s]
# # list[:0] = s 
# # print (list)
# # for i in range (len(list)):
# result = [False, False, False, False, False]
# for i in s:
#     if i.isalnum():
#         result[0] = True
#     if i.isalpha(): 
#         result[1] = True
#     if i.isdigit(): 
#         result[2] = True
#     if i.islower(): 
#         result[3] = True
#     if i.isupper(): 
#         result[4] = True
# for i in result:
#     print (i)

# 0123 4567 89
# string, max_width = input(), int(input())
# i = max_width
# for int i in string:
#     print (string[i])

import textwrap

def wrap(string, max_width):
    # my method
    # list = [ i for i in string]
    # i = max_width
    # while i < len(list):
    #     list.insert(i,' ')
    #     i = i + 1 + max_width
    # string1 = " "
    # string1 = ''.join(list)
    # x = string1.split()
    # z =""
    # for i in x:
    #     z = z + i + '\n' 
    # return z
    
    wrapper = textwrap.TextWrapper(width=max_width)
    
    wrapped = wrapper.fill(text=string)

    return wrapped
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print (result)