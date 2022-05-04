# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution
# -----------------------------------------------------------------------------
strs = ['flower', 'flow', 'flight']
# strs = ['dog', 'racecar', 'car']

strs.sort(key = lambda i : len(i))

res = []
first = strs[0]

# starting from after first word
for i in strs[1:]:
    letter_counter = 0
    temp_list = []
    temp = ''
    # go thru each letter
    for j in i:
        # if counter goes out of bounce or the letters are not the same, we can just stop
            if letter_counter +1 > len(first) or j != first[letter_counter] :
                break
            else:
                # add to list, and move up on our letter counter
                temp_list.append(j)
                letter_counter +=1
    # join all the letters in the temp list and add to our result list
    temp = "".join(temp_list)
    res.append(temp)
# we sort again for the shortest in length and then that'll be our result
res.sort(key = lambda i : len(i))

result = res[0]

print("final result", result)

# flaw with solution: don't know if the shortest after sorting is correct, 
# since we put all the characters from our search into our list. 
# another issue is that we're pulling word first, then check each letter in word. 
# better solution would be pull shortest word, pull letter, then check thru each word
# 
# 
# 
# -----------------------------------------------------------------------------
#  Attempt: #2                start of solution
# -----------------------------------------------------------------------------



strs.sort(key = lambda i : len(i)) #time complexity of sorting all, O(nlogn)

res = []

for i in range(len(strs[0])):
    for j in strs:
        # if 
        if strs[0][i] != j[i]:
            print("end: ", res)
            break
    res += strs[0][i]

print("end", res)


    





