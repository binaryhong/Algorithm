import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;
/*
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오
*/


public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BigInteger K = new BigInteger(st.nextToken());
        BigInteger L = new BigInteger(st.nextToken());
        //인수분해 소수가 L보다 작을 경우 해당 소수를 저장할 변수 선언
        int N = 0;

        //L은 BigInteger형이기때문에 int형인 i와 크기 비교를 하기 위해 intValue로 int형으로 변환
        //만약 L이 int 형을 벗어난 값을 입력 받을 수 있다면 컴파일 오류가 나겠지만, 1000000이기에 가능
        for(int i = 2; i < L.intValue(); i++) {
            //K에 i를 나눠서 나머지가 0이 나오면 이라는 조건을 사용
            if((K.remainder(BigInteger.valueOf(i))).compareTo(BigInteger.ZERO) == 0) {
                N = i;
                break;
            }
        }
        //삼항연산자로 S값에 N값의 여부에 따른 값 저장
        String S = (N > 0)? ("BAD " + N) : "GOOD";

        System.out.println(S);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}