from decimal import Decimal
from Calculator import Calculator

calculator = Calculator()
# calculator.help()
# print()

# base damage a spell does (printed damage)
spell_dmg = Decimal(input("Spell DMG: "))
calculator.setSpellDamage(spell_dmg)

# the amount of damage from gear/pets/etc...
player_dmg = Decimal(input("DMG: "))
calculator.setPlayerDamage(player_dmg)

# pierce given by gear/enchants/pets/etc
pierce = Decimal(input("Pierce: "))
calculator.setPierce(pierce)

# enemy resist to the spell's school of damage
enemy_resist = Decimal(input("Enemy Resist: "))
calculator.setEnemyResist(enemy_resist)

while True:
    print()
    print("'help' for list of commands")
    print()
    print("Total:", calculator.getTotal())
    print()
    command = input("Enter a command: ")


    match command:
        case "b":
            try:
                calculator.setBladeList(Decimal(input("Blade value: ")))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        case "rb":
            calculator.removeBlade()

        case "0b":
            calculator.clearBlades()

        case "t":
            try:
                calculator.setTrapList(Decimal(input("Trap value: ")))
            except ValueError:
                print("Invalid input. Please enter a number.")

        case "rt":
            calculator.removeTrap()

        case "0t":
            calculator.clearTraps()

        case "w":
            try:
                calculator.setWeaknessList(Decimal(input("Weakness value: ")))
            except ValueError:
                print("Invalid input. Please enter a number.")

        case "rw":
            calculator.removeWeakness()

        case "0w":
            calculator.clearWeaknesses()

        case "s":
            try:
                calculator.setShieldList(Decimal(input("Shield value: ")))
            except ValueError:
                print("Invalid input. Please enter a number.")

        case "rs":
            calculator.removeShield()

        case "0s":
            calculator.clearShields()

        case "a":
            try:
                calculator.setAura(Decimal(input("Aura Value: ")))
            except ValueError:
                print("Invalid input. Please enter a number.")

        case "0a":
            calculator.clearAura()

        case "bub":
            try:
                calculator.setBubble(Decimal(input("Bubble value: ")))
            except ValueError:
                print("Invalid input. Please enter a number.")

        case "0bub":
            calculator.clearBubble()

        case "00":
            calculator.clearAll()

        case "ns":
            try:
                calculator.setSpellDamage(Decimal(input("Enter new Spell Damage: ")))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")

        case "nd":
            try:
                calculator.setPlayerDamage(Decimal(input("Enter new DMG: ")))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")

        case "np":
            try:
                calculator.setPierce(Decimal(input("Enter new pierce: ")))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")

        case "nr":
            try:
                calculator.setEnemyResist(Decimal(input("Enter new enemy resist: ")))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")

        case "c":
            try:
                calculator.setCritMod(Decimal(input("Enter new crit mod: ")))
            except ValueError:
                print("Invalid input! Please enter a valid decimal number.")

        case "p":
            try:
                calculator.setPierceBladeList(Decimal(input("Pierce blade value: ")))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        case "rb":
            calculator.removePierceBlade()

        case "0b":
            calculator.clearPierceBlades()

        case "check" "c":
            calculator.check()

        case "q":
            break

        case "help":
            calculator.help()

        case _:
            print("Invalid command")
