N = int(input()) # N 입력
A = list(map(int, input().split())) # A 입력
B = sorted(range(N), key=lambda x: A[x]) # A의 값에 따라 인덱스 정렬
P = [0] * N # P 초기화
for i in range(N):
    P[B[i]] = i # P 채우기
print(*P) # 결과 출력