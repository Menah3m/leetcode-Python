# Name:BlankReplace
# Author:Yasu
# Time:2020/3/18


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_new = []

        for char in s:
            if char == ' ':
                list_new.append('%20')
            else:
                list_new.append(char)

        return ''.join(list_new)

#代码2
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res    