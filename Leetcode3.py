class Solution(object):
   def maxSubArray(self, nums):  
      new = [0 for i in range(len(nums))]
      new[0] = nums[0]
    
      for i in range(1,len(nums)):     
        new[i] = new[i-1] + nums[i]
        if(new[i] < nums[i]):
            new[i] = nums[i]
      
      new.sort(reverse=True)  
      
      return new[0]
