import java.io.*;

public class Main {

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        String n1 = input[0].trim(); // 첫 번째 숫자
        String n2 = input[1].trim(); // 두 번째 숫자

        // "0"인 경우 바로 처리
        if (n1.equals("0") || n2.equals("0")) {
            System.out.println("0");
            return;
        }
        // 결과 계산
        long sum = 0;

        // A의 각 자리수와 B의 각 자리수를 곱한 값의 합 구하기
        for (int i = 0; i < n1.length(); i++) {
            int digitA = n1.charAt(i) - '0'; // A의 i번째 자리 숫자
            for (int j = 0; j < n2.length(); j++) {
                int digitB = n2.charAt(j) - '0'; // B의 j번째 자리 숫자
                sum += (long) digitA * digitB; // 각 자리수를 곱하고 합산
            }
        }

        System.out.println(sum);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}