from pokemon import Pokemon
from random import randint
import math
class Fogo(Pokemon):
    def __init__(self, escolha):
        super().__init__(escolha)
        self.ataques={"(N)arranhar":self.nivel*4,"(F)brasas":self.nivel*7}
        self.tipo="fogo"
        self.fraco="agua"
        self.forte="planta"
        self.vida=math.ceil(12*(self.nivel*1.2))
        self.vida_max=math.ceil(12*(self.nivel*1.2))
    def stats_tipo(self):
        super().stats(1.2,1.5)
    
    def ataque_novo(self,nivel):
        chance = randint(1,100)
        if (nivel == 7) and (chance>=50):
            print(f'Seu pokemon aprendeu o ataque "Explosão de fogo" do tipo de fogo')
            self.ataques['(F)Explosão de fogo'] = math.ceil(self.nivel*20)
        elif (nivel == 7) and (chance<50):
            super().ataque_novo(nivel)
        elif (nivel ==11) and (chance>=50):
            print(f'Seu pokemon aprendeu o ataque "Lança-chamas" do tipo de fogo')
            self.ataques['(F)Lança-chamas'] = math.ceil(self.nivel*35)
        elif (nivel == 11) and (chance<50):
            super().ataque_novo(nivel)
        elif (nivel ==15) and (chance>=50):
            print(f'Seu pokemon aprendeu o ataque "Erupção" do tipo de fogo')
            self.ataques['(F)Erupção'] = math.ceil(self.nivel*57)
        elif (nivel == 15) and (chance<50):
            super().ataque_novo(nivel)
        
    #def dano(self,x,vida_pokemon_inimigo,tipo_ataque):
    #    super().dano(x,vida_pokemon_inimigo,tipo_ataque,self.forte,self.fraco)

class Planta(Pokemon):
    def __init__(self, escolha):
        super().__init__(escolha)
        self.ataques={"(N)arranhar":self.nivel*3,"(P)enraizamento":self.nivel*5}

        self.tipo="planta"
        self.fraco="fogo"
        self.forte="agua"
        
        self.vida=round(12*(self.nivel*1.5))
        self.vida_max=round(12*(self.nivel*1.5))   

    def stats_tipo(self):
        super().stats(1.5, 1.2)

    def ataque_novo(self, nivel):
        chance = randint(1,100)
        if nivel == 7 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Esporos" do tipo de planta!')
            self.ataques['(P)Esporos'] = math.ceil(self.nivel*16)
        elif (nivel == 7) and (chance<50):
            super().ataque_novo(nivel)
        elif nivel == 11 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Lâmina de folhas" do tipo de planta!')
            self.ataques['(P)Lâmina de folhas'] = math.ceil(self.nivel*26)
        elif (nivel == 11) and (chance<50):
            super().ataque_novo(nivel)
        elif nivel == 15 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Chicote de folhas" do tipo de planta!')
            self.ataques['(P)Chicote de folhas'] = math.ceil(self.nivel*37)
        elif (nivel == 15) and (chance<50):
            super().ataque_novo(nivel)
    
    #def dano(self,x,tipo,vida_pokemon_inimigo,tipo_ataque):
    #   super().dano(x,tipo,vida_pokemon_inimigo,tipo_ataque)



# fazer o tipo eletrico - Forte contra agua e fraco contra planta
class Agua(Pokemon):
    def __init__(self, escolha):
        super().__init__(escolha)
        self.ataques={"(N)arranhar":self.nivel*3,"(A)jato dagua":self.nivel*6}

        self.tipo="agua"
        self.fraco="planta"
        self.forte="fogo"
        self.vida=math.ceil(12*(self.nivel*1.3))
        self.vida_max=math.ceil(12*(self.nivel*1.3))

    def stats_tipo(self):
        super().stats(1.3, 1.3)

    def ataque_novo(self, nivel):
        chance = randint(1,100)
        if nivel == 7 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Jato dágua" do tipo de água!')
            self.ataques['(A)Jato dagua'] = math.ceil(self.nivel*26)
        elif (nivel == 7) and (chance<50):
            super().ataque_novo(nivel)
        elif nivel == 11 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Lâmina de água" do tipo de água!')
            self.ataques['(A)Lâmina de água'] = math.ceil(self.nivel*36)
        elif (nivel == 11) and (chance<50):
            super().ataque_novo(nivel)
        elif nivel == 15 and chance >= 50:
            print(f'Seu pokemon aprendeu o ataque "Chicote de água" do tipo de água!') #hidrobomb em ingles
            self.ataques['(A)Chicote de água'] = math.ceil(self.nivel*47)
        elif (nivel == 15) and (chance<50):
            super().ataque_novo(nivel)

    #def dano(self,dano):
    #   super().dano(dano)






















#def batalha(pokemon_contra.tipo,self, dano)
#for k,v in self.ataques.items():
    #if k[1] == "F" and pokemon_contra.tipo==self.fraco:
       # dano = dano*1.3
        #self.vida -= dano
        #print(f'VocÊ tomou {dano} de dano')