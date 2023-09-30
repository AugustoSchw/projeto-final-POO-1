from pokemon import Pokemon, Jogador
from pokemon_tipos import Fogo, Planta, Agua
from random import randint
import math

def media_niveis(lista_pokemons):
    qnt_pokemons=0
    media=0
    for i in range(len(lista_pokemons)):
        qnt_pokemons+=1
        media+= lista_pokemons[i].nivel
    return math.ceil(media/qnt_pokemons)

def tentar_int(x):
    while True:
        try:
            x = int(x)
            return(x)
        except ValueError:
            x = input(f'O resultado deve ser um número!')
            continue



def sigla_para_tipo(x):
    if x=="N":
        return "normal"
    elif x=="F":
        return "fogo"
    elif x=="A":
        return "agua"
    else:
        return "planta"
    
def ataque():
    for i, (k, v) in enumerate(meu_pokemon.ataques.items()):
        if i==0:
            escolha_ataque=input("Selecione o número que corresponde ao ataque desejado: ")
            escolha_ataque=tentar_int(escolha_ataque)
            while ((escolha_ataque) < 1) or (escolha_ataque > len(meu_pokemon.ataques)):
                escolha_ataque=input("Selecione o número que corresponde ao ataque desejado: ")
                escolha_ataque= tentar_int(escolha_ataque)
            escolha_ataque=escolha_ataque - 1
        #escolha_ataque=escolha_ataque-1 
        if (i==0) and (escolha_ataque==i):
            if meu_pokemon.pp1>=1:
                dano = v
                tipo_dano_ataque = sigla_para_tipo(k[1])
                meu_pokemon.pp1-=1
                return dano, tipo_dano_ataque
            else:
                print(f'O pokemon não consegue mais usar essa habilidade!')
                return ataque()
        if (i==1) and (escolha_ataque==i): 
            if meu_pokemon.pp2>=1:
                dano = v
                tipo_dano_ataque = sigla_para_tipo(k[1])
                meu_pokemon.pp2-=1
                return dano, tipo_dano_ataque
            else:
                print(f'O pokemon não consegue mais usar essa habilidade!')
                return ataque()
        if (i==2) and (escolha_ataque==i): 
            if meu_pokemon.pp3>=1:
                dano = v
                tipo_dano_ataque = sigla_para_tipo(k[1])
                meu_pokemon.pp3-=1
                return dano, tipo_dano_ataque
            else:
                print(f'O pokemon não consegue mais usar essa habilidade!')
                return ataque()
        if (i==3) and (escolha_ataque==i): 
            if meu_pokemon.pp4>=1:
                dano = v
                tipo_dano_ataque = sigla_para_tipo(k[1])
                meu_pokemon.pp4-=1
                return dano, tipo_dano_ataque
            else:
                print(f'O pokemon não consegue mais usar essa habilidade!')
                return ataque()
        if (i==4) and (escolha_ataque==i): 
            if meu_pokemon.pp5>=1:
                dano = v
                tipo_dano_ataque = sigla_para_tipo(k[1])
                meu_pokemon.pp5-=1
                return dano, tipo_dano_ataque
            else:
                print(f'O pokemon não consegue mais usar essa habilidade!')
                return ataque()

    
### -de 70% da vida, 70% de chance de capturar
#como capturar: nome_lista_pokemons.append(pokemon_contra)
meuspokemons=[]
meuspokemonsPC=[]
pokedex={'charmander': "fogo", 'squirtle': "agua", 'bulbassauro': "planta", "zapdos": "eletrico"}
#fazer um for com a lista de pokemons como range e executar a cura em cada objeto
#for v in meus_pokemons:
#   v.pokestop() ---------------------- Tem isso no arquivo testealeatorio

player=Jogador()
escolha=input("Escolha o seu pokemon: \n1)Charmander\n2)Squirtle\n3)Bulbassauro\n: ")
escolha = tentar_int(escolha)

if escolha == 1:
    meu_pokemon=Fogo("charmander")
elif escolha == 2:
    meu_pokemon=Agua("squirtle")
elif escolha == 3:
    meu_pokemon=Planta("bulbassauro")
meuspokemons.append(meu_pokemon)

print(meu_pokemon.ascii)
meu_pokemon.escolha_nome()

treinador_1_derrotado=False
aparicao_treinador_1 = False
treinador_1_pokemons=[]
while True:
    if media_niveis(meuspokemons) >= 3 and (treinador_1_derrotado==False):
        if aparicao_treinador_1 == False:
            print("Um treinador pokemon apareceu na cidade! Se quiser lutar contra ele, escolha a opção correspondente")
            caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/treinador/meus pokemons): ')
            while (caminho!="mercado") and (caminho!="batalhar") and (caminho!="pokecenter") and (caminho!="PC") and (caminho!="treinador" and (caminho!="meus pokemons")):
                caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/treinador/meus pokemons): ')
            aparicao_treinador1 = True
        else:
            caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/treinador/meus pokemons): ')
            while (caminho!="mercado") and (caminho!="batalhar") and (caminho!="pokecenter") and (caminho!="PC") and (caminho!="treinador") and (caminho!="meus pokemons"):
                caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/treinador/meus pokemons): ')
    else:
        caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/meus pokemons): ')
        while (caminho!="mercado") and (caminho!="batalhar") and (caminho!="pokecenter") and (caminho!="PC" and (caminho!="meus pokemons")):
            caminho=input(f'Escolha entre ir ao mercado para comprar suprimentos ou batalhar(mercado/batalhar/pokecenter/PC/meus pokemons): ')

    
        #while len(pokemons_treinador_1)>1:
         #   x = len(pokemons_treinador_1)
            
    if caminho == "meus pokemons":
        if len(meuspokemons)>0:
            for i in range(len(meuspokemons)):
                print(f'{i+1}) {meuspokemons[i].raca} de nivel {meuspokemons[i].nivel}')
            mudanca_pokemon=input(f'Escolha o número do pokemon que você deseja alterar o nome ou retirar do seu time: ')
            mudanca_pokemon=tentar_int(mudanca_pokemon)
            escolha_pokemon = input(f'Escolha a funcao que deseja: \n1:Alterar Nome\n2: Libertar para a natureza')
            escolha_pokemon = tentar_int(escolha_pokemon)
            if escolha_pokemon == 1:
                meu_pokemon.escolha_nome()
                continue
            elif escolha_pokemon == 2:
                if len(meuspokemons) == 1:
                    print("Você não pode libertar seu único pokemon")
                    continue
                else:
                    meuspokemons.pop(meuspokemons[mudanca_pokemon])
                    continue
                    
    
    if caminho == "PC":
        if len(meuspokemonsPC)>0:
            for i in range(len(meuspokemonsPC)):
                print(f'{i+1}) {meuspokemonsPC[i].raca} de nivel {meuspokemonsPC[i].nivel}')
            select = int(input("Selecione o pokemon que deseja incluir no bando: \n")) - 1
            for i in range(len(meuspokemons)):
                print(f'{i+1}) {meuspokemons[i].raca} de nivel {meuspokemons[i].nivel}')
            trocar = int(input("Selecione o pokemon que deseja retirar no bando: \n")) - 1
            x = meuspokemons[trocar] 
            meuspokemons[trocar] = meuspokemonsPC[select]
            meuspokemonsPC[select] = x
        else:
            print("Você não tem pokemons no PC!")
            continue
        
    if caminho=="mercado":
        player.loja()
        continue
    if caminho=="batalhar":
        chance=randint(1,3)
        for i, (k,v) in enumerate(pokedex.items()):
            if i + 1 == chance:
                if v == "fogo":
                    pokemon_contra = Fogo(k)
                if v == "agua":
                    pokemon_contra = Agua(k)
                if v == "planta":
                    pokemon_contra = Planta(k)
    
    if caminho == "treinador":
        pokemons_treinador_1 = []
        while len(pokemons_treinador_1) < 3:
            for i, (k,v) in enumerate(pokedex.items()):
                chance = randint(0,2)
                if i == 3:
                    break
                if i == chance:
                    if v == "fogo":
                        pokemon_contra = Fogo(k)
                    if v == "agua":
                        pokemon_contra = Agua(k)
                    if v == "planta":
                        pokemon_contra = Planta(k)
                    for i in range(5 - pokemon_contra.nivel):
                        pokemon_contra.stats_tipo()
                        pokemon_contra.nivel += 1
                    pokemons_treinador_1.append(pokemon_contra)
        pokemon_contra = pokemons_treinador_1[0]
            
        for i in range(len(pokemons_treinador_1)):
            print(f'{i+1}) {pokemons_treinador_1[i].raca} de nivel {pokemons_treinador_1[i].nivel}')
                
            
            
              
    if caminho=="pokecenter":
        for i in range(len(meuspokemons)):
            meuspokemons[i].pokecenter()
        print('Seu pokemon foi recuperado !')
    while (pokemon_contra.vida>0) and caminho == "batalhar":
        print(f'\nhp: {pokemon_contra.vida}\n\n{pokemon_contra.ascii}\n\n')
        print(f'--------------------------------------------\n Vida de {meu_pokemon.nome}: {meu_pokemon.vida}\n--------------------------------------------\nMoedas:{player.moedas}')
        acao=input(f'-------   -------   -------   ----------\n/ATACAR/  /FUGIR/   /ITENS/   /POKEMONS/\n-------   -------   -------   ----------\n: ')
        if acao=="itens":
            if len(player.inventario) >0:
                item_escolhido=player.usar_itens()
                if type(item_escolhido) == int:
                    meu_pokemon.curar(item_escolhido)
                    if item_escolhido ==0:
                        continue
                else:
                    pokebola_chance = getattr(meu_pokemon, item_escolhido) 
                    resultado_pokebola = pokebola_chance(pokemon_contra.vida,pokemon_contra.vida_max)
                    if resultado_pokebola == "S":
                        print(f'Você capturou um {pokemon_contra.raca} de nivel {pokemon_contra.nivel}')
                        alterar_nome=input("Você deseja dar um nome ao seu novo pokemon?(S/N)").upper()
                        if alterar_nome =="S":
                            pokemon_contra.escolha_nome()
                            if len(meuspokemons) < 6:
                                meuspokemons.append(pokemon_contra)
                            else:
                                print("O bando já está cheio, seu pokemon foi enviado para o PC!")
                                meuspokemonsPC.append(pokemon_contra)
                        else:
                            pokemon_contra.nome = pokemon_contra.raca
                            if len(meuspokemons) < 6:
                                meuspokemons.append(pokemon_contra)
                            else:
                                print("O bando já está cheio, seu pokemon foi enviado para o PC!")
                                meuspokemonsPC.append(pokemon_contra)
                        break
                    else:
                        print(f'Você não conseguiu capturar o pokemon!')
            else:
                print(f'Você não tem itens no seu inventário!')
                continue
                
        if (acao!="fugir") and (acao!="atacar") and (acao!="itens") and (acao!="pokemons"):
            continue
        if acao=="fugir":
            chance=randint(0,100)
            if chance<=90:
                print("Conseguiu escapar!")
                break
            else:
                print("Não conseguiu escapar")
        if acao =="atacar":
            #x=0 #O numero de cada ataque (p/ formatacao)
            for i,(k,v) in enumerate(meu_pokemon.ataques.items()):
                string="pp" + str(i+1)
                print(f'{i+1}){k}: {v} dano\n {getattr(meu_pokemon, string)} ataques restantes\n')  #Primeira variavel pega o nome do objt e a segunda faz um objt.segundaVariavel e analisa se ela existe no objeto
            #escolha_ataque=int(input("Selecione o número que corresponde ao ataque desejado: "))
            #escolha_ataque=escolha_ataque-1 
            dano, tipo_dano_ataque = ataque()
            pokemon_contra.dano(dano,meu_pokemon.vida, tipo_dano_ataque, pokemon_contra.forte, pokemon_contra.fraco) 
            

        if acao == "pokemons":
            for i in range(len(meuspokemons)):
                print(f'{i+1}) {meuspokemons[i].raca} de nivel {meuspokemons[i].nivel} / HP: {meuspokemons[i].vida}')
            selecionar_pokemon = input("Selecione o pokemon desejado: ")
            selecionar_pokemon = tentar_int(selecionar_pokemon)
            meu_pokemon = meuspokemons[selecionar_pokemon-1] ##Teste nao sei se funciona
            continue
   
        escolha_ataque_inimigo=randint(0, len(pokemon_contra.ataques.items()) - 1)

      
        

        for i, (k, v) in enumerate(pokemon_contra.ataques.items()):
               
                if escolha_ataque_inimigo == i:
                    dano = v
                    tipo_dano_ataque = sigla_para_tipo(k[1])
                    break

        print(f'\nTurno do inimigo:\n')
        meu_pokemon.dano(dano,pokemon_contra.vida,tipo_dano_ataque, meu_pokemon.forte, meu_pokemon.fraco)
        
        if meu_pokemon.vida<=0:
            for i in range(len(meuspokemons)):
                if meuspokemons[i].vida>0:
                    meuspokemons[i]=meu_pokemon
            
            contador = 0
            for i in range(len(meuspokemons)):
                if meuspokemons[i].vida <= 0:
                    contador += 1
            if contador == len(meuspokemons):
                print(f'Infelizmente a vida de todos os pokemons chegou a 0, você será enviado ao pokecenter!')
                for i in range(len(meuspokemons)):
                    meuspokemons[i].pokecenter()
                contador = 0
                break
        if pokemon_contra.vida<=0:
            meu_pokemon.ganho_xp(pokemon_contra.nivel)
            meu_pokemon.subida_nivel()
            player.moedas_vitoria(pokemon_contra.nivel)
            print(f'nivel = {meu_pokemon.nivel} // xp = {meu_pokemon.xp}')
            media_pokemons = media_niveis(meuspokemons)
            print(media_pokemons)
    
    while (pokemon_contra.vida>0) and (caminho == "treinador") and (len(pokemons_treinador_1) > 0):
        print(f'\nhp:{pokemon_contra.raca}: {pokemon_contra.vida}\n\n{pokemon_contra.ascii}\n\n')
        print(f'--------------------------------------------\n Vida de {meu_pokemon.nome}: {meu_pokemon.vida}\n--------------------------------------------\nMoedas:{player.moedas}')
        acao=input(f'-------   -------   -------   ----------\n/ATACAR/  /FUGIR/   /ITENS/   /POKEMONS/\n-------   -------   -------   ----------\n: ')
        if acao=="itens":
            if len(player.inventario) >0:
                item_escolhido=player.usar_itens()
                if type(item_escolhido) == int:
                    meu_pokemon.curar(item_escolhido)
                    if item_escolhido ==0:
                        continue
                else:
                    print("Você não pode capturar o pokemon de outro treinador!")
                    continue
            else:
                print(f'Você não tem itens no seu inventário!')
                continue
                
        if (acao!="fugir") and (acao!="atacar") and (acao!="itens") and (acao!="pokemons"):
            continue
        if acao=="fugir":            
            print("Conseguiu escapar!")
            break

        if acao =="atacar":
            #x=0 #O numero de cada ataque (p/ formatacao)
            for i,(k,v) in enumerate(meu_pokemon.ataques.items()):
                string="pp" + str(i+1)
                print(f'{i+1}){k}: {v} dano\n {getattr(meu_pokemon, string)} ataques restantes\n')  #Primeira variavel pega o nome do objt e a segunda faz um objt.segundaVariavel e analisa se ela existe no objeto
            #escolha_ataque=int(input("Selecione o número que corresponde ao ataque desejado: "))
            #escolha_ataque=escolha_ataque-1 
            dano, tipo_dano_ataque = ataque()
            pokemon_contra.dano(dano,meu_pokemon.vida, tipo_dano_ataque, pokemon_contra.forte, pokemon_contra.fraco) 
            

        if acao == "pokemons":
            for i in range(len(meuspokemons)):
                print(f'{i+1}) {meuspokemons[i].raca} de nivel {meuspokemons[i].nivel} / HP: {meuspokemons[i].vida}')
            selecionar_pokemon = input("Selecione o pokemon desejado: ")
            selecionar_pokemon = tentar_int(selecionar_pokemon)
            meu_pokemon = meuspokemons[selecionar_pokemon-1] ##Teste nao sei se funciona
            continue
        
        escolha_ataque_inimigo=randint(0, len(pokemon_contra.ataques.items()) - 1)

      


        for i, (k, v) in enumerate(pokemon_contra.ataques.items()):
                
                if escolha_ataque_inimigo == i:
                    dano = v
                    tipo_dano_ataque = sigla_para_tipo(k[1])
                    break

        print(f'\nTurno do inimigo:\n')
        meu_pokemon.dano(dano,pokemon_contra.vida,tipo_dano_ataque, meu_pokemon.forte, meu_pokemon.fraco)
        
        if meu_pokemon.vida<=0:
            for i in range(meuspokemons):
                if meuspokemons[i].vida>0:
                    meuspokemons[i]=meu_pokemon
            
            contador = 0
            for i in range(meuspokemons):
                if meuspokemons[i].vida == 0:
                    contador += 1
            if contador == len(meuspokemons):
                print(f'Infelizmente a vida de todos os pokemons chegou a 0, você será enviado ao pokecenter!')
                for i in range(len(meuspokemons)):
                    meuspokemons[i].pokecenter()
                contador = 0
                break
        if pokemon_contra.vida<=0:
            meu_pokemon.ganho_xp(pokemon_contra.nivel)
            meu_pokemon.subida_nivel()
            player.moedas_vitoria(pokemon_contra.nivel)
            print(f'nivel = {meu_pokemon.nivel} // xp = {meu_pokemon.xp}')
            media_pokemons = media_niveis(meuspokemons)
            if len(pokemons_treinador_1) > 0:
                pokemons_treinador_1.pop(pokemon_contra)
                if len(pokemons_treinador_1) > 0:
                    pokemon_contra = pokemons_treinador_1[0]
                else:
                    print("Parabéns, você venceu a batalha e concluiu o jogo!!!")
                    exit()
            print(media_pokemons)
        
        