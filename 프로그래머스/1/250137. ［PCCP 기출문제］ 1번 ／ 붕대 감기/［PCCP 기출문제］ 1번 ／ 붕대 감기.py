def solution(bandage, health, attacks):
    cur = 1 # 공격 리스트의 인덱스를 의미
    cur_health = health-attacks[0][1] # 첫 공격받은 후의 체력 의미
    cur_bon = 0 # 연속 붕대 성공을 위한 연속시간 카운팅
    
    for i in range(attacks[0][0]+1,attacks[-1][0]+1):
        if i == attacks[cur][0]:
            cur_health= cur_health-attacks[cur][1]
            cur+= 1
            cur_bon = 0
            if cur_health <= 0:
                return -1
            continue
        cur_bon += 1
        if cur_bon == bandage[0]:
            cur_health += bandage[2]
            cur_bon = 0
        cur_health += bandage[1]
        if cur_health > health:
            cur_health = health
        

    return cur_health