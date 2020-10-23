
#include<iostream>
using namespace std;
int main()
{
    int t=0,s,arr[1000],sum=0,x,len=INT_MAX,count;
    cin>>t;
    while(t--){
		len=INT_MAX;
		cin>>s;
		cin>>x;
		for (int i=0;i<s;i++){
			cin>>arr[i];
		}
		for (int i=0;i<s;i++)
		{    
			sum=0;
			count=0;
			for (int j=i;j<s;j++){
				sum=sum+arr[j];
				count++;
				if (sum>=x && len>count)
				{
				   len=count;
					}
				
				}
			
			}
			if (len!=INT_MAX)
			cout<<len<<endl;
			else
			cout<<0<<endl;
			
	}
			
    return 0;
}
