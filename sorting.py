import random
import time
import sys

l = []
listSize = 0

#If command line arg then use it, else prompt
if len(sys.argv) > 1:
    listSize = int(sys.argv[1])
else:
    listSize = int(input("How many values in list, boss? "))  
for x in range(listSize ):
  l.append (random.randint(1,10000) )

py_sort = list(l)
access = 0
start_t = time.time()

#This is where you sort l
#For example: Check out this slow garbage
for i in range(len(l)):
  for j in range(len(l)):
    if l[i] < l[j]:
          other = l[i]
          l[i] = l[j]
          l[j] = other
          #keep track of list accesses
          access = access+1
#End custom sort of l
end_t = time.time()

#Check if custom list l is sorted
for x in range(len(l) - 1):
      if  (l[x] > l[x+1] ):
            raise Exception("List is not sorted!")

#Time took to custom sort:
sort_1_t = (end_t - start_t)

#block to sort using custom sort
start_t = time.time()
py_sort.sort()
end_t = time.time()
sort_2_t = (end_t - start_t)

print ("My Time  : %.4f with %d list accesses. \nOtherTime: %.04f" % (sort_1_t*1000, access, sort_2_t*1000))