#include <iostream>
#include <cstdio>
#define ll long long
using namespace std;
int a[100050];
int d[100050];
int vis[100050];
ll sum[100050];
int fa[100050];
ll res[100050];
int n;
int search(int x) {
	if (x > n || x <= 0) return -1;
	return x == fa[x] ? x : fa[x] = search(fa[x]);
}
int main()
{
	int i, j, temp;
	ll max = 0;
	cin >> n;
	for (i = 1; i <= n; i++) scanf("%d", &a[i]);
	for (i = n; i >= 1; i--) scanf("%d", &d[i]);
	for (i = 1; i <=n; i++) {
		fa[i] = i;
		vis[i] = 0;
		sum[i] = a[i];
	}
	for (i = 1; i < n; i++) {
		j = d[i];
		vis[j] = 1;
		int r = search(j + 1);
		int l = search(j - 1);
		if ((l == -1 || vis[l] == 0) && (r == -1 || vis[r] == 0)) {//There are no accessed elements at both ends, no operation
		}
		else {
			if (r != -1 && vis[r] != 0) {
				if (l == -1 || vis[l] == 0) {
					fa[j] = r;
					sum[r] += sum[j];
				}
				else {
					fa[l] = r;
					fa[j] = r;
					sum[r] += sum[l] + sum[j];
				}
			}
			else {
				fa[j] = l;
				sum[l] += sum[j];
			}
		}
		temp = search(j);
		if (sum[temp] > max)
			max = sum[temp];
		res[n -1- i] = max;
	}
	for (i = 0; i < n; i++)
		cout << res[i] << endl;
	return 0;
}