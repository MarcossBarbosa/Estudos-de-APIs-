import requests

API_KEY = "7858ec9f4a163922bf3b769ba059c350"
BASE_URL = "https://api.themoviedb.org/3"

def buscar_filme(titulo):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": titulo,
        "language": "pt_br"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        dados = response.json()
        if dados["results"]:
            for filme in dados["results"][:5]:
                print(f'Título: {filme['title']} ({filme['release_date'][:4]})')
                print(f'Sinopse: {filme['overview']}')
                print(f'Nota: {filme['vote_average']}/10')
                print('-' *50)
        else:
            print('Nenhum filme encontrado')
    else:
        print(f'Erro: {response.status_code}')

buscar_filme('Vingadores')