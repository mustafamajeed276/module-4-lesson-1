l = [5, 4, 3, 8, 6, 5]
print("orignal list is ", l)
count = 0
for i in l:
    count += i
avg = count/len(l)
print("sum = ", count)
print("average = ", avg)
l.sort()
print("smallest element is ", l[0])
print("largest element is ", l[-1])