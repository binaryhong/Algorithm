n = int(input())
s = list(input() for _ in range(n))
for i in range(0, len(s)):
    s[i] = s[i][::-1]
bList = [""] * n
k = 1
for i in range(1,len(s[0])+1):
    for j in range(0,n):
        bList[j] = s[j][0:i]
        """
        bList: ['5', '6', '5']
        bList: ['54', '65', '54']
        ...
        bList: ['5432121', '6532121', '5443300']
        """
    if len(list(set(bList))) == n:
        print(len(bList[0]))
        """
                bList: ['5', '6', '5']
                bList: ['54', '65', '54']
                bList: ['543', '653', '544']
                3번째 실행에서 세 수가 모두 다르므로 break.
                세 수의 길이가 모두 똑같으므로 첫번째 수의 길이를 반환함.
                ...
                bList: ['5432121', '6532121', '5443300']
        """
        break