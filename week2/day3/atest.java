package week2.day3;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class atest {
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(String s) {
            try {
                br = new BufferedReader(new FileReader(s));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String nextToken() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException | NullPointerException e) {
                    st = null;
                    return null;
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(nextToken());
        }

        long nextLong() {
            return Long.parseLong(nextToken());
        }

        double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }

    public double Prim(double[][] G, int V) {
        double answer = 0;
        int INF = 9999999;

        int no_edge;

        boolean[] selected = new boolean[V];

        Arrays.fill(selected, false);

        no_edge = 0;

        selected[0] = true;

        while (no_edge < V - 1) {

            double min = INF;
            int x = 0;
            int y = 0;

            for (int i = 0; i < V; i++) {
                if (selected[i]) {
                    for (int j = 0; j < V; j++) {
                        if (!selected[j] && G[i][j] != 0) {
                            if (min > G[i][j]) {
                                min = G[i][j];
                                x = i;
                                y = j;
                            }
                        }
                    }
                }
            }

            answer += G[x][y];
            selected[y] = true;
            no_edge++;
        }
        return answer;
    }

    public static boolean isDouble(Double d_num) {
        if ((d_num % 1) == 0) {
            return false;
        } else {
            return true;
        }
    }

    public static double euclidean_distance(int[] v1, int[] v2){
        return Math.sqrt( Math.pow((v2[0] + v1[0]), 2) + Math.pow((v2[1] + v1[1]), 2) );
    }

    public static void solve(int testNumber, FastScanner in, PrintStream out){
        int y = 0, x = 0;
        int V = in.nextInt();
        String token = "";

        int[][] coords = new int[V][2];
        for(int i = 0;  i < V; i++) {
            for(int j = 0; j < 2; j++){
                coords[i][j] = in.nextInt();
            }
        }

        double[][] adjacency_matrix = new double[V][V];
        for(int actual_vertex = 0; actual_vertex < V; actual_vertex++){
            for(int next_vertex = 0; next_vertex < V; next_vertex++){
                if(actual_vertex != next_vertex){
                    adjacency_matrix[actual_vertex][next_vertex] = euclidean_distance(coords[actual_vertex], coords[next_vertex]);
                    y++;
                } else{
                    adjacency_matrix[actual_vertex][next_vertex] = 0;
                }
            }
            y = 0;
            x ++;
        }

        atest g = new atest();

        double answer = g.Prim(adjacency_matrix, V);

        if(isDouble(answer)){
            out.println(answer);
        }
        else{
            out.println((int) answer);
        }
    }

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        solve(0, fs, System.out);
    }
}
