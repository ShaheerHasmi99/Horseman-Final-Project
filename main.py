import sys,time,os
import random
#player Stats = [str, health, lvl, exp, gld] 
Nictis = [5, 100, 1, 0, 0]
playerHpCap = 100
playerLvlUP = 10
Nictis[1] <= playerHpCap
Nictis[3] <= playerLvlUP
def LevelUp():
    if Nictis[3] == playerLvlUP:
        print("LEVEL UP!")
        if Nictis[2] == 2:
            GradualText("When you level up you gain 1 str stat, 10 to you hp, level up to get stronger!")
        playerHpCap = playerHpCap + 10
        playerLvlUP = playerLvlUp + 10
        Nictis[0] = Nictis[0] + 1
        Nictis[1] = Nictis[1] + 10
        Nictis[2] = Nictis[2] + 1

playerParty = 1
Griffon = [5, 250]
#inventory
genericSword = 2
weaponAdd = genericSword


#Party/enemies
party = ["Nictis"]
player = party[0]
tutorialGoblin = [2, 40, 5, 5]
hunterGoblin1 = [3, 45, 5, 10]
hunterGoblin2 = [2, 35, 5, 5]
hunterGoblin3 = [5, 40, 5, 15]
goblinWeap = 1
#enemies = [str, health, exp, gold]


#other Factors
block = False
crit = False
hit = True
global sides
friends = 0
enemies = 0
sides = 6
baseDamage = 0
oppDmg = 0
PlayerTurn = False
def TurnDecide():
    if friends + enemies == 3:
        turnDecide = random.randint(1,3)
        if turnDecide == 1:
            en1Turn = True
            print(en1, "turn")
        elif turnDecide == 2:
            p1Turn = True
            print(p1, "turn")
        elif turnDecide == 3:
            PlayerTurn = True
            print("Nictis' turn")
    elif friends + enemies == 4:
        turnDecide = random.randint(1,4)
        if friends == 3 and enemies == 1:
            if turnDecide == 1:
                en1Turn = True
                print(en1, "turn")
            elif turnDecide == 2:
                p1Turn = True
                print(p1, "turn")
            elif turnDecide == 3:
                p2Turn = True
                print(p2, "turn")
            elif turnDecide == 4:
                playerTurn = True
                print("Nictis' turn")
        elif friends == 2 and enemies == 2:
            turnDecide = random.randint(1,4)
            if turnDecide == 1:
                en1Turn = True
                print(en1, "turn")
            elif turnDecide == 2:
                en2Turn = True
                print(en2, "turn")
            elif turnDecide == 3:
                p2Turn = True
                print(p2, "turn")
            elif TurnDecide == 4:
                playerTurn = True
                en3turn = False
                print("Nictis' turn")
    elif friends + enemies == 5:
        turnDecide = random.randint(1,5)
        if friends == 3 and enemies == 2:
                if turnDecide == 1:
                    en1Turn = True
                    print(en1, "turn")
                elif turnDecide == 2:
                    en2Turn = True
                    print(en2, "turn")
                elif turnDecide == 3:
                    p1Turn = True
                    print(p1, "turn")
                elif turnDecide == 4:
                    p2Turn = True
                    print(p2, "turn")
                elif turnDecide == 5:
                    playerTurn = True
                    print("Nictis' turn")
        elif friends == 2 and enemies == 3:
                if turnDecide == 1:
                    en1Turn = True
                    print(en1, "turn")
                elif turnDecide == 2:
                    en2Turn = True
                    print(en2, "turn")
                elif turnDecide == 3:
                    en3Turn = True
                    print(en3, "turn")
                elif turnDecide == 4:
                    p1Turn = True
                    print(p1, "turn")
                elif turnDecide == 5:
                    playerTurn = True
                    print("Nictis' turn")
    else: # maximum of 6 enemies + friends
        turnDecide = random.randint(1,6)
        if friends == 3 and enemies == 3:
            if turnDecide == 1:
                en1Turn = True
                print(en1, "turn")
            elif turnDecide == 2:
                en2Turn = True
                print(en2, "turn")
            elif turnDecide == 3:
                en3Turn = True
                print(en3, "turn")
            elif turnDecide == 4:
                p1Turn = True
                print(p1, "turn")
            elif turnDecide == 5:
                p2Turn = True
                print(p2, "turn")
            elif turnDecide == 6:
                playerTurn = True
                print("Nictis' turn")

def Damage(atkStr, oppStr, weaponAdd, enemyAdd):
    baseDamage = float((atkStr *2) + weaponAdd)
    enemyDamage = float((atkStr*2) + enemyAdd)
    rollCrit = random.randint(1, 12)
    if rollCrit == 2:
        CombatText("The Attack Crit!\n")
        crit = True
    else:
        crit = False
    if crit == True:
        baseDamage = float(baseDamage *2)
        enemyDamage = float(enemyDamage *2)
    else:
        print("Crit Failed!\n")
    Defence(atkStr, oppStr)
    if block == True:
        CombatText("Block succsessfull!\n")
        baseDamage = float(baseDamage /2)
        enemyDamage = float(enemyDamage/2)
        black = False
    else:
        print("Block Failed!\n")
    return baseDamage
    return enemyDamage

def Defence(atkStr, oppStr):
    if atkStr > oppStr:
        if (atkStr - oppStr) <= 1:
            sides = 6
        elif (atkStr - oppStr) == 2:
            sides = 5
        elif (atkStr - oppStr) == 3:
            sides = 4
        elif (atkStr - oppStr) == 4:
            sides = 3
        elif (atkStr - oppStr) == 5:
            sides = 2
        elif (atkStr - oppStr) >=6:
            sides = 1
    else:
        if (oppStr - atkStr) <= 1:
            sides = 6
        elif (oppStr - atkStr) == 2:
            sides = 7
        elif (oppStr - atkStr) == 3:
            sides = 8
        elif (oppStr - atkStr) == 4:
            sides = 9
        elif (oppStr - atkStr) == 5:
            sides = 10
        elif (oppStr - atkStr) == 6:
            sides = 11
        elif (oppStr - atkStr) > 6:
            sides = 12
    rollBlock = random.randint(1, sides)
    if rollBlock == 2:
        block = True
    else:
        block = False
        
def Combat(friends, enemies, Nictis, p1, p2, en1, en2, en3, enemyAdd):
    global playerTurn
    global p1Turn
    global p2Turn
    global en1Turn
    global en2Turn
    global en3Turn
    global tutorial
    global win
    playerTurn = True
    en1Turn = False
    en2Turn = False
    p1Turn = False
    p2Turn = False
    en3Turn = False
    tutorial = True
    win = False
    
    while True:
        if Nictis[1] == 0: #PLAYER <--------
            print("game over")
            win = False
            break
        else:
            if playerTurn == True:
                decision = input("\ntype the number of what you would like to do 1.Attack, 2. Defend, 3. run: ")
                if decision == "1":
                    if enemies == 1:
                        baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                        en1[1] = float(en1[1]) - baseDamage
                        print("you hit for", baseDamage, "enemies health", en1[1])
                        playerTurn = False
                        en1Turn = True
                    elif enemies == 2:
                        if en[1] > 0 and en2[1] > 0:
                            atkChoice = input("\ntype the number of who you would like to attack 1.enemy One, 2.enemy Two")
                            if atkChoice == "1":
                                baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies ines health", en1[1])
                                playerTurn = False
                                en1Turn = True
                            elif atkChoice == "2":
                                baseDamage = Damage(Nictis[0], en2[0], weaponAdd, enemyAdd)
                                en1[1] = float(en2[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Two's health", en2[1])
                                playerTurn = False
                                en1Turn = True
                        elif en[1] > 0 and en2[1] <= 0:
                            baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                            en1[1] = float(en1[1]) - baseDamage
                            print("you hit for", baseDamage, "enemies ones health", en1[1])
                            playerTurn = False
                            en1Turn = True
                        elif en[1] <= 0 and en2[1] > 0:
                            baseDamage = Damage(Nictis[0], en2[0], weaponAdd, enemyAdd)
                            en2[1] = float(en2[1]) - baseDamage
                            print("you hit for", baseDamage, "enemies two's health", en2[1])
                            playerTurn = False
                            en2Turn = True
                    else:
                        if en1[1] > 0 and en2[1] > 0 and en3[1] > 0:
                            atkChoice = input("\nhoose who you would like to fight 1.enemy one, 2.enemy two, 3. enemy three")
                            if atkChoice == "1":
                                baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies ones health", en1[1])
                                playerTurn = False
                                en1Turn = True
                            elif atkChoice == "2":
                                baseDamage = Damage(Nictis[0], en2[0], weaponAdd, enemyAdd)
                                en1[1] = float(en2[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Two's health", en2[1])
                                playerTurn = False
                                en1Turn = True
                            elif atkChoice == "3":
                                baseDamage = Damage(Nictis[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Three's health", en3[1])
                                playerTurn = False
                                en1Turn = True
                        elif en1[1] > 0 and en2[1] > 0 and en3[1] <= 0:
                            atkChoice = input("\n type the number of who you would like to attack 1.enemy One, 2.enemy Two")
                            if atkChoice == "1":
                                baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies one's health", en1[1])
                                playerTurn = False
                                en1Turn = True
                            elif atkChoice == "2":
                                baseDamage = Damage(Nictis[0], en2[0], weaponAdd, enemyAdd)
                                en1[1] = float(en2[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Two's health", en2[1])
                                playerTurn = False
                                en1Turn = True
                        elif en1[1] > 0 and en2[1] <= 0 and en3[1] <= 0:
                            baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                            en1[1] = float(en1[1]) - baseDamage
                            print("you hit for", baseDamage, "enemies one's health", en1[1])
                            playerTurn = False
                            en1Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] > 0:
                            atkChoice = input("\ntype the number of who you would like to attack 1.enemy Two, 2.enemy Three")
                            if atkChoice == "1":
                                baseDamage = Damage(Nictis[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Two's health", en2[1])
                                playerTurn = False
                                en2Turn = True
                            elif atkChoice == "2":
                                baseDamage = Damage(Nictis[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("you hit for", baseDamage, "enemies Three's health", en2[1])
                                playerTurn = False
                                en2Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] <= 0:
                            baseDamage = Damage(Nictis[0], en1[0], weaponAdd, enemyAdd)
                            en2[1] = float(en2[1]) - baseDamage
                            print("you hit for", baseDamage, "enemies Two's health", en2[1])
                            playerTurn = False
                            en1Turn = True
                        elif en1[1] <= 0 and en2[1] <= 0 and en3[1] > 0:
                            baseDamage = Damage(Nictis[0], en3[0], weaponAdd, enemyAdd)
                            en3[1] = float(en3[1]) - baseDamage
                            print("you hit for", baseDamage, "enemies Three's health", en3[1])
                            playerTurn = False
                            en3Turn = True
                        
                        
                elif decision == "2":
                    CombatText("Strength increased by 2 better defensive stance\n")
                    Nictis[0] = float(Nictis[0]) + 2
                    playerTurn = False
                    if en1[1] > 0:
                        en1Turn = True
                        CombatText("Enemey ones Turn\n")
                    elif en1[1] > 0 and en2[1] > 0:
                        en1Turn = True
                        CombatText("Enemey ones Turn\n")
                    elif en1[1] > 0 and en2[1] >  0 and en3[1] > 0:
                        en1Turn = True
                        CombatText("Enemey ones Turn\n")
                    elif en[1] <= 0:
                        en2Turn = True
                        CombatText("Enemy Two's Turn\n")
                    elif en1[1] <= 0 and en2[1] <= 0:
                        en3Turn = True
                        CombatText("Enemy Three's Turn\n")
            elif playerTurn == False:
                if en1Turn == True: #ENEMY ONE <---------
                    CombatText("Enemy one is Attacking\n")
                    if friends == 2:
                        if p1[1] > 0 and Nictis[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Nictis\n")
                                enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                                Nictis[1] = float(Nictis[1]) - enemyDamage
                                print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                en1Turn = False
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                p1Turn = True
                            else:
                                CombatText("Target Party member one\n")
                                enemyDamage = Damage(en1[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                en1Turn = False
                                p1Turn = True
                        elif p1[1] <= 0 and Nictis[1] > 0:
                            CombatText("Target Nictis\n")
                            enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                            Nictis[1] = float(Nictis[1]) - enemyDamage
                            print("you have been hit for", enemyDamage, " your health", Nictis[1])
                            en1Turn = False
                            if decision == "2":
                                Nictis[0] = float(Nictis[0]) - 2
                            playerTurn = True  
                    if friends == 3:
                        if p1[1] > 0 and Nictis[1] > 0 and p2[1] > 0:
                            whoAtk = random.randint(1,3)
                            if whoAtk == 1:
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en1Turn = False
                                    if decision == "2":
                                        Nictis[0] = float(Nictis[0]) - 2
                                    p1Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Party member one\n")
                                enemyDamage = Damage(en1[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                en1Turn = False
                                p1Turn = True
                            else:
                                CombatText("Target Party member two\n")
                                enemyDamage = Damage(en1[0], p2[0], weaponAdd, enemyAdd)
                                p2[1] = float(p2[1]) - enemyDamage
                                print("Party member two has been hit for", enemyDamage, "Party member two's health", p2[1])
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                en1Turn = False
                                p1Turn = True
                        elif p1[1] > 0 and Nictis[1] > 0 and p2[1] <= 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Nictis\n")
                                enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                                Nictis[1] = float(Nictis[1]) - enemyDamage
                                print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                en1Turn = False
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                p1Turn = True
                            else:
                                CombatText("Target Party member one\n")
                                enemyDamage = Damage(en1[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                en1Turn = False
                                p1Turn = True
                        elif p1[1] <= 0 and Nictis[1] > 0 and p2[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Nictis\n")
                                enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                                Nictis[1] = float(Nictis[1]) - enemyDamage
                                print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                en1Turn = False
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                p1Turn = True
                            else:
                                CombatText("Target Party member Two\n")
                                enemyDamage = Damage(en1[0], p2[0], weaponAdd, enemyAdd)
                                p2[1] = float(p2[1]) - enemyDamage
                                print("Party member Two has been hit for", enemyDamage, "Party member Two's health", p2[1])
                                if decision == "2":
                                    Nictis[0] = float(Nictis[0]) - 2
                                en1Turn = False
                                p2Turn = True
                        elif p1[1] <= 0 and Nictis[1] > 0 and p2[1] <= 0:
                            CombatText("Target Nictis\n")
                            enemyDamage = Damage(en1[0], Nictis[0], weaponAdd, enemyAdd)
                            Nictis[1] = float(Nictis[1]) - enemyDamage
                            print("you have been hit for", enemyDamage, " your health", Nictis[1])
                            en1Turn = False
                            if decision == "2":
                                Nictis[0] = float(Nictis[0]) - 2
                            playerTurn = True
                elif p1Turn == True: #PARTY MEMBER 1 <--------
                    CombatText("Party member one is attacking!\n")
                    if enemies == 1:
                        CombatText("Party Member one's target is Enemy one\n")
                        baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                        en1[1] = float(en1[1])- baseDamage
                        print("the enemy has been hit for", baseDamage, "enemies health", en1[1])
                        if decision == "2":
                            Nictis[0] = float(Nictis[0]) - 2
                        p1Turn = False
                        playerTurn = True
                    if enemies == 2:
                        if en1[1] > 0 and en2[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p1Turn = False
                                en2Turn = True
                            else:
                                GradualText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy two health", en2[1])
                                p1Turn = False
                                en2Turn = True
                        elif en1[1] > 0 and en2[1] <= 0:
                            CombatText("Target Enemy One\n")
                            baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                            en1[1] = float(en1[1]) - baseDamage
                            print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                            p1Turn = False
                            playerTurn = True
                        elif en1[1] <= 0 and en2[1] > 0:
                            GradualText("Target Enemy Two\n")
                            baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                            en2[1] = float(en2[1]) - baseDamage
                            print("Party member one hit enemy two for", baseDamage, " Enemy two health", en2[1])
                            p1Turn = False
                            en2Turn = True
                    if enemies == 3:
                        if en1[1] > 0 and en2[1] > 0 and en3[1] > 0:
                            whoAtk = random.randint(1,3)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p1Turn = False
                                en2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy two health", en2[1])
                                p1Turn = False
                                en2Turn = True
                            elif whoAtk == 3:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("Party member one hit Enemy Three for", baseDamage, " Enemy Three health", en3[1])
                                p1Turn = False
                                en2Turn = True
                        elif en1[1] > 0 and en2[1] > 0 and en3[1] <= 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p1Turn = False
                                en2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy two health", en2[1])
                                p1Turn = False
                                en2Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en2[1])
                                p1Turn = False
                                en2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy two health", en3[1])
                                p1Turn = False
                                en2Turn = True
                        elif en1[1] > 0 and en2[1] <= 0 and en3[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p1Turn = False
                                en3Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("Party member one hit enemy Three for", baseDamage, " Enemy Three health", en3[1])
                                p1Turn = False
                                en3Turn = True
                        elif en1[1] > 0 and en2[1] <= 0 and en3[1] <= 0:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p1Turn = False
                                en1Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] <= 0:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy Two for", baseDamage, " Enemy Two health", en2[1])
                                p1Turn = False
                                en2Turn = True
                        elif en1[1] <= 0 and en2[1] <= 0 and en3[1] > 0:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("Party member one hit enemy Three for", baseDamage, " Enemy Three health", en3[1])
                                p1Turn = False
                                en3Turn = True
                elif en2Turn == True: #ENEMY TWO<---------
                        CombatText("Enemy Two is Attacking\n")
                        if friends == 2:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Nictis\n")
                                enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                Nictis[1] = float(Nictis[1]) - enemyDamage
                                print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                en2Turn = False
                                playerTurn = True
                            else:
                                CombatText("Target Party member one\n")
                                enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                en2Turn = False
                                playerTurn = True
                        if friends == 3:
                            if p1[1] > 0 and Nictis[1] > 0 and p2[1] > 0:
                                whoAtk = random.randint(1,3)
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en2Turn = False
                                    p2Turn = True
                                elif whoAtk == 2:
                                    CombatText("Target Party member One\n")
                                    enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                                    p1[1] = float(p1[1]) - enemyDamage
                                    print("Party member One has been hit for", enemyDamage, "Party member ones health", p1[1])
                                    en2Turn = False
                                    p2Turn = True
                                else:
                                    CombatText("Target Party member Two\n")
                                    enemyDamage = Damage(en2[0], p2[0], weaponAdd, enemyAdd)
                                    p2[1] = float(p2[1]) - enemyDamage
                                    print("Party member two has been hit for", enemyDamage, "Party member Two's health", p2[1])
                                    en2Turn = False
                                    p2Turn = True
                            elif p1[1] > 0 and Nictis[1] > 0 and p2[1] <= 0:
                                whoAtk = random.randint(1,2)
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en2Turn = False
                                    playerTurn = True
                                elif whoAtk == 2:
                                    CombatText("Target Party member two\n")
                                    enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                                    p1[1] = float(p1[1]) - enemyDamage
                                    print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                    en2Turn = False
                                    playerTurn = True
                            elif p1[1] <= 0 and Nictis[1] > 0 and p2[1] > 0:
                                whoAtk = random.randint(1,2)
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en2Turn = False
                                    p2Turn = True
                                elif whoAtk == 2:
                                    CombatText("Target Party member two\n")
                                    enemyDamage = Damage(en2[0], p2[0], weaponAdd, enemyAdd)
                                    p2[1] = float(p2[1]) - enemyDamage
                                    print("Party member Two has been hit for", enemyDamage, "Party member Two's health", p2[1])
                                    en2Turn = False
                                    p2Turn = True
                            elif p1[1] <= 0 and Nictis[1] > 0 and p2[1] <= 0:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en2Turn = False
                                    playerTurn = True
                elif p2Turn == True: #PARTY MEMBER 2
                    GradualText("Party member one is attacking!\n")
                    if enemies == 1:
                        GradualText("Party Member one's target is Enemy one\n")
                        baseDamage = Damage(p2[0], en1[0], weaponAdd, enemyAdd)
                        en1[1] = float(en1[1])- baseDamage
                        print("the enemy has been hit for", baseDamage, "enemies health", en1[1])
                        p2Turn = False
                        en1Turn = True
                    if enemies == 2:
                        if en1[1] > 0 and en2[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One")
                                baseDamage = Damage(p2[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p2Turn = False
                                en2Turn = False
                            else:
                                CombatText("Target Party member one\n")
                                baseDamage = Damage(p2[0], en1[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1])- baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy twohealth", en2[1])
                                p2Turn = False
                                en2Turn = False
                        elif en1[1] > 0 and en2[1] <= 0:
                            CombatText("Target Enemy One")
                            baseDamage = Damage(p2[0], en1[0], weaponAdd, enemyAdd)
                            en1[1] = float(en1[1]) - baseDamage
                            print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                            p2Turn = False
                            en1Turn = False
                        elif en1[1] <= 0 and en2[1] > 0:
                            CombatText("Target Party member one\n")
                            baseDamage = Damage(p2[0], en2[0], weaponAdd, enemyAdd)
                            en2[1] = float(en2[1])- baseDamage
                            print("Party member one hit enemy two for", baseDamage, " Enemy twohealth", en2[1])
                            p2Turn = False
                            en2Turn = False
                        
                    if enemies == 3:
                        if en1[1] > 0 and en2[1] > 0 and en3[1] > 0:
                            whoAtk = random.randint(1,3)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p2Turn = False
                                en3Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1])- baseDamage
                                print("Party member one hit enemy two for", baseDamage, " Enemy two health", en2[1])
                                p2Turn = False
                                en3Turn = True
                            elif whoAtk == 3:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1])- baseDamage
                                print("Party member one hit Enemy Three for", baseDamage, " Enemy Three health", en3[1])
                                p2Turn = False
                                en3Turn = True
                        elif en1[1] > 0 and en2[1] > 0 and en3[1] <= 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p2Turn = False
                                en2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Two\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1])- baseDamage
                                print("Party member Two hit enemy two for", baseDamage, " Enemy two health", en2[1])
                                p2Turn = False
                                en2Turn = True
                        elif en1[1] > 0 and en2[1] <= 0 and en3[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p2Turn = False
                                en3Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1])- baseDamage
                                print("Party member Three hit enemy two for", baseDamage, " Enemy Three health", en3[1])
                                p2Turn = False
                                en3Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en2[1])
                                p2Turn = False
                                en3Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Enemy Three\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1])- baseDamage
                                print("Party member Three hit enemy two for", baseDamage, " Enemy Three health", en3[1])
                                p2Turn = False
                                en3Turn = True
                        elif en1[1] > 0 and en2[1] <= 0 and en3[1] <= 0:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en1[0], weaponAdd, enemyAdd)
                                en1[1] = float(en1[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en1[1])
                                p2Turn = False
                                en1Turn = True
                        elif en1[1] <= 0 and en2[1] > 0 and en3[1] <= 0:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en2[0], weaponAdd, enemyAdd)
                                en2[1] = float(en2[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en2[1])
                                p2Turn = False
                                en2Turn = True
                        elif en1[1] <= 0 and en2[1] <= 0 and en3[1] > 0:
                                CombatText("Target Enemy One\n")
                                baseDamage = Damage(p1[0], en3[0], weaponAdd, enemyAdd)
                                en3[1] = float(en3[1]) - baseDamage
                                print("Party member one hit enemy one for", baseDamage, " Enemy one health", en3[1])
                                p2Turn = False
                                en3Turn = True
                            
                elif en3Turn == True: #ENEMY THREE
                    CombatText("Enemy one is Attacking\n")
                    if friends == 2:
                        whoAtk = random.randint(1,2)
                        if whoAtk == 1:
                            CombatText("Target Nictis\n")
                            enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                            Nictis[1] = float(Nictis[1]) - enemyDamage
                            print("you have been hit for", enemyDamage, " your health", Nictis[1])
                            en3Turn = False
                            p1Turn = True
                        else:
                            CombatText("Target Party member one\n")
                            enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                            p1[1] = float(p1[1]) - enemyDamage
                            print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                            en3Turn = False
                            p1Turn = True
                    if friends == 3:
                        if p1[1] > 0 and Nictis[1] > 0 and p2[1] > 0:
                            whoAtk = random.randint(1,3)
                            if whoAtk == 1:
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en3Turn = False
                                    p2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Party member two\n")
                                enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                en3Turn = False
                                p2Turn = True
                            else:
                                CombatText("Target Party member Three\n")
                                enemyDamage = Damage(en2[0], p2[0], weaponAdd, enemyAdd)
                                p2[1] = float(p2[1]) - enemyDamage
                                print("Party member three has been hit for", enemyDamage, "Party member Three's health", p2[1])
                                en3Turn = False
                                p2Turn = True
                        elif p1[1] > 0 and Nictis[1] > 0 and p2[1] <= 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                if whoAtk == 1:
                                    CombatText("Target Nictis\n")
                                    enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                    Nictis[1] = float(Nictis[1]) - enemyDamage
                                    print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                    en3Turn = False
                                    playerTurn = True
                            elif whoAtk == 2:
                                CombatText("Target Party member two\n")
                                enemyDamage = Damage(en2[0], p1[0], weaponAdd, enemyAdd)
                                p1[1] = float(p1[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p1[1])
                                en3Turn = False
                                playerTurn = True
                        elif p1[1] <= 0 and Nictis[1] > 0 and p2[1] > 0:
                            whoAtk = random.randint(1,2)
                            if whoAtk == 1:
                                CombatText("Target Nictis\n")
                                enemyDamage = Damage(en2[0], Nictis[0], weaponAdd, enemyAdd)
                                Nictis[1] = float(Nictis[1]) - enemyDamage
                                print("you have been hit for", enemyDamage, " your health", Nictis[1])
                                en3Turn = False
                                p2Turn = True
                            elif whoAtk == 2:
                                CombatText("Target Party member two\n")
                                enemyDamage = Damage(en2[0], p2[0], weaponAdd, enemyAdd)
                                p2[1] = float(p2[1]) - enemyDamage
                                print("Party member one has been hit for", enemyDamage, "Party member ones health", p2[1])
                                en3Turn = False
                                p2Turn = True 
                            
        if enemies == 1:
            if en1[1] <= 0:
                CombatText("Battle Complete!")
                Nictis[3] = int(Nictis[3] + en1[2])
                Nictis[4] = int(Nictis[4] + en1[3])
                win = True
                break
        elif enemies == 2:
            if en1[1] <= 0 and en2[1] <= 0:
                CombatText("Battle Complete!")
                Nictis[3] = int(Nictis[3] + en1[2] + en2[2])
                Nictis[4] = int(Nictis[4] + en1[3] + en2[3])
                win = True
                break
        elif enemies == 3:
            if en1[1] <= 0 and en2[1] <= 0 and en3[1] <=0:
                CombatText("Battle Complete!")
                Nictis[3] = int(Nictis[3] + en1[2] + en2[2] + en3[2])
                Nictis[4] = int(Nictis[4] + en1[3] + en2[3] + en3[3])
                win = True
                break
def GradualText(dialog):
    for char in dialog:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(.02)
            else:
                time.sleep(.5)
def CombatText(dialog):
    for char in dialog:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(.035)
            else:
                time.sleep(.5)
def Main():
    start = input("poor child, Hit enter to begin (best played in full screen for not text splitting)")
    
    intro = "you see a burning land, your land. \n\
Unknown: come with me little one i'll take care of you.\n\
as the unkown figure grabs you and your sister he fights off others, figures like yourself.\n\
Unknown: Lancelot move! more will come our way, take these two we meet at the river up north!.\n\
15 years pass, you are now the age of 20 under the care of King Aurthor the unknown figure.\n\
your name is Nictis and are now the Kings Care taker.\n\
Squire: My Lord! My Lord!, The kings Councel is called again. we must leave at once!\n\
Aurthor: Again? is it about King Creole? doesn't matter Nictis, Sir Griffon come!\n\
Aurthor: We don't know if force of goblins have moved from our borders Griffon your help will be needed.\n\
Aurthor, yourself, and Sir Griffon make preperations and leave for the Councel. but when you hit the border of the" \
        " kingdom, you are attacked.\n"
    os.system("cls")
    GradualText(intro)
    print("Here are your Stats [srength, Health, lvl, Exp, gold]", Nictis)
    partyUpdate = "\nParty Update! Aurthor and Sir Griffon have joined the party"
    GradualText(partyUpdate)
    party.append("King Aurthor")
    party.append("Sir Griffon")
    playerParty = 3
    print("\n YOU HAVE ENTERED COMBAT!")
    GradualText("Aurthor: I wont be helping you fight this battle, it would make it a bit too easy\n\
Aurthor has left the party!\n\
Aurhtor: It is pretty basic stuff, this goblin wont hurt you bad but if there is a swarm of them you might run into some trouble\n\
Sir Griffon: Don't worry young master, we will swiftly take care of this foe\n\
Nictis: If one goblin isnt that hard, why waste our time?\n\
Sir Griffon: HA! HA! HA! thats the spirt, there are three options we can do in battle\n\
run which is looked down upon, attack is where you strike your opponent, and defending is to take less damage\n\
demonstrate how far you've come, I will deal the killing blow just incase.\n")
    Combat(2, 1, Nictis,Griffon,0, tutorialGoblin,0,0, goblinWeap)
    GradualText("Sir Griffon: You did it young Master!, but I fear we are not in the clear a single Goblin just means there are more\n\
on the way. lets move quickly.\n\
Aurthor: lets.\n")
    GradualText("Aurthor: Wait. Something is off, We arent far from the councle, not seeing anymore goblins is not a good sign\n\
your party continues to move on, until, a large explosion knocks your carriage over.\n\
Nictis: Run!\n\
Aurthor: hunter goblins don't have explosives, I fear it is something larger, I will chase them away.\n\
Sir Griffon: Come Young Master, us staying here would be worse.\n\
Nictis: right lets keep moving.\n\
\n\
as you keep moving onwards with Sir Griffon, you get attacked by 3 goblins!")
    print("\n YOU HAVE ENTERED COMBAT!")
    Combat(2, 3, Nictis, Griffon, 0, hunterGoblin1, hunterGoblin2, hunterGoblin3, goblinWeap)
    LevelUp()
Main()

    
