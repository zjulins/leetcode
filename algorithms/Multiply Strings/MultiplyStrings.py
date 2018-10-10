class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)
        rlt = dict()
        num3 = ''
        for i in range(l1):
            for j in range(l2):
                k = i+j
                cj = int(num1[i])*int(num2[j])
                if not k in rlt:
                    rlt[k] = 0
                rlt[k] += cj
        
        jw = 0
        for i in range(l1+l2-1):
            num = (rlt[i]+jw) % 10
            num3 = str(num)+num3
            jw = (rlt[i]+jw)/10
        num3 = str(jw)+num3
        while num3[0] == '0' and len(num3)>1:
            num3 = num3[1:]
        return num3
