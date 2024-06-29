class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> total;
        for(int i = 0; i < nums1.size(); i++){
            total.push_back(nums1[i]);
        }
        for(int i = 0; i < nums2.size(); i++){
            total.push_back(nums2[i]);
        }
        sort(total.begin(), total.end());
        int size = total.size();
        if(size%2 == 1){
            return static_cast<double> (total[size/2]);
        }
        else{
            int median1 = total[size/2];
            int median2 = total[size/2 - 1];
            return (static_cast<double>(median1) + static_cast<double>(median2)) / 2.0;
        }
    }
};
