class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        int init_max = candies[0];

        List<Boolean> result = new ArrayList<Boolean>();

        // first loop to find initial maximum 
        for(int i = 1; i < n; i++) {
            if(candies[i] > init_max) {
                init_max = candies[i];
            }
        }

        // loop that adds extraCandies
        for(int i = 0; i < n; i++) {
            if (candies[i] + extraCandies >= init_max) {
                result.add(true); 
            } else {
                result.add(false); 
            }
        }

        return result; 
    }
}
