import random

gForte = random.randint(1, 21)
gFraco = random.randint(6, 12)
print('Você está andando pela floresta e se depara com um goblin sorrateiro, ela pula enfurecidamente pra cima de você, com um bom reflexo você desvia e contra-ataca')
print()
print('Como você prefere atacar? Com um golpe certeiro porem mediano, ou um golpe forte mas desajustado?')
atk = int(input('1 para golpe mediano e 2 para golpe forte:'))
if atk == 1:
    print('Você aproveita a brecha para dar um golpe certeiro, o seu golpe causou {} de dano!!'.format(gFraco))
else:
    print('Prevendo os movimentos do goblin você desvia e consegue se preparar para um golpe potente! Você causou {} de dano'.format(gForte))
