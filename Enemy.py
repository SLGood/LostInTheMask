class Enemy(object):

    def __init__(self, name, mask, art, rangedattack, meleeattack,defense, hp, dialogueTree):
        self.name = name
        self.mask = mask
        self.art = art
        self.rangedattack = rangedattack
        self.meleeattack = meleeattack
        self.defense = defense
        self.hp = hp
        self.dialogueTree = dialogueTree


# dumb example:

jock1 = Enemy("Brett", "Jock", "someArt.png", 10, 15, 20, 50, "someDialogueFunc")

jock1.hp = jock1.hp - 5

print(jock1.hp)