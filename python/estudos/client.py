# how use properly class to do same thing 
class Calculadora():
    def __init__(self,name:str, age: float | None = None, adress: str | None = None):
        self.nome = name
        self.idade = age,
        self.endereco = adress

    def callBackData(self):
        return self.nome, self.idade, self.endereco


portaltil = Calculadora("minecraft",1,1)

print(portaltil.callBackData()[3])       