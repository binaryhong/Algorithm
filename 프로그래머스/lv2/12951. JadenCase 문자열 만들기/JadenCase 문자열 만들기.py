import re

def solution(s):
    return re.sub(r'\b(\d*[a-zA-Z]+)\b', lambda x: x.group(1).capitalize(), s)