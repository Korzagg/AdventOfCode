nums = ""
with open('input','r') as file:
    nums = file.read()

step = len(nums)//2
print(sum([int(nums[i]) if nums[i] == nums[(i+step)%len(nums)] else 0 for i in range(len(nums))]))