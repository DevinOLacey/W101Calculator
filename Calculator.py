from decimal import Decimal


class Calculator:
    # STATIC VALUES
    zero = Decimal('0')
    one = Decimal('1')
    hundred = Decimal('100')
    pointOne = Decimal('0.01')

    # INITIALIZER
    def __init__(self):
        self.spellDamage = self.zero
        self.playerDamage = self.one
        self.critMod = self.one
        self.pierce = self.zero
        self.enemyResist = self.zero
        self.aura = self.one
        self.bubble = self.one
        self.bladeList = []
        self.pierceBladeList = []
        self.trapList = []
        self.weaknessList = []
        self.shieldList = []
        self.shieldMultipliers = []
        self.blades = self.one
        self.weaknesses = self.one
        self.traps = self.one
        self.shields = self.zero
        self.total = self.one

    def __int__(self, playerDamage, pierce):
        self.spellDamage = self.zero
        self.playerDamage = playerDamage
        self.pierce = pierce
        self.critMod = self.one
        self.enemyResist = self.zero
        self.aura = self.one
        self.bubble = self.one
        self.bladeList = []
        self.pierceBladeList = []
        self.trapList = []
        self.weaknessList = []
        self.shieldList = []
        self.shieldMultipliers = []
        self.blades = self.one
        self.weaknesses = self.one
        self.traps = self.one
        self.shields = self.zero
        self.total = self.one




    # SET METHODS
    def setSpellDamage(self, spell_dmg):
        self.spellDamage = spell_dmg

    def setPlayerDamage(self, player_dmg):
        self.playerDamage = self.convertBuff(player_dmg)

    def setCritMod(self, crit):
        self.critMod = self.convertBuff(crit)

    def setPierce(self, pierce):
        self.pierce = self.convertPierce(pierce)

    def setEnemyResist(self, enemy_resist):
        self.enemyResist = self.convertResist(enemy_resist)

    def setBladeList(self, blade):
        self.bladeList.append(self.convertBuff(blade))

    def setPierceBladeList(self, blade):
        self.pierceBladeList.append(self.convertPierce(blade))

    def setTrapList(self, trap):
        self.trapList.append(self.convertBuff(trap))

    def setWeaknessList(self, weakness):
        self.weaknessList.append(self.convertDebuff(weakness))

    def setShieldList(self, shield):
        self.shieldList.append(self.convertShield(shield))
        self.shieldMultipliers.append((self.convertShieldMultiplier(shield)))

    def setAura(self, aura):
        self.aura = self.convertBuff(aura)

    def setBubble(self, bubble):
        self.bubble = self.convertBuff(bubble)



    # CONVERSION METHODS
    def convertBuff(self, buff):
        return self.one + buff * self.pointOne

    def convertDebuff(self, debuff):
        return self.one - debuff * self.pointOne

    def convertPierce(self, pierce):
        return pierce * self.pointOne

    def convertResist(self, resist):
        return resist * self.pointOne

    def convertShield(self, shield):
        return shield * self.pointOne

    def convertShieldMultiplier(self, shield):
        return self.one - Decimal(shield) * self.pointOne

    def convertTempShield(self, shield):
        return self.one - shield

    # DISPLAY METHODS
    def displayBuff(self, buff):
        return self.display_as_int((Decimal(buff) - self.one) * self.hundred)

    def displayDebuff(self, debuff):
        return self.display_as_int((self.one - Decimal(debuff)) * self.hundred)

    def displayBuffs(self, buffList):
        display = []
        for num in buffList:
            display.append((Decimal(num) - self.one) * self.hundred)
        self.display_array_as_int(display)
        return display

    def displayDebuffs(self, debuffList):
        display = []
        for num in debuffList:
            display.append((self.one - Decimal(num)) * self.hundred)
        self.display_array_as_int(display)
        return display

    @staticmethod
    def display_array_as_int(array):
        for index in range(len(array)):
            array[index] = int(array[index])
        return array

    @staticmethod
    def display_as_int(num):
        return int(num)

    # PRINT METHODs
    def check(self):
        print("Spell Damage:", int(self.spellDamage))
        print("Player Damage:", self.displayBuff(self.playerDamage))
        if self.critMod > self.one:
            print("Critical Multiplier:", self.displayBuff(self.critMod))
        print("Pierce:", int(self.pierce * self.hundred))
        print("Enemy Resist:", self.displayDebuff(self.enemyResist))

        if self.aura == 1:
            print("No Aura")
        else:
            print("Aura:", self.displayBuff(self.aura))

        if self.bubble == 1:
            print("No Aura")
        else:
            print("Bubble:", self.displayBuff(self.bubble))

        if len(self.bladeList) > 0:
            print("Blades:", self.displayBuffs(self.bladeList))
        else:
            print("No Blades")

        if len(self.trapList) > 0:
            print("Traps:", self.displayBuffs(self.trapList))
        else:
            print("No Traps")

        if len(self.weaknessList) > 0:
            print("Weaknesses:", self.displayDebuffs(self.weaknessList))
        else:
            print("No Weaknesses")

        if len(self.shieldList) > 0:
            print("Shields:", self.displayDebuffs(self.shieldMultipliers))
        else:
            print("No Shields")

    @staticmethod
    def help():
        print("b\t\tadds a blade\nrb\t\tremoves the value of the last blade\n0b\t\tresets all blade\np\t\tadds a "
              "pierce blade\nrp\t\tremoves the value of the last pierce blade\n0p\t\tresets all pierce "
              "blades\nt\t\tadds a trap\nrt\t\tremoves the value of the last trap\n0t\t\tresets all "
              "traps\nw\t\tadds a weakness\nrw\t\tre adds the value lost from the last weakness\n0w\t\tresets all "
              "weaknesses\ns\t\tadds a shield\nrs\t\tremoves the value of the last shield\0s\t\tresets all "
              "shields\na\t\tadds an aura\n0a\t\tremoves an aura\nbub\t\tadds a bubble\n0bub\tremoves a "
              "bubble\n00\t\tresets ALL buffs and weaknesses\nns\t\tchanges the spells base dmg "
              "value\nnd\t\tchanges the dmg value\nnp\t\tchanges the pierce value\nnr\t\tchanges the resist "
              "value\nc\t\tadds a crit mod\ncheck\tdisplays all current buffs and debuffs\nq\t\tstops the "
              "code")



    # REMOVE METHODS
    def removeBlade(self):
        if len(self.bladeList) > 0:
            self.bladeList.pop()

    def removePierceBlade(self):
        if len(self.pierceBladeList) > 0:
            self.pierceBladeList.pop()
    def removeTrap(self):
        if len(self.trapList) > 0:
            self.trapList.pop()

    def removeWeakness(self):
        if len(self.weaknessList) > 0:
            self.weaknessList.pop()

    def removeShield(self):
        if len(self.shieldList) > 0:
            self.shieldList.pop()
            self.shieldMultipliers.pop()


    # CLEAR METHODS
    def clearBlades(self):
        if len(self.bladeList) > 0:
            self.bladeList.pop()

    def clearPierceBlades(self):
        if len(self.pierceBladeList) > 0:
            self.pierceBladeList.pop()
    def clearTraps(self):
        self.trapList.clear()

    def clearWeaknesses(self):
        self.weaknessList.clear()

    def clearShields(self):
        self.shieldList.clear()
        self.shieldMultipliers.clear()

    def clearAura(self):
        self.aura = self.one

    def clearBubble(self):
        self.bubble = self.one

    def clearAll(self):
        self.clearBlades()
        self.clearPierceBlades()
        self.clearTraps()
        self.clearWeaknesses()
        self.clearShields()
        self.clearAura()
        self.clearBubble()


    # MATH METHODS
    def getTotal(self):
        self.blades = self.getMultiplier(self.bladeList)
        self.traps = self.getMultiplier(self.trapList)
        self.weaknesses = self.getMultiplier(self.weaknessList)
        total = (self.spellDamage * self.playerDamage * self.aura * self.bubble *
                 self.blades * self.traps * self.weaknesses)
        total = self.afterPierce(total)
        return int(total)

    def afterPierce(self, total):
        allShields = self.getTotalValue(self.shieldList)
        tempPierce = self.pierce + self.getTotalValue(self.pierceBladeList)
        tempResist = self.enemyResist
        tempShieldList = self.createTempArray(self.shieldList)
        tempShieldMultipliers = self.createTempArray(self.shieldMultipliers)

        # CHECKS IF YOU CAN PIERCE ALL SHIELDS
        if tempPierce >= allShields:
            tempPierce = tempPierce - allShields
            # CHECKS FOR LEFTOVER PIERCE FOR ENEMIES RESIST
            if tempPierce >= tempResist:
                tempPierce = self.zero
                tempResist = self.zero
            # FINAL CALCULATION IF YOU PIERCED ALL SHIELDS
            total = total * (self.one - (tempResist - tempPierce))
            return total

        # PIERCES ALL SHIELDS ONE AT A TIME
        else:
            while tempPierce > 0:
                tempPierce -= tempShieldList.pop()
                # REMOVES PIERCED SHIELDS
                if tempPierce > 0:
                    tempShieldMultipliers.pop()
                # STORES REMAINING VALUE OF THE SHIELD
                else:
                    tempShieldMultipliers.pop()
                    tempShieldList.append(abs(tempPierce))
                    tempShieldMultipliers.append(self.convertTempShield(abs(tempPierce)))

        self.shields = self.getMultiplier(tempShieldMultipliers)
        total = total * self.shields * (self.one - tempResist)
        return total


    def getMultiplier(self, array):
        multiplier = self.one
        for num in array:
            multiplier *= num
        return multiplier

    def getTotalValue(self, array):
        total = self.zero
        for num in array:
            total += num
        return total

    @staticmethod
    def createTempArray(array):
        tempArray = []
        for num in array:
            tempArray.append(num)
        return tempArray

























