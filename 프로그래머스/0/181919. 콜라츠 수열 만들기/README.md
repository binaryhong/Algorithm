# [level 0] 콜라츠 수열 만들기 - 181919 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181919?language=python3) 

### 성능 요약

메모리: 9.25 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 01월 19일 23:09:46

### 문제 설명

<p style="user-select: auto !important;">모든 자연수 <code style="user-select: auto !important;">x</code>에 대해서 현재 값이 <code style="user-select: auto !important;">x</code>이면 <code style="user-select: auto !important;">x</code>가 짝수일 때는 2로 나누고, <code style="user-select: auto !important;">x</code>가 홀수일 때는 <code style="user-select: auto !important;">3 * x + 1</code>로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시  <code style="user-select: auto !important;">x</code>가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.</p>

<p style="user-select: auto !important;">그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.</p>

<p style="user-select: auto !important;">계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다. </p>

<p style="user-select: auto !important;">임의의 1,000 보다 작거나 같은 양의 정수 <code style="user-select: auto !important;">n</code>이 주어질 때 초기값이 <code style="user-select: auto !important;">n</code>인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">n</code> ≤ 1,000</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">n</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">10</td>
<td style="user-select: auto !important;">[10, 5, 16, 8, 4, 2, 1]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">순서대로 연산한 결과를 표로 만들면 다음과 같습니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">연산 횟수</th>
<th style="user-select: auto !important;">x</th>
<th style="user-select: auto !important;">홀짝 여부</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">10</td>
<td style="user-select: auto !important;">짝수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">홀수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">16</td>
<td style="user-select: auto !important;">짝수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">8</td>
<td style="user-select: auto !important;">짝수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">짝수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">짝수</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">6</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">홀수</td>
</tr>
</tbody>
      </table>
<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">따라서 [10, 5, 16, 8, 4, 2, 1]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges