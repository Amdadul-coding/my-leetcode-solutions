class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlength = 0;
        for(int i = 0; i < s.length(); i ++){
            string character;
            character = character + s[i];
            for(int j = i + 1; j < s.length(); j++){
                if(character.find(s[j], 0) != string::npos){
                    break;
                }
                character = character + s[j];
            }
            // length = length + character.length();
            if(character.length() > maxlength){
                maxlength = character.length();
            }
        }
        return maxlength;
    }
};
