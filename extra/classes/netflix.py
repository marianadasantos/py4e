class Client:
    def __init__(self, name, email, plano):
        self.name = name
        self.email = email
        lista_planos = ['basic', 'premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            print('Invalid')

    def mudar_plano(self, novo_plano):
        if novo_plano in lista_planos:
            print('Seu novo plano é ', )
    
    def ver_filme(self, filme):