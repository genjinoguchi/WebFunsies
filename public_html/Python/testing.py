d=[1, 2, 3]
d2=[4, 5, 6]

def perms(d1, d2):
    ans={}
    for each in d1:
        for nums in d2:
            ans[each+nums] = {each:nums}
    return ans
