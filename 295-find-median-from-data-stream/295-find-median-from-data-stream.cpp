class MedianFinder {
public:
    multiset<int> mset;
    multiset<int>::iterator miditer;     ///Keeps track of middle iterator of the multiset, if the list is even the iterator points to first element of the mid
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        mset.insert(num);
        if(mset.size() == 1){
            miditer = mset.begin();      //Initially only one element 
        }else if(mset.size()%2 == 0 && num < *miditer){   //Decrement the iterator only if after insertion of "num" the multiset size becomes even and the number is inserted before previous mid, since the list is even make iterator point to first element
                miditer--;    
        }else if(mset.size()%2 != 0 && num >= *miditer){  //Increment the iterator only if after insertion of "num" the multiset size becomes odd and the number is inserted after previous mid
                miditer++;
        }
    }
    
    double findMedian() {
        if(mset.size()%2 == 0){
            double ans = (*miditer + *(++miditer))/2.0;
            --miditer;
            return ans;
        }else{
            return *miditer;
        }     
    }
};