def solution(bandage, health, attacks):
    now_health = health
    attack_term = 0
    tot_t, sec_heal, extra_heal = bandage
    before_turn = 0

    for turn, attacks in attacks:
        attack_term = turn - before_turn - 1  # 공격 간극
        now_health += (attack_term * sec_heal) + ((attack_term // tot_t) * extra_heal)
        if now_health > health:
            now_health = health

        now_health -= attacks
        before_turn = turn

        if now_health <= 0:
            now_health = -1
            break

    return now_health
