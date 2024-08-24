class Solution {
    public String longestPalindrome(String s) {
                if (s == null || s.length() < 1) return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);     // Odd length palindromes
            int len2 = expandAroundCenter(s, i, i + 1); // Even length palindromes
            int len = Math.max(len1, len2);
            
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
        // if(s.length() < 1 || s == null){
        //     return "";
        // }
        // if(s.length() == 1){
        //     return s;
        // }
        // String longest = "";
        // int middle = (s.length()/2);
        // System.out.print(middle);
        // if(s.length() % 2 == 0){
        //     if(s.charAt(middle - 1) == s.charAt(middle)){
        //         longest = s.substring(middle - 1, middle + 1);
        //     }
        // }
        // for(int i = 0; i <= middle; i++){
        //     if(s.length()%2 != 0){
        //         int right = middle + i;
        //         int left = middle - i;
        //         if(s.charAt(right) == s.charAt(left)){
        //             String idk = s.substring(middle - i, middle + i + 1);
        //             System.out.print(idk);
        //             if(idk.length() > longest.length()){
        //             longest = idk;
        //             }
        //         }
        //     }
        //     else{
        //         if(s.length() == 2 & s.charAt(0) != s.charAt(1)){
        //             return s.substring(0,1);
        //         }
        //     }
        // }
        // return longest;
    }
}
