nums = [1,2,3,4,5,6,7,8,9]
target = int(input("enter the number: "))

for i in range(len(nums)):
    for j in range(i+1,(len(nums))):
        if nums[i]+nums[j]==target:
            print(f"pair found : {nums[i],nums[j]}")