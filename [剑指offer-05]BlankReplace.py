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