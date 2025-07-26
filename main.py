from usuario import Usuario
from link import Link


def criar_usuario():
    print("\nBem-vindo ao Linkhoot!")
    print("Criando um usuário...")
    nomeuser = input("Digite seu nome: ")
    emailuser = input("Digite seu email: ")
    senhauser = input("Digite sua senha: ")
    biouser = input("Digite sua bio: ")
    imagemuser = input("Digite o caminho da sua imagem de perfil: ")
    print("Usuário criado com sucesso!")

    return Usuario(nomeuser, emailuser, senhauser, biouser, imagemuser)
    
def entrar_na_conta(usuario):
    if usuario is None:
        print("Nenhum usuário cadastrado")
        return
    
    print("\n=====Entrando na conta=====")
    emailuser = input("Digite seu email: ")
    senhauser = input("Digite sua senha:")

    if usuario.email == emailuser and usuario.senha == senhauser:
        print(f'Usuário logado com sucesso: {usuario.nome}')
    else:
        print("Falha na autenticação. Verifique seu email e senha.")

def menu_links(usuario):
    while True:
        print("\n=== Menu Linkhoot ===")
        print("1 - Adicionar Link")
        print("2 - Listar Link")
        print("3 - Ativar Links")
        print("4 - Desativar Link")
        print("5 - Sair do Linkhoot")     

        escolha = input("Escolha uma opção: ")
        match escolha:
            case "1":
                titulo = input("Digite o título do link: ")
                url = input("Digite a URL do link: ")
                ordem = len(usuario.links) + 1  
                visivel = input("O link está visível? (s/n): ").lower() == 's'
                novo_link = Link(titulo, url, ordem, visivel)
                usuario.links.append(novo_link)
                print(f"Link '{novo_link.titulo}' adicionado com sucesso!")
            case "2":
                if not usuario.links:
                    print("Nenhum link cadastrado.")
                else:
                    print("\nLinks cadastrados:")
                    for link in usuario.links:
                        status = "Visível" if link.visivel else "Desativado"
                        print(f"{link.ordem}. {link.titulo} - {link.url} ({status})")
            case "3":
                if not usuario.links:
                    print("Nenhum link cadastrado.")
                else:
                    if all(link.visivel for link in usuario.links):
                        print("Todos os links já estão visíveis.")
                    else:
                        for link in usuario.links:
                            if not link.visivel:
                                link.ativar()
                                print(f"Link '{link.titulo}' ativado.")
            case "4":
                if not usuario.links:
                    print("Nenhum link cadastrado.")
                else:
                    links_visiveis = [link for link in usuario.links if link.visivel]
                    if not links_visiveis:
                        print("Todos os links já estão desativados.")
                    else:
                        print("Links visíveis:")
                        for link in links_visiveis:
                            print(f"{link.ordem}. {link.titulo} - {link.url}")
                        try:
                            escolha_ordem = int(input("Digite a ordem do link que deseja desativar: "))
                        except ValueError:
                            print("Entrada inválida. Digite um número válido.")
                            continue  # Volta para o menu
                        
                        link_para_desativar = None
                        for l in links_visiveis:
                            if l.ordem == escolha_ordem:
                                link_para_desativar = l
                                break
                    
                        if link_para_desativar:
                            link_para_desativar.desativar()
                            print(f"Link '{link_para_desativar.titulo}' desativado.")
                        else:
                            print("Ordem inválida ou link já está desativado.")

            case "5":
                print("Saindo do Linkhoot...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

def main():
    usuario = None  

    while True:
        print("\n1 - Criar Usuário")
        print("2 - Entrar na Conta")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")
        match escolha:
            case "1":
                usuario = criar_usuario()
            case "2":
                entrou = entrar_na_conta(usuario)
                break
            case "3":
                print("Saindo...")
                return
            case _:
                print("Opção inválida.")

    menu_links(usuario)

if __name__ == "__main__":
    main()
