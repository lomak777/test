file_name=input('File name:')
nums=[]
r=open(file_name)
for i in r:
    nums.append(i)
r.close()
nums[:]=map(int,nums)

list.sort(nums)
h=len(nums)
g=round(h/2)
x=0
for i in nums:
    if i>nums[g-1]:
        x=x+(i-nums[g-1])
    else:
        x=x+(nums[g-1]-i)
print (x)        


