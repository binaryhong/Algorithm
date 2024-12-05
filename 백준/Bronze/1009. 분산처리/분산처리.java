import java.io.*;

public class Main {
    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 테스트 케이스 수 입력

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);

            int result = 1;
            for (int j = 0; j < b; j++) {
                result = (result * a) % 10;
            }

            if (result == 0) {
                System.out.println("10");
            } else {
                System.out.println(result);
            }
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}