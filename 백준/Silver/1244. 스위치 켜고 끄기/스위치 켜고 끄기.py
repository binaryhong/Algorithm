T = int(input())
switch_arr = list(map(int, input().split()))
student = int(input())
for i in range(student):
    gender, num = map(int, input().split())

    if gender == 1:
        temp = num
        while num <= len(switch_arr):
            if switch_arr[num - 1] == 1:
                switch_arr[num - 1] = 0
            else:
                switch_arr[num - 1] = 1
            num += temp
    else:
        if num == 1 or num == len(switch_arr):
            if switch_arr[num - 1] == 1:
                switch_arr[num - 1] = 0
            else:
                switch_arr[num - 1] = 1
        else:
            sym = 0
            k = 1
            try:
                while switch_arr[num - 1 - k] == switch_arr[num - 1 + k] and num - 1 - k >= 0 and num - 1 + k <= len(
                        switch_arr) - 1:
                    sym += 1
                    k += 1
            except:
                pass
            if sym == 0:
                if switch_arr[num - 1] == 1:
                    switch_arr[num - 1] = 0
                else:
                    switch_arr[num - 1] = 1
            else:
                for j in range(sym * 2 + 1):
                    if switch_arr[num - 1 - sym + j] == 1:
                        switch_arr[num - 1 - sym + j] = 0
                    else:
                        switch_arr[num - 1 - sym + j] = 1
for i in range(0, T, 20):
    print(*switch_arr[i:i + 20])