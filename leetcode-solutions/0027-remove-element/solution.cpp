class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector <int> idk;
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != val){
                idk.push_back(nums[i]);
                count++;
            }
        }
        nums = idk;
        return count;
    }
};
