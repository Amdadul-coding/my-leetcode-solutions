class Solution {
    public void setZeroes(int[][] matrix) {
        List<Integer> idki = new ArrayList<Integer>();
        List<Integer> idkj = new ArrayList<Integer>();
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length; j++){
                System.out.print(matrix[i][j]);
                if(matrix[i][j] == 0){
                  idki.add(i);
                  idkj.add(j);  
                }
            }
        }
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length; j++){
                if(idki.contains(i) == true || idkj.contains(j) == true){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
