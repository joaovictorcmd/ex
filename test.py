import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3d3ead3c05d27f6eb1d604befda8b752"

resposta = urllib.request.urlopen(url)  # Request to server

dados = resposta.read()  # Read the response given from server

jsondata = json.loads(dados)

print(jsondata["results"])
