class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> finally;
        int coun = 0;
        for(int i = 0; i < nums.size(); i++){
            int cnt = count(finally.begin(), finally.end(), nums[i]);
            if(cnt == 0){
                finally.push_back(nums[i]);
                coun++;
            }
        }
        for(int j = 0; j < finally.size(); j++){
            nums[j] = finally[j];
        }
        return coun;
    }
};
