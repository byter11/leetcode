class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int j=0;
        int n = students.size();
        for(int i=0; i<n; i++) {
            int leaves = 0;
            while(students[j] != sandwiches[i]) {
                if(students[j] != 2) {
                    leaves++;
                    if (leaves == n-i) return n-i;
                }
                j = (j + 1)%n;
            }
            students[j] = 2;
        }

        return 0;
    }
};