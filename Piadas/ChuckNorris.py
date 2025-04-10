import requests

base_url = "https://api.chucknorris.io/jokes/random"


def piada_aleatoria():
    url = f'{base_url}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados:
            return dados['value']
        else:
            print('Erro')
    else:
        print(f'Erro: {response.status_code}')


def exbir_categorias():
    url = f'https://api.chucknorris.io/jokes/categories'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados:
            for piadas in dados:
                print(piadas)
            return dados
        else:
            print('erro')
    else:
        print(f'Erro: {response.status_code}')


def buscar_piada_por_palavra(categoria):
    nova_url = f'{base_url}?category={categoria}'
    response = requests.get(nova_url)
    if response.status_code == 200:
        dados = response.json()
        return dados['value']
    else:
        print(f'ERRO: {response.status_code}')


def busca_por_texto_livre(query):
    url = f'https://api.chucknorris.io/jokes/search?query={query}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        resposta = dados.get('result')
        if resposta:
            print(f'Resultado para a {query}:')
            for i, piada in enumerate(resposta[:5],1):
                print(f'{i}. {piada["value"]}')
        else:
            print('ERRO')
    else:
        print(f'ERRO: {response.status_code}')




while True:
    print('''
1. Buscar piada por texto
2. Buscar por categoria
3. Piada aleatória
4. Sair ''')
    try:
        opcoes = int(input('Digite umas dessas opções: '))
    except ValueError:
        print('Digite um numero valido')
        continue

    if opcoes == 1:
        texto = input('Digite um texto livre: ')
        print(busca_por_texto_livre(texto))
    elif opcoes == 2:
        categoria = exbir_categorias()
        escolha = input('Escolha uma categoria dessas acima:').lower().strip()
        if escolha in categoria:
            print(buscar_piada_por_palavra(escolha))
        else:
            print('ERRO: Não existe essa categoria')
    elif opcoes == 3:
        print(piada_aleatoria())

    elif opcoes == 4:
        print('APP Finalizado!!')
        break
    else:
        print('opção invalida')