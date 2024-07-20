class Solution:
    def firstUniqChar(self, s: str) -> int:
        x1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in s:
            if(i in x1):
                x2 = 0
                for j in s:
                    if(j == i):
                        x2 = x2 + 1
                    elif(x2 >= 2):
                        break
                if(x2 == 1):
                    return s.index(i)
                x1.remove(i)             
        return -1
