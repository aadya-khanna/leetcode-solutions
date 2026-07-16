class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

    # create a dictionary

        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        
        arr = list(s)


        result = 0
        skip = False

        for cur in range(len(arr)):
            if (not skip) and cur == len(arr) - 1:
                result+=d.get(arr[cur])
                return result 

            if (not skip) and arr[cur] == "I":
                if arr[cur+1] == "V":
                    result+=4
                    skip = True
                    continue
                elif arr[cur+1] == "X":
                    result+=9
                    skip = True 
                    continue  
            elif (not skip) and arr[cur] == "X":
                if arr[cur+1] == "L":
                    result+=40
                    skip = True
                    continue
                elif arr[cur+1] == "C":
                    result+=90
                    skip = True
                    continue
            elif (not skip) and arr[cur] == "C":
                if arr[cur+1] == "D":
                    result+=400
                    skip = True
                    continue
                elif arr[cur+1] == "M":
                    result = result+900
                    skip = True
                    continue
            
            if not skip: 
                result+=d.get(arr[cur])
                print(str(result))
            
            skip = False
                

        return result


