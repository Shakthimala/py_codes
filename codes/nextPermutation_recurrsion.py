
# Online Python - IDE, Editor, Compiler, Interpreter


def nextPermutation(nums) -> None:
    n = len(nums)
    flag = [0]*n
    ds = []
    ans = []
    def recur(nums, flag, ds, ans):
        if len(ds) == n:
            ans.append(ds[:])
            return

        for i in range(n):
            if flag[i] == 0:
                flag[i] = 1
                ds.append(nums[i])
                recur(nums, flag, ds, ans)
                ds.pop()
                flag[i] = 0
    recur(nums, flag, ds, ans)
    return ans
        
def main():
    nums = [1,2,3]
    print(nextPermutation(nums))
main()