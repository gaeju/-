def solution(hp):
    general = 5
    soldier = 3
    work = 1
    cnt = 0
    cnt += hp // general
    cnt += (hp % general) // soldier
    cnt += (hp % general) % soldier
    return cnt