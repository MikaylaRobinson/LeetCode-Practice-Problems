class Solution:
    def climbStairs(self, n: int) -> int:
        stored_list= [0, 1, 2]           
        for i in range(3, n + 1):
            possible_paths = stored_list[i - 1] + stored_list[i - 2]
            stored_list.append(possible_paths)
        return stored_list[n]
