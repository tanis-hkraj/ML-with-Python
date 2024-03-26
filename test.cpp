#include <bits/stdc++.h>

using namespace std;



/*
 * Complete the 'countPalindromes' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int countPalindromes(string s) {
    int count=0;
    for(int i=0;i<s.size();i++){
        string s1="";
        for(int j=i;j<s.size();j++){
            s1+=s[j];
            string s2=s1;
            reverse(s1.begin(),s1.end());
            if(s1==s2){
                cout<<s2<<endl;
                count++;
            }
            s1=s2;
        }
    }
    return count;
    
    
}

int main()
{
    

    int result = countPalindromes("aaa");

    cout << result << "\n";


    return 0;
}
