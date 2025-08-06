
# class Solution:
#     def isBalanced(self, s):
#         stack = []
#         opening = {'(', '{', '['}
#         closing_to_opening = {')': '(', '}': '{', ']': '['}

#         for char in s:
#             if char in opening:
#                 stack.append(char)
#             elif char in closing_to_opening:
#                 if not stack or stack[-1] != closing_to_opening[char]:
#                     return False
#                 stack.pop()
#             else:
#                 return False

#         return not stack


# print(Solution().isBalanced("()[]{}"))
# print(Solution().isBalanced("(]"))
# print(Solution().isBalanced("([)]"))
# print(Solution().isBalanced("{[]}"))
# print(Solution().isBalanced("{[()]}"))
# print(Solution().isBalanced("{[(])}"))
# print(Solution().isBalanced("{[()()]()}"))
