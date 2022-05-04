target = 10
nums = [2, 5, 7, 8]

hashmap = {}

for i in range(len(nums)):
    complement = target - nums[i]
    print('complement',complement)
    if complement in hashmap:
        print("nums[i]", i)
        print([hashmap[complement], i])
    hashmap[nums[i]] = i
    print('hash', hashmap)
