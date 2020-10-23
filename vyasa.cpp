#include<iostream>

using namespace std;

int main(){
	int n =0;
	int prv=0;
	int arr[100000],arr1[100000];
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	int j=0;
	for(int i=0;i<n;i++){
		cin>>arr1[i];
		for(j=n-1;j>=0;j--){
			if (arr1[i]==arr[j]){
				arr[j]=-1;
				cout<<j+1-prv<<" ";
				prv=j+1;
				break;
			}
			else if(arr[j]==-1){
				cout<<0<<' ';
				break;
			}}
	}
return 0;
	}
