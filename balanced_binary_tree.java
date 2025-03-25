class Solution {
    public boolean isBalanced(TreeNode root) {
        return height(root) != -1;
    }

    private int height(TreeNode node){
        if(node == null){
            return 0;
        }

        int leftheight = height(node.left);
        if(leftheight == -1){
            return -1;
        }

        int rightheight = height(node.right);
        if(rightheight == -1){
            return -1;
        }

        if(Math.abs(leftheight - rightheight) > 1){
            return -1;
        }

        return Math.max(leftheight, rightheight) + 1;
    }
}
