# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].
```

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

## Approach

### Method 1: Hash Map (Optimal)
Use a hash map to store numbers we've seen along with their indices. For each number, check if `target - num` exists in the hash map.

**Algorithm:**
1. Create an empty hash map to store {number: index}
2. Iterate through the array
3. For each number, calculate complement = target - num
4. If complement exists in hash map, return [hash_map[complement], current_index]
5. Otherwise, add current number and its index to hash map
6. Continue until solution is found

**Time Complexity:** O(n) - Single pass through the array
**Space Complexity:** O(n) - Hash map can store up to n elements

### Method 2: Brute Force (Not Recommended)
Check every pair of numbers to see if they sum to target.

**Time Complexity:** O(n²) - Nested loops
**Space Complexity:** O(1) - No extra space needed

## Solution

See `solution.py` for implementation.

## Test Cases
```
Test Case 1: nums = [2,7,11,15], target = 9
Expected: [0,1]

Test Case 2: nums = [3,2,4], target = 6
Expected: [1,2]

Test Case 3: nums = [3,3], target = 6
Expected: [0,1]
```

## Notes
- This is a classic interview problem that demonstrates the hash map pattern
- The hash map approach trades space for time efficiency
- Edge case: Array with duplicate numbers is handled correctly

## Related Problems
- Three Sum
- Four Sum
- Two Sum II (Input Array Is Sorted)

## References
- [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)
