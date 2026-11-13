from itertools import groupby

text = "yyyyaaabbddffyyyghhhhhhssss"
#result = "".join(f"{char}{len(list(group))}" for char, group in groupby(text))
#print(result)  # Output: a3b2d2f2g1h6s4
text_sort = "".join(sorted(text))

print(text_sort)
# for char,group in groupby(text_sort):
#     print(char,list(group)) giri


res = "$".join(f"{char}{len(list(group))}" for char,group in groupby(text_sort))

print(res)