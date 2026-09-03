class Solution:
    def trap(self, height: List[int]) -> int:
        last_min_height = 0
        curr_fill = 0
        total_trapped = 0
        l,r = 0,len(height) -1
        while(l+1<len(height) and height[l] < height[l+1]):
            l+=1
        while(r-1 > 0 and height[r] < height[r-1]):
            r-=1
        while(l<r):
            if(height[l]<=height[r]):
                last_min_height = height[l]
                l+=1
                while(height[l]<last_min_height and l<r):
                    curr_fill += last_min_height - height[l]
                    l+=1
                total_trapped += curr_fill
                curr_fill = 0
            else:
                last_min_height = height[r]
                r-=1
                while(height[r]<last_min_height and l<r):
                    curr_fill += last_min_height - height[r]
                    r-=1
                total_trapped += curr_fill
                curr_fill = 0
            
        return total_trapped 