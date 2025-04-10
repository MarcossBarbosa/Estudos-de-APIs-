import  requests

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


categoria = exbir_categorias()
escolha = input('Escolha uma categoria dessas acima: ou digite aleatoria: ').lower().strip()

if escolha in categoria:
    print(buscar_piada_por_palavra(escolha))
elif escolha == 'aleatoria':
    print(piada_aleatoria())
else:
    print('ERRO: Não existe essa escolha')