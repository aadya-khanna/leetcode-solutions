class Solution {
    public String mergeAlternately(String word1, String word2) {
        String builder = ""; 

        int smaller_len = Math.min(word1.length(), word2.length());

        for(int i = 0; i <= smaller_len; i++) {
            if(word1.length() == i) {
                builder += word2.substring(i); 
            } else if (word2.length() == i) {
                builder += word1.substring(i);  
            } else {
                builder+= word1.charAt(i); 
                builder+=word2.charAt(i); 
            }
        }

        return builder;
    }
}


