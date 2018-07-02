class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        
        [0,0,2,2]
        [1,1,3,3]
        """
        x_int = False
        y_int = False
        
        low_x_bound = max(rec1[0], rec2[0])
        high_x_bound = min(rec1[2], rec2[2])
        low_y_bound = max(rec1[1], rec2[1])
        high_y_bound = min(rec1[3], rec2[3])
        
        # should include the endpoint so +1, this isn't index
        for i in xrange(low_x_bound, high_x_bound+1): 
            if i > rec2[0] and i < rec2[2]:
                x_int = True
                break
        
        for j in xrange(low_y_bound, high_y_bound+1):
            if j > rec2[1] and j < rec2[3]:
                y_int = True
                break
                
        return x_int and y_int
