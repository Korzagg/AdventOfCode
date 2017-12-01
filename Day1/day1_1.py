nums = ""
with open('input','r') as file:
    nums = file.read()
print(sum([int(nums[i]) if nums[i] == nums[i+1] else 0 for i in range(len(nums)-1)]) + int(nums[0]) if nums[0] == nums[-1] else 0)
