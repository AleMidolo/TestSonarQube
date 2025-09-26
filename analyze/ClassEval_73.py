class RPGCharacter:
    MAX_HP = 100
    EXP_PER_LEVEL = 100
    HP_INCREASE_ON_LEVEL_UP = 20
    ATTACK_POWER_INCREASE_ON_LEVEL_UP = 5
    DEFENSE_INCREASE_ON_LEVEL_UP = 5

    def __init__(self, name, hp, attack_power, defense, level=1):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        damage = self.calculate_damage(other_character)
        other_character.hp -= damage

    def calculate_damage(self, other_character):
        return max(self.attack_power - other_character.defense, 1)

    def heal(self):
        self.hp = min(self.hp + 10, self.MAX_HP)
        return self.hp

    def gain_exp(self, amount):
        while amount != 0:
            if self.has_level_up(amount):
                amount -= self.level_up_exp_needed()
                self.level_up()
            else:
                self.exp += amount
                amount = 0

    def has_level_up(self, amount):
        return self.exp + amount >= self.level * self.EXP_PER_LEVEL

    def level_up_exp_needed(self):
        return self.level * self.EXP_PER_LEVEL - self.exp

    def level_up(self):
        if self.level < 100:
            self.level += 1
            self.exp = 0
            self.increase_stats()

    def increase_stats(self):
        self.hp += self.HP_INCREASE_ON_LEVEL_UP
        self.attack_power += self.ATTACK_POWER_INCREASE_ON_LEVEL_UP
        self.defense += self.DEFENSE_INCREASE_ON_LEVEL_UP

    def is_alive(self):
        return self.hp > 0