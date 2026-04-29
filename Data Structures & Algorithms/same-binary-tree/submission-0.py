# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue1=deque([p])
        queue2=deque([q])

        while queue1 and queue2:
            e1=queue1.popleft()
            e2=queue2.popleft()
            if not e1 and not e2:
                continue
            if not e1 or not e2:
                return False

            if e1.val!=e2.val:
                return False
            
            queue1.append(e1.left)
            queue1.append(e1.right)
            queue2.append(e2.left)
            queue2.append(e2.right)
        return not queue1 and not queue2
