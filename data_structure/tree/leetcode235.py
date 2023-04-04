class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right # 都在right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur