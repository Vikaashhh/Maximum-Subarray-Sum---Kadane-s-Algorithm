# 💡 Day-10: Maximum Sum Subarray — Kadane's Algorithm

On Day-10 of the #gfg160 Challenge, I implemented one of the most efficient algorithms in dynamic programming — **Kadane’s Algorithm**. The goal is to find the **maximum sum of a contiguous subarray** within a 1D array of numbers.

---

## 📌 Problem Statement

Given an integer array `arr`, find the contiguous subarray (containing at least one number) which has the **largest sum** and return its sum.

---

## 🔍 Intuition Behind Kadane’s Algorithm

Instead of checking all subarrays (which takes O(n²)), we use a greedy approach:
- At each index, decide whether to start a new subarray at the current element or continue with the existing subarray.
- Keep track of the **maximum sum so far** and update it when needed.

---

## 🧠 Approach & Explanation

1. Initialize:
   - `curr_sum` = first element
   - `max_sum` = first element
2. Traverse from the second element:
   - At each index `i`:  
     `curr_sum = max(arr[i], curr_sum + arr[i])`  
     `max_sum = max(max_sum, curr_sum)`
3. Return `max_sum`

---

## 📊 Time & Space Complexity
- Time Complexity: O(n)

- Space Complexity: O(1)

---

## Sample Input/Output
- Input:- Enter array elements: -2 -3 4 -1 -2 1 5 -3
- Output:- Maximum subarray sum: 7

---

##  Challenge Tag
#gfg160 #geekstreak2025 #Day10
---

## ✨ Author
Curated by Vikash Joshi — Front-End Developer, UI/UX Designer, and DSA Enthusiast 🌟

