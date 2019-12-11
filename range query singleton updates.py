__author__ = 'huzef'
// define MAX to be some really big number

int tree[MAX], N;

// initialises a tree for n data entries
int init( int n )
{
  N = 1;
  while( N < n ) N *= 2;
  for( int i = 1; i < N + n; i++ ) tree[i] = 0;
}

// compute the product a[i] + a[i+1] + ... + a[j]
int range_sum( int i, int j )
{
  int ans = 1;
  for( i += N, j += N; i <= j; i = ( i + 1 ) / 2, j = ( j - 1 ) / 2 )
  {
    if( i % 2 == 1 ) ans += tree[i];
    if( j % 2 == 0 ) ans += tree[j];
  }
  return ans;
}

// set a[i] = val
void update( int i, int val )
{
  int diff = val - tree[i+N];
  for( int j = i + N; j; j /= 2 ) tree[j] += diff;
}