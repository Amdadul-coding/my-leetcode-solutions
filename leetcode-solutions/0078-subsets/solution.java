class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> sol = new ArrayList<>();
        sol.add(new ArrayList<>()); // Start with the empty set
        
        for (int num : nums) {
            int n = sol.size();
            for (int i = 0; i < n; i++) {
                List<Integer> newSubset = new ArrayList<>(sol.get(i));
                newSubset.add(num);
                sol.add(newSubset);
            }
        }
        
        return sol;
    //     List<List<Integer>> sol = new ArrayList<>();
    //     sol.add(new ArrayList<>());
    //     List<Integer> full = new ArrayList<Integer>();
    //     for(int i = 0; i < nums.length; i++){
    //         full.add(nums[i]);
    //         List<Integer> singleElementList = new ArrayList<>();
    //         singleElementList.add(nums[i]);
    //         sol.add(singleElementList);
    //         for(int j = 0; j < nums.length; j++){
    //             if(nums[i] != nums[j]){
    //                 if(sol.contains([i,j])){

    //                 }
    //                 List<Integer> twoitem = new ArrayList<>();
    //                 twoitem.add(nums[i]);
    //                 twoitem.add(nums[j]);
    //                 sol.add(twoitem);
    //             }
    //         }
    //     }
    //     if(nums.length != 1){
    //         sol.add(full);
    //     }
    //     return sol;
    }
}
