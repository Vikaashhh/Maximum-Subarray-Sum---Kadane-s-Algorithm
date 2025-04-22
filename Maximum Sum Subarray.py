class Solution:
    def maxSubArraySum(self, arr):
        # Initial max_sum and current_sum ko pehle element se start karte hain
        max_sum = curr_sum = arr[0]

        # Array ke second element se start karke loop chalayenge
        for i in range(1, len(arr)):
            # Ya toh current element le lo ya fir current_sum mein add karo
            curr_sum = max(arr[i], curr_sum + arr[i])
            
            # Har step pe max_sum ko update karo agar current_sum bada ho
            max_sum = max(max_sum, curr_sum)

        return max_sum
    

# Driver Code
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    sol = Solution()
    print("Maximum subarray sum:", sol.maxSubArraySum(arr))