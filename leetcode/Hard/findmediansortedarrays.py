nums1=[1,3]
nums2=[2,4]
nums1=(nums1+nums2)
nums1.sort()
if len(nums1)%2==0:
    i=len(nums1)//2
    j=i-1
    print("The median is (",nums1[j],"+",nums1[i],")/2 =",'%.1f' %((nums1[i]+nums1[j])/2))
else:
    print('The median is', '%.1f' % nums1[len(nums1)//2])
