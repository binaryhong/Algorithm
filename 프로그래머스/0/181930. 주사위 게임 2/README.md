# [level 0] 주사위 게임 2 - 181930 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181930?language=python3) 

### 성능 요약

메모리: 9.11 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 01월 19일 23:19:30

### 문제 설명

<p style="user-select: auto !important;">1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 <code style="user-select: auto !important;">a</code>, <code style="user-select: auto !important;">b</code>, <code style="user-select: auto !important;">c</code>라고 했을 때 얻는 점수는 다음과 같습니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">세 숫자가 모두 다르다면 <code style="user-select: auto !important;">a</code> + <code style="user-select: auto !important;">b</code> + <code style="user-select: auto !important;">c</code> 점을 얻습니다.</li>
<li style="user-select: auto !important;">세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (<code style="user-select: auto !important;">a</code> + <code style="user-select: auto !important;">b</code> + <code style="user-select: auto !important;">c</code>) × (<code style="user-select: auto !important;">a</code><sup style="user-select: auto !important;">2</sup> + <code style="user-select: auto !important;">b</code><sup style="user-select: auto !important;">2</sup> + <code style="user-select: auto !important;">c</code><sup style="user-select: auto !important;">2</sup> )점을 얻습니다.</li>
<li style="user-select: auto !important;">세 숫자가 모두 같다면 (<code style="user-select: auto !important;">a</code> + <code style="user-select: auto !important;">b</code> + <code style="user-select: auto !important;">c</code>) × (<code style="user-select: auto !important;">a</code><sup style="user-select: auto !important;">2</sup> + <code style="user-select: auto !important;">b</code><sup style="user-select: auto !important;">2</sup> + <code style="user-select: auto !important;">c</code><sup style="user-select: auto !important;">2</sup> ) × (<code style="user-select: auto !important;">a</code><sup style="user-select: auto !important;">3</sup> + <code style="user-select: auto !important;">b</code><sup style="user-select: auto !important;">3</sup> + <code style="user-select: auto !important;">c</code><sup style="user-select: auto !important;">3</sup> )점을 얻습니다.</li>
</ul>

<p style="user-select: auto !important;">세 정수 <code style="user-select: auto !important;">a</code>, <code style="user-select: auto !important;">b</code>, <code style="user-select: auto !important;">c</code>가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>, <code style="user-select: auto !important;">b</code>, <code style="user-select: auto !important;">c</code>는 1이상 6이하의 정수입니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">a</th>
<th style="user-select: auto !important;">b</th>
<th style="user-select: auto !important;">c</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">6</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">9</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">473</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">110592</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 1번에서 세 주사위 숫자가 모두 다르므로 2 + 6 + 1 = 9점을 얻습니다. 따라서 9를 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 2번에서 두 주사위 숫자만 같으므로 (5 + 3 + 3) × (5<sup style="user-select: auto !important;">2</sup> + 3<sup style="user-select: auto !important;">2</sup> + 3<sup style="user-select: auto !important;">2</sup> ) = 11 × 43 = 473점을 얻습니다. 따라서 473을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 3번에서 세 주사위 숫자가 모두 같으므로 (4 + 4 + 4) × (4<sup style="user-select: auto !important;">2</sup> + 4<sup style="user-select: auto !important;">2</sup> + 4<sup style="user-select: auto !important;">2</sup> ) × (4<sup style="user-select: auto !important;">3</sup> + 4<sup style="user-select: auto !important;">3</sup> + 4<sup style="user-select: auto !important;">3</sup> ) = 12 × 48 × 192 = 110,592점을 얻습니다. 따라서 110592를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges