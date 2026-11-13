a = [0, 1, 0, 3, 12, 0, 5]
insert_pos = 0
for i in range(len(a)):
    if a[i] != 0:
        a[insert_pos], a[i] = a[i], a[insert_pos]
        insert_pos += 1
print(a)