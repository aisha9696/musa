import random

dragon = {
    'hp': 2000,
    'defence': 120,
    'str': 150,
    'weapon': 0
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 120,
    'weapon': 250,
    'shield': 150,
    'has_shield': False,
    'counter': 1,
    'pot': 500
}


def display_dragon_info():
    print("Dragon has", dragon.get('hp'), "hp.")


def display_hero_info(number):
    if number == 1:
        print("=====================================")
        print("Hero defends himself!")
    elif number == 3:
        print("=====================================")
        print("Hero drinks pot! He has", hero.get('hp'), "hp!")
    else:
        print("Hero has", hero.get('hp'), "hp\n"
              "=====================================")


def modify_health(person, influence):
    hp = person.get('hp')
    hp += influence
    person['hp'] = hp
    if person.get('hp') <= 0:
        person['hp'] = 0


def hero_attack(heero, drag):
    damage = heero.get('str') + heero.get('weapon') - drag.get('defence')
    if damage < 0:
        damage = 0
    if random.random() < 0.75:
        modify_health(dragon, -damage)
        print("=====================================\n"
              "Hero did", damage, "damage!")
        display_dragon_info()

    else:
        print("=====================================\n"
              "Hero missed")
        display_dragon_info()

    return damage


def hero_defence(heero):
    equip_shield()
    power = heero.get('defence') + heero.get('shield')
    return power


def equip_shield():
    if not hero.get('has_shield'):
        hero['has_shield'] = True


def remove_shield():
    hero['has_shield'] = False


def hero_pass():
    print("=====================================")
    print("Hero missed his turn!")


def use_pot():
    hero['counter'] -= 1


def hero_turn(choice):
    if choice.lower() == 'attack':
        hero_attack(hero, dragon)
    elif choice.lower() == 'defence':
        hero_defence(hero)
        display_hero_info(1)
        display_dragon_info()
    elif choice.lower() == 'pass':
        hero_pass()
        display_dragon_info()
    elif choice.lower() == 'healthier':
        if hero.get('counter') > 0:
            use_pot()
            modify_health(hero, hero.get('pot'))
            display_hero_info(3)
            display_dragon_info()
        else:
            hero_pass()
            display_dragon_info()
    else:
        hero_turn(input("Enter one of the turn: attack, defence, pass, healthier:"))


def dragon_attack(heero, drag):
    if hero.get('has_shield'):
        damage = drag.get('str') + drag.get('weapon') - hero_defence(hero)
    else:
        damage = drag.get('str') + drag.get('weapon') - heero.get('defence')
    if damage < 0:
        damage = 0
    return damage


def dragon_turn():
    if random.random() < 0.5:
        modify_health(hero, -dragon_attack(hero, dragon))
        print("=====================================\n"
              "Dragon did", dragon_attack(hero, dragon), "damage!")
        display_hero_info(2)
    else:
        print("=====================================\n"
              "Dragon just slept. -_-")
        display_hero_info(2)


while True:
    if dragon.get('hp') <= 0:
        print("Hero wins!")
        break
    elif hero.get('hp') <= 0:
        print("Hero lost!")
        break
    hero_turn(input("Enter one of the turn: attack, defence, pass, healthier:"))
    dragon_turn()
    remove_shield()
