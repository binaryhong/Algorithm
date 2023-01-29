a, b = map(str, input().split())
cnt = 0
differentList = []

# 길이가 같을 경우 문자를 앞뒤로 추가할수 없기에 현재 다른 인덱스만 출력.
if len(a) == len(b):
    for i in range(0, len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)

# 길이가 다를 경우
"""
koder / topcoder의 경우

koder 
topcoder

koder
 topcoder

koder
  topcoder

와 같이 문자열을 이동하면서 비교해서 최소값을 찾아야함.

len(b) - len(a) + 1 로 koder 문자열의 이동한계점 지정.

b[i:i + len(a)][j] 로 b를 이동시킴
ex) 0:5 -> 1:6, 2:7

비교해서 다를 경우 cnt 증가, 리스트 삽입 이후 리스트에선 최솟값 출력.
"""
if len(a) != len(b):
    for i in range(0, len(b) - len(a) + 1):
        for j in range(len(a)):
            if a[j] != b[i:i + len(a)][j]:
                cnt += 1
        differentList.append(cnt)
        cnt = 0
    print(min(differentList))
