def solution(id_pw, db):
    value = 1
    for i in range(0,len(db)):
        if id_pw[0] == db[i][0]:
            if id_pw[1] == db[i][1]:
                return "login"
            elif id_pw[1] != db[i][1]:
                return "wrong pw"
        elif id_pw[0] != db[i][0]:
            value = -1
    if value == -1:
        return "fail"