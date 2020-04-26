my_hp, my_damage, enemy_hp, enemy_damage = map(int, input().split())


while True:
    enemy_hp -= my_damage
    if enemy_hp <= 0:
        print('Yes')
        break
    my_hp -= enemy_damage
    if my_hp <= 0:
        print('No')
        break
