import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String input = br.readLine();
            int num = Integer.parseInt(input);
            int sum = 0;
            if (num == 0) {
                break;
            }
            for (char c: input.toCharArray()){
                if (c=='0'){
                    sum += 4;
                }
                else if (c=='1'){
                    sum += 2;
                }
                else {
                    sum += 3;
                }
            }
            // 숫자 사이의 간격 (각 숫자 사이에 1cm 여백)
            int gap = (input.length() - 1);
            int border = 2;
            int totalLength = sum + gap + border;
            sb.append(totalLength).append("\n");
        }

        System.out.print(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}