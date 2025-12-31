
# Online Python - IDE, Editor, Compiler, Interpreter


def nextPermutation(ind,nums,ans) -> None:
    l = len(nums)
    if ind == l:
        ans.append(nums[:])
        return


    for i in range(ind,l):
        nums[i], nums[ind] = nums[ind], nums[i]
        nextPermutation(ind+1, nums,ans)
        nums[i], nums[ind] = nums[ind], nums[i]
    return ans
    
    
        
def main():
    nums = [1,2,3]
    ans = []
    print(nextPermutation(0,nums,ans))
main()