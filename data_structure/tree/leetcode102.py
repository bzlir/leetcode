class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                out = q.popleft()
        
                if out:
                    q.append(out.left)
                    q.append(out.right)
                    level.append(out.val)
            if level:
                res.append(level)
        return res