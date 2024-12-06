import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

N(2 ≤ N ≤ 1,000)명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.
 */

public class Main {
    public void solution() throws java.io.IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

       // 첫 번째 줄에서 참여하는 사람 수 N을 입력받음
        int N = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        int sum = 0;
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            // 주사위 3개의 눈 값을 공백으로 분리
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);
            if ((a == b) & (a == c) & (b == c)){
                sum = a * 1000 + 10000;
            }
            else if (a == b & a!=c){
                sum = a * 100 + 1000;
            }
            else if (b == c & a!=c){
                sum = b * 100 + 1000;
            }
            else if (a == c & a!=b){
                sum = a * 100 + 1000;
            }
            else {
                sum = Math.max(a, Math.max(b, c)) * 100;
            }

            // 이 시점에서 sum에 해당 참가자의 상금이 계산됨
            // 이제 maxValue 갱신
            if (sum > maxValue) {
                maxValue = sum;
            }
        }
        System.out.println(maxValue);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}