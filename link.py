class Link:
    def __init__(self, titulo, url, ordem, visivel):
        self.titulo = titulo
        self.url = url
        self.ordem = ordem
        self.visivel = visivel

    def ativar(self): #void
        self.visivel = True

    def desativar(self): #void
        self.visivel = False

    def atualizar(self, titulo, url, ordem, visivel): #void
        self.titulo = titulo
        self.url = url
        self.ordem = ordem
        self.visivel = visivel
