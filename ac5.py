import random 

def jogo():
    va = 100
    vm = random.randint(60, 80)
    da = random.randint(1, 5)
    atqm = random.randint(20, 30)
    atqa = random.randint(10, 20)
    print("aventureiro: vida -", va, "att -", atqa, "def -", da )
    print("monstro: vida -", vm, "att -", atqm)

    rodada = 0

    while vm > 0 and va > 0: 
        rodada += 1 
        vm = vm - random.randint(1, atqa)
        if vm <= 0:
            print("rodada",rodada)
            print("o monstro morreu!")
        else:
            dano = random.randint(1, atqm) - da
            if dano > 0:             
                va = va - dano
            else:
                va = va - 1  
            if va <=0:
                print("rodada", rodada)
                print("voce morreu!")
            else: 
                print("rodada", rodada)
                print("aventureiro: vida -", va, "att -", atqa, "def -", da )
                print("monstro: vida -", vm, "att -", atqm)

jogo()


