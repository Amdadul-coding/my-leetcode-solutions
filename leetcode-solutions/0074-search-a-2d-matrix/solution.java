class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int foundrow = -1;
        for(int i = 0; i < matrix.length - 1; i++){
            if(matrix[i][0] < target && matrix[i+1][0] > target){
                foundrow = i;
                break;
            }
            else if(matrix[i][0] == target){
                return true;
            }
        }
        if(foundrow == -1){
            foundrow = matrix.length - 1;
        }
        for(int i = 0; i < matrix[foundrow].length; i++){
            if(matrix[foundrow][i] == target){
                return true;
            }
        }
        return false;
    }
}
