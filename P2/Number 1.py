# Muhammad Royhan Alfitra
# 123140146
# PRAKTIKUM PBO RD


import random

class Robot:
    def __init__(self, name, attack_power, hp, accuracy, evasion, is_ai=False):
        self.name = name
        self.attack_power = attack_power
        self.hp = hp
        self.accuracy = accuracy
        self.evasion = evasion
        self.stunned = False
        self.defending = False
        self.is_ai = is_ai  # Set Robot mana yang menjadi CPU / Komputer

    def attack_enemy(self, enemy):
        if self.stunned:
            print(f"{self.name} is stunned and cannot attack.")
            self.stunned = False
            return

        if random.random() > self.accuracy:
            print(f"{self.name} missed the attack!")    # Serangan Miss Apabile Accuracy lebih kecil dari Evasion musuh
        elif random.random() < enemy.evasion:
            print(f"{enemy.name} dodged the attack!")   # Serangan Terhindar Apabila Evasion lebih besar dari Accuracy musuh
        else:
            damage = random.randint(self.attack_power - 5, self.attack_power + 5)
            enemy.hp -= damage
            print(f"{self.name} attacked {enemy.name} for {damage} damage!")
            print(f"=== TURN END ===")
            enemy.defending = False

            if random.random() < 0.1:   # 10% chance musuh terkena Stun / Stagger
                print(f"{enemy.name} is stunned!")
                enemy.stunned = True

    def regen_health(self):
        heal = random.randint(7, 15)
        self.hp += heal
        print(f"{self.name} regenerated {heal} HP!")

    def check_health(self):
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
            return True
        return False
    
    def choose_action(self):
        if self.is_ai:
            return str(random.choice(["1", "2", "3"]))  # AI / CPU memilih Action secara Random
        return input(f"{self.name}, select command : ")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start_game(self):
        round_number = 1
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"Round {round_number}===========================\n")
            print(f"{self.robot1.name} HP: {self.robot1.hp} | {self.robot1.attack_power}")
            print(f"{self.robot2.name} HP: {self.robot2.hp} | {self.robot2.attack_power}")

            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:
                print(f"\n{robot.name}'s Turn!")    # Notifikasi Turn Robot
                print(" 1. Attack   2. Defense  3. Self Destruct")
                action = robot.choose_action()
                print(f"{robot.name} selects: {action}")
                
                if action == "1":
                    robot.attack_enemy(enemy)
                elif action == "2":
                    robot.defending = True
                elif action == "3":
                    print(f"\n{enemy.name} Victory!")
                    return
            round_number += 1

# Game Start
robot1 = Robot("Maximus CXV", 10, 500, 0.8, 0.2)  # Player-controlled robot
robot2 = Robot("Xervius X", 9, 480, 0.9, 0.3, is_ai=True)  # AI-controlled robot

game = Game(robot1, robot2)
game.start_game()
