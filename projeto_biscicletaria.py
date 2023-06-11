class Biscicleta:
    #CONSTRUTOR
    def __init__(self, cor, modelo, ano, valor):
        #Self é uma referência explícita ao objeto
        #Não é obrigatório usar o nome "self"; pode nomear com "this", por exemplo
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #Método bozinar
    def bozinar(self):
        print("Bike bozinando")

    #Método parar   
    def parar(self):
        print("Bike parando")

    #Método correr   
    def correr(self):
        print("Bike correndo")

    #Imprimindo atributos do objeto
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")


#Declarando um objeto
bike1 = Biscicleta("vermelha", "caloi", 2023, 600)

bike1.parar()
bike1.bozinar()
bike1.correr()

print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)
print(bike1)