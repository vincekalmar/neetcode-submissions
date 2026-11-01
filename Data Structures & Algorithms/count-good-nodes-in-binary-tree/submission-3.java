/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }

    public int dfs(TreeNode root, int max_val) {
        if (root == null) return 0;

        int res = (root.val >= max_val) ? 1 : 0;
        max_val = Math.max(max_val, root.val);

        res += dfs(root.left, max_val);
        res += dfs(root.right, max_val);

        return res;
    }
}
