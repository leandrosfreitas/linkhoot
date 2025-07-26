class Usuario:
    def __init__(self, nome, email, senha, bio, imagem_perfil, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.bio = bio
        self.imagem_perfil = imagem_perfil
        self.ativo = ativo
        self.links = []

    def autenticar(self, email, senha):
        if email == self.email and senha == self.senha:
            return True
        return False
