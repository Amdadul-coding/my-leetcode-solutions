class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> returning;
        for(int i = 0; i < nums.size(); i++){
            int current = nums[i];
            for(int j = 0; j < nums.size(); j++){
                if(nums[i] + nums[j] == target && i != j){
                    returning.push_back(i);
                    returning.push_back(j);
                    return returning;
                }
            }
        }
        return returning;
    }
};
