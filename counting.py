array = [1,2,3,4,5,2,5,1,8,9,1]
index_array=[0]*len(array)
ans=[0]*len(array)
for index in range (0, len(array)-1): index_array[array[index]]+=1
for index in range (1, len(index_array)): index_array[index]+=index_array[index-1]
for index in range (0, len(array)): 
    ans[index_array[array[index]]]=array[index]
    index_array[array[index]]-=1
print(ans)