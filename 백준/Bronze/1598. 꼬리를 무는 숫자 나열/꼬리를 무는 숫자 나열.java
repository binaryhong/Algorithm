import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오
*/


public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 두 개의 자연수를 입력받습니다.
        String[] inputs = br.readLine().split(" ");
        int a = Integer.parseInt(inputs[0]);
        int b = Integer.parseInt(inputs[1]);

        // 첫 번째 숫자의 위치 계산
        int colA = (a - 1) / 4;
        int rowA = (a - 1) % 4;

        // 두 번째 숫자의 위치 계산
        int colB = (b - 1) / 4;
        int rowB = (b - 1) % 4;

        // 직각 거리 계산
        int distance = Math.abs(colA - colB) + Math.abs(rowA - rowB);

        // 결과 출력
        System.out.println(distance);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
