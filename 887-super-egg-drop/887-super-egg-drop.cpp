class Solution {
public:
    int superEggDrop(int K, int N) {
        vector<int> floors(K,1);

        int counter = 2;
        while (N > 1) {
            for (int j = K - 1; j > 0; --j) floors[j] += floors[j-1] + 1; 
            floors[0] = counter;

            if (floors[K-1] >= N) return counter;
            ++counter;
        }

        return counter-1;
    }
};