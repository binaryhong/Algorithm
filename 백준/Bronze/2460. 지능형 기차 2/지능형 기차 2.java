import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws java.io.IOException {
        BufferedReader br = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        String line;
        int totalCnt = 0;
        int maxValue = Integer.MIN_VALUE;
        // 입력이 더 이상 없거나(line == null), 빈 줄일 경우 반복 종료
        while ((line = br.readLine()) != null && !line.trim().isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);

            // 공백으로 구분된 두 정수 입력 처리
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            totalCnt = totalCnt - a + b;
            // 현재 totalCnt가 maxValue보다 크면 maxValue 갱신
            if (totalCnt > maxValue) {
                maxValue = totalCnt;
            }

            // 여기서 a, b 값을 이용한 로직을 수행
        }
        System.out.println(maxValue);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
