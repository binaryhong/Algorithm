import java.io.*;

public class Main {
    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputLine = br.readLine().trim(); // 공백 제거

        // 공백만 있는 경우 또는 빈 문자열 처리
        if (inputLine.isEmpty()) {
            System.out.println(0);
            return;
        }

        String[] words = inputLine.split(" ");
        int wordCount = words.length;
        if (inputLine.startsWith(" ")) {
            System.out.println(wordCount - 1);
        }
        else {
            System.out.println(wordCount);
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}