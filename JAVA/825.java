class Solution {
    public int numFriendRequests(int[] ages) {
        int[] count = new int[121];
        for (int age: ages) count[age]++;
        int res = 0;
        for (int i = 0; i < 121; i++) {
            int countA = count[i];
            for (int j = 0; j < 121; j++) {
                int countB = count[j];
                if (i * 0.5 + 7 >= j) continue;
                if (i < j) continue;
                if (i < 100 && 100 < j) continue;
                res += countA * countB;
                if (i == j) {
                	res -= countA;
                }
            }
        }
        return res;
    }
}

#Runtime: 14 ms
#Your runtime beats 27.32 % of java submissions.