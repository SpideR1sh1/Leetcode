class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        
        /*
        APPROACH
        1. Sort all the points based on the starting points and ending points
        2. if encounter a building (starting point) add to the multiset the height 
        3. If leaving a building (ending point) remove the height
        4. after each addition and removal if the max height changes, calculate the change in the answer
        
        TC :- O(NlogN)
        */
        
        vector<vector<int> > res;
        vector<pair<int, int> > points; // x coordinate, height of building start and ends
                                        // store -h for start point and +h for end point
        
        for(auto &a : buildings)
        {
            points.push_back({a[0],-a[2]});
            points.push_back({a[1], a[2]});
        }
        
        sort(points.begin(), points.end()); // sort based on the x coordinate
        multiset<int> m = {0}; // keep a building of height 0 for reference
        int prev=0;
        int curr=0;
        for(auto &p : points)
        {
            if(p.second < 0)
            {
                // add it building height to the DS
                m.insert(-p.second);
            }
            else
            {
                //remove from the buildong
                m.erase(m.find(p.second));
            }
            curr = *m.rbegin(); // current max after building removal
            if(prev!=curr)
            {
                prev = curr;
                res.push_back({p.first,curr});
            }
        }
        return res;
        
    }
};