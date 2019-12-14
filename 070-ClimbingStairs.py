class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize a list to store "default" cases 0, 1, and 2
        stored_list= [0, 1, 2]           

        # Iterate through all numbers up to n + 1
        # We look at n + 1 to account for the case were n = 3 
        for i in range(3, n + 1):
            # Calculate the possible paths to stair i using the stored paths and append to list
            possible_paths = stored_list[i - 1] + stored_list[i - 2]
            stored_list.append(possible_paths)
        return stored_list[n]
