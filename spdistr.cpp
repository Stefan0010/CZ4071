#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <cstring>

#define ull unsigned long long
#define ll long long
#define ul unsigned long
#define vi vector<int>
#define vll vector<long long>
#define pb push_back
#define pii pair<int, int>
#define pll pair<long long, long long>
#define mp make_pair
#define pq priority_queue
#define fi first
#define se second

using namespace std;

int num_nodes = 0;
int mapper[2000001];
vi neighbours[2000001];
int dist[2000001];
int cum_dist[2000001];
const int MY_INF = 0x7F7F7F7F;
int max_dist;

void bfs(const int &start_node) {
	queue<int> q;
	q.push(start_node);
	dist[start_node] = 0;
	while(!q.empty()) {
		int u = q.front();
		q.pop();
		for(int i = 0, size = neighbours[u].size(); i < size; ++i) {
			int v = neighbours[u][i];
			if(dist[u] + 1 < dist[v]) {
				dist[v] = dist[u] + 1;
				q.push(v);
			}
		}
	}
}

int main(int argc, char* argv[]) {
	if(argc != 3) {
		fprintf(stderr, "Usage: %s IN_FILE OUT_FILE\n", argv[0]);
		return EXIT_FAILURE;
	}
	
	FILE * fin = fopen(argv[1], "r");
	
	char buffer[256];
	memset(mapper, 0xFF, sizeof mapper);
	while(fgets(buffer, 256, fin)) {
		char *buffer_ptr = buffer;
		while(isspace(*buffer_ptr)) ++buffer_ptr;
		if(*buffer_ptr == '#' || *buffer_ptr == '\0') continue;
		
		int u, v;
		sscanf(buffer_ptr, "%d%*c%d", &u, &v);
		if(mapper[u] == -1) mapper[u] = num_nodes++;
		if(mapper[v] == -1) mapper[v] = num_nodes++;
		
		neighbours[mapper[u]].pb(mapper[v]);
		neighbours[mapper[v]].pb(mapper[u]);
	}
	
	for(int start_node = 0; start_node < num_nodes; ++start_node) {
		memset(dist, 0x7F, sizeof dist);
		bfs(start_node);
		
		for(int u = 0; u < start_node; ++u) {
			if(dist[u] == MY_INF || u == start_node)
				continue;
			
			++cum_dist[dist[u]];
			max_dist = max(max_dist, dist[u]);
		}
		
		printf("Completed: %.6f%%\n", (float) (start_node + 1) / num_nodes * 100.);
	}
	
	FILE * fout = fopen(argv[2], "w");
	for(int d = 1; d <= max_dist; ++d) {
		fprintf(fout, "%d,%d\n", d, cum_dist[d]);
	}
	
	return 0;
}
