package week2.day1;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BRSQ {

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(String s) {
            try {
                br = new BufferedReader(new FileReader(s));
            } catch (FileNotFoundException e) {
                // TODO Auto-generated catch block
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

    static class SegmentTree{

        int n ;
        long[] sum;

        public SegmentTree(int n){
            this.n = n;
            this.sum = new long[4 * n];
        }
        // every tree node is integer
        // node i -> sum[i]
        // left child is 2 * i
        //right childe is 2 * i +1
        // root is 1
        // 1 -> 2, 3
        // 2 -> 4, 5
        // 3 -> 6, 7

        // n = 3
        // 1 -> [0, 2]
        // 2 -> [0, 1]
        // 3 -> [2, 2]
        // 4 -> [0, 0]
        // 5 -> [1, 1]

        // if x -> [a, b]
        // then 2 * x -> [a, (a+b)/2]
        // and 2 * x +1 -> [(a+b)/2, b]

        public void modify(int i, long x){
            internalModify(i, x, 0, n - 1, 1);
        }

        private void internalModify(int i, long x, int a, int b, int node){
            // [a,b] corresponds to $node
            // case 1: no intersection
            if( a == b){
                sum[node] = x;
                return;
            }
            int middle = (a + b)/2;
            if(i <= middle){
                // go recursively to the left child
                internalModify(i, x, a, middle, node * 2);
            }else{
                internalModify(i, x, middle + 1, b, node * 2 + 1);
            }
            // noe sum[node] is no longer valid, update its value
            sum[node] = sum[node * 2] + sum[node * 2 + 1];
        }

        long sum(int l, int r){
            return internalSum(l, r, 0, n - 1, 1);
        }

        private long internalSum(int l, int r, int a, int b, int node){
            // [a,b] corresponds to $node
            // case 1: no intersection
            if( l > b || a > r ){
                return 0;
            }
            // case 2: [a,b] is a subset of [l ,r]
            if(l <= a && b <= r){
                return sum[node];
            }
            return internalSum(l, r, a, (a + b)/2, node * 2) +
                    internalSum(l, r, (a + b)/2 + 1, b, node * 2 + 1);
        }
    }

    public static void solve(int testNumber, FastScanner in, PrintStream out){
        int n = in.nextInt();
        String token = "";

        SegmentTree tree = new SegmentTree(n);
        for (int i = 0; i<n; i++){
            tree.modify(i, in.nextLong());
        }
        token = in.nextToken();
        while(token != null){
            String op = token;
            if(op.equals("sum")){
                int l = in.nextInt() - 1, r = in.nextInt() - 1;
                out.println(tree.sum(l, r));
            }else{
                int i = in.nextInt() - 1;
                long x = in.nextLong();
                tree.modify(i, x);
            }
            token = in.nextToken();
        }
    }

    public static void main(String[] args){
        FastScanner fs = new FastScanner();
        solve(0, fs, System.out);
    }
}
