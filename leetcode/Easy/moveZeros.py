nums=[0,1,0,3,12]
leng=len(nums)
temp=0
n=leng
while(n>0):
    for i in range(0,leng-1):
        if nums[i]==0:
            temp=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=temp
        n=n-1

print(nums)
