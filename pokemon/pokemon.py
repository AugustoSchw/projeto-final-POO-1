import math
from random import randint

def tentar_int(x):
    while True:
        try:
            x = int(x)
            return(x)
        except ValueError:
            x = input(f'O resultado deve ser um número!')
            continue

desenho_pokemons = {"charmander": """⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬛🟧⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬛🟧🟧⬛⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬜⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜
⬜⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🟧⬛🟧🟧⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟨🟨🟨⬛⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧🟧🟧⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
""", "squirtle": """⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🏿⬛⬛⬜⬛🟦🟦🟦⬛🟦🟦⬛
⬛🟫🟦🟦🟦🟦🟦🟦🟦🟦🏿🟫🏿⬛🟦🟦🟦⬛🟦🟦🟦⬛
⬛🟦🟦🟦🟦⬜⬛🟦🟦🟦🏽🟫🟫🏿⬛🟦🟦⬛🟦🟦⬛⬜
⬛🟦🟦🟦🟦⬛🟫🟦🟦🟦⬜🟫🟫🟫⬛🟦⬛⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟫🟦🟦🟦⬛⬜⬜🟫🟫⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨⬛🟦🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🏽🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟦⬛🟫🟨🟨🟨🟫⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟫🟫🟦⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜

""","bulbassauro":"""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
"""}
#vantangens_tipos=[['agua','fogo'],['planta','agua'],['fogo','planta']]

pokedex={'charmander': "fogo", 'squirtle': "agua", 'bulbassauro': "planta"}

class Pokemon:
    def __init__(self,escolha):
        self.nivel=3
        self.xp_up=12
        self.xp=0
        self.pp1=10
        self.pp2=8
        self.pp3=6
        self.pp4=4
        self.pp5=2
        
        if escolha in pokedex:
            self.raca = escolha
            self.ascii = desenho_pokemons[escolha]
        if escolha==1:
            #self.nivel=3
            #self.xp_up=12
            #self.xp=0
            #self.vida=math.ceil(12*(self.nivel*1.2))
            #self.vida_max=math.ceil(12*(self.nivel*1.2))
            #self.tipo="fogo"
            #self.fraco="agua"
            self.ascii=desenho_pokemons["charmander"]
            #self.ataques={"(N)arranhar":self.nivel*4,"(F)brasas":self.nivel*7}
            #self.dano_ataque1=self.nivel*4
            #self.dano_ataque2=self.nivel*7
            self.raca="charmander"
        if escolha==2:
            #self.nivel=3
            #self.xp_up=12
            #self.xp=0
            #self.vida=math.ceil(13*(self.nivel*1.2))
            #self.vida_max=math.ceil(13*(self.nivel*1.2))
            #self.tipo="agua"
            #self.fraco="planta"
            #self.ataques={"(N)caudada":math.ceil(self.nivel*3.5),"(A)bolhas": math.ceil(self.nivel*6.2)}
            #self.dano_ataque1=math.ceil(self.nivel*3.5)
            #self.dano_ataque2=math.ceil(self.nivel*6.2)
            self.ascii=desenho_pokemons["squirtle"]
            self.raca="squirtle"
        if escolha==3:
            #self.nivel=3
            #self.vida=math.ceil(15*(self.nivel*1.2))
            #self.vida_max=math.ceil(15*(self.nivel*1.2))
            #self.xp_up=12
            #self.xp=0
            #self.tipo="planta"
            #self.fraco="fogo"
            self.ascii=desenho_pokemons["bulbassauro"]
            #self.ataques={"(N)caudada":math.ceil(self.nivel*3.2),"(P)floreio": math.ceil(self.nivel*5.7)}
            #self.dano_ataque1=math.ceil(self.nivel*3.2)
            #self.dano_ataque2=math.ceil(self.nivel*5.7)
            self.raca="bulbassauro"

    def escolha_nome(self):
        self.nome=input("Dê um nome para o seu pokemon!\n: ")
        if self.nome == "":
            self.nome = self.raca
    def printar(self):
        print(f'{self.ascii}\n {"-"*8} {self.nome} {"-"*8}\nRaça do pokemon: {self.raca}\nTipo do pokemon: {self.tipo}\nVida atual: {self.vida}\nNível de batalha: {self.nivel}')
    def dano(self,x,vida_pokemon_inimigo,tipo_ataque,forte,fraco):
        if vida_pokemon_inimigo<=0:
            print(f'O pokemon inimigo desmaiou!\n')
            return
        if tipo_ataque == fraco:
            x = math.ceil(x*1.3)
            self.vida -= x
            print(f'------------------------------------\nAtaque efetivo! {x} pontos de dano!      \n------------------------------------')
        elif (tipo_ataque == forte) or (tipo_ataque == self.tipo):
            x = math.ceil(x*0.7)
            self.vida -= x
            print(f'------------------------------------\nAtaque ineficiente! {x} pontos de dano!      \n------------------------------------')
        else:
            self.vida -= math.ceil(x)
            print(f'------------------------------------\nAtaque normal! {x} pontos de dano!      \n------------------------------------')
        
    def ganho_xp(self,nivel_adversario):
        self.xp+= math.ceil((nivel_adversario*1.2)) ##lembrar de alterar para 1.2
    def subida_nivel(self):
        if self.xp >= self.xp_up:
            self.nivel+=1
            self.xp=0 #sempre vai pro proximo nivel com 0 de xp, arrumar.
            self.xp_up=self.xp_up*1.2
            self.stats_tipo()
            self.ataque_novo(self.nivel)

    def stats(self,multVida,multDano):

        self.vida=math.ceil(self.vida*multVida)
        self.vida_max=math.ceil(self.vida_max*multVida)
        for k,v in self.ataques.items():
            self.ataques[k]=math.ceil(v*multDano)

    def curar(self,qnt):
        if self.vida+qnt>self.vida_max:
            self.vida=self.vida_max
        else:
            self.vida+=qnt
    def pokecenter(self):
        self.vida=self.vida_max
        self.pp1=10
        self.pp2=8
        self.pp3=6
        self.pp4=4
        self.pp5=2

    def ataque_novo(self, nivel):
        if (nivel == 7):
            print(f'Seu pokemon aprendeu o ataque "Investida" do tipo normal!')
            self.ataques['(N)Investida'] = math.ceil(self.nivel*8.5)
        if (nivel == 11):
            print(f'Seu pokemon aprendeu o ataque "Mordida" do tipo normal!')
            self.ataques['(N)Mordida'] = math.ceil(self.nivel*8.5)
        if (nivel == 15):
            print(f'Seu pokemon aprendeu o ataque "Explosão" do tipo normal!')
            self.ataques['(N)Explosão'] = math.ceil(self.nivel*8.5)

    def captura(self,vida_pokemon_inimigo,vida_maxima_pokemon_inimigo):
        chance = randint(1, 100)
        if vida_pokemon_inimigo <=vida_maxima_pokemon_inimigo*0.25:
            if chance <=75:
                return "S"
            else:
                return "N"
        else:
            if chance <= 50:
                return "S"
            else:
                return "N"
            

#itens=[['Pokebola',15],['Pocao pequena de cura',20],['Pocao media de cura',35]]
itens_preco = {'Pokebola': 15, 'Pocao pequena de cura': 20, 'Pocao media de cura': 35}
consumiveis_ganho= {'Pocao pequena de cura': 40}
class Jogador:
    def __init__(self):
        self.moedas=20
        #self.inventario=['Pocao pequena de cura','Pocao pequena de cura','Pocao media de cura','Pokebola', 'Pokebola', 'Pokebola'] ###append
        self.inventario = {'Pokebola': 3, 'Pocao pequena de cura': 2, 'Pocao media de cura': 1}
    def loja(self):
        for i,(k,v) in enumerate(itens_preco.items()):
            if i == 0:
                print(f'\nSuas moedas: {self.moedas}\nDigite o número correspondente ao item que deseja comprar!(caso queira voltar, digite 9)\nLoja:\n{i+1}){k}: {v} moedas\n')
            elif i!= len(itens_preco)-1:
                print(f'{i+1}){k}: {v} moedas\n')
            else:
                print(f'{i+1}){k}: {v} moedas\n')
                compra=input(f': ')
                compra = tentar_int(compra)
                if compra == 9:
                    return
                while (compra < 1) or (compra > 3):
                    compra=input(f': ')
                    compra = tentar_int(compra)
            
        if compra == 9:
            return
        #compra=itens_preco[compra-1]
        for i, (k, v) in enumerate(itens_preco.items()):
            if compra - 1 == i:
                if self.moedas < v:
                    print(f'Você não tem moedas suficientes para comprar esse item!')
                    return
                self.inventario[k] += 1
                self.moedas -= v
                
        #for i in range(len(itens)):
            #if itens[i][0] == compra:
                #if  self.moedas < itens[i][1]:
                #    print(f'Você não tem moedas suficientes para comprar esse item!')
                #    return
                #self.inventario.append(itens[i][0])
                #self.moedas+= -(itens[i][1])
                #print(self.moedas,self.inventario)
    def usar_itens(self):
        for i, (k,v) in enumerate(self.inventario.items()):
            if i == 0:
                print(f'Escolha o número do item que você quer usar:\n')
                print(f'{i+1}) {k} ({v} restantes)')
            else:
                print(f'{i+1}) {k} ({v} restantes)')
            if i==len(self.inventario)-1:           ##!!!
                escolher_item=input(f'Escolha o número do item que você quer usar:\n')
                escolher_item = tentar_int(escolher_item) - 1
                while (escolher_item < 0) or (escolher_item > 2):
                    escolher_item=input(f'Escolha o número do item que você quer usar:\n')
                    escolher_item = tentar_int(escolher_item) - 1
                
        for i, (k,v) in enumerate(self.inventario.items()):
            if escolher_item == i:
                if self.inventario[k] -1 < 0:
                    print(f'Você não tem esse item, passe no mercado para comprar!')
                    return 0
                if k == "Pokebola":
                    self.inventario[k] -= 1
                    return "captura"
                else:
                    self.inventario[k] -= 1
                    return itens_preco[k]
                
    def moedas_vitoria(self,nivel_inimigo):
        self.moedas+= math.ceil(nivel_inimigo*5)