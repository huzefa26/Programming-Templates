__author__ = 'huzef'
// define MAX to be a really big number

int tree[MAX], N;

// initialises a tree for n data entries
int init( int n )
{
  N = 1;
  while( N < n ) N *= 2;
  for( int i = 1; i < N + n; i++ ) tree[i] = 0;
}

// increments a[k] by val for all k between i and j, inclusive
void range_increment( int i, int j, int val )
{
  for( i += N, j += N; i <= j; i = ( i + 1 ) / 2, j = ( j - 1 ) / 2 )
  {
    if( i % 2 == 1 ) tree[i] += val;
    if( j % 2 == 0 ) tree[j] += val;
  }
}

// compute a[i]
int query( int i )
{
  int ans = 0;
  for( int j = i + N; j; j /= 2 ) ans += tree[j];
  return ans;
}