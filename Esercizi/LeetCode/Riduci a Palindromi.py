class Solution:
    def longestPalindrome(s: str):
        sPalindroma = ''        
        for i in range(len(s)//2):    
            if(s[i]==s[-i-1]):
                sPalindroma += s[i]
            else:
                sPalindroma=''
                
        tempS = sPalindroma[::-1] 
        if(len(s)%2 == 1): 
            print("dispari " + s[len(s)//2])
            sPalindroma += s[len(s)//2]
        return sPalindroma + tempS