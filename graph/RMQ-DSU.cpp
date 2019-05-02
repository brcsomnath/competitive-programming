/**
Offline RMQ (range minimum query) in O(α(n)) on average / Arpa's trick
We are given an array a[] and we have to compute some minima in given segments of the array.

The idea to solve this problem with DSU is the following: We will iterate over the array and 
when we are at the ith element we will answer all queries (L, R) with R == i. 
To do this efficiently we will keep a DSU using the first i elements with the following structure: 
the parent of an element is the next smaller element to the right of it.
Then using this structure the answer to a query will be the a[find_set(L)], 
the smallest number to the right of L.
**/

struct Query {
    int L, R, idx;
};

vector<int> answer;
vector<vector<Query>> container;

stack<int> s;
for (int i = 0; i < n; i++) {
    while (!s.empty() && a[s.top()] > a[i]) {
        parent[s.top()] = i;
        s.pop();
    }
    s.push(i);
    for (Query q : container[i]) {
        answer[q.idx] = a[find_set(q.L)];
    }
}
