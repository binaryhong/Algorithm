import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오
*/


public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 통화의 개수 N 입력
        int N = Integer.parseInt(br.readLine());

        // 통화 시간 목록 입력
        StringTokenizer st = new StringTokenizer(br.readLine());

        int totalYoungsik = 0; // 영식 요금제 총 비용
        int totalMinsik = 0;   // 민식 요금제 총 비용

        for(int i = 0; i < N; i++) {
            int duration = Integer.parseInt(st.nextToken());

            // 영식 요금제 계산 (30초마다 10원)
            int youngsikCost = ((duration / 30) + 1) * 10;
            totalYoungsik += youngsikCost;

            // 민식 요금제 계산 (60초마다 15원)
            int minsikCost = ((duration / 60) + 1) * 15;
            totalMinsik += minsikCost;
        }

        // 더 저렴한 요금제 판단 및 출력
        if (totalYoungsik < totalMinsik) {
            System.out.println("Y " + totalYoungsik);
        } else if (totalMinsik < totalYoungsik) {
            System.out.println("M " + totalMinsik);
        } else {
            System.out.println("Y M " + totalYoungsik);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
