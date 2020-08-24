# Logger by andrzej
## Modeon

1. Po sklonowaniu repozytorium, skopiuj plik **config.json** z maila
do katalogu z Dockerfile a następnie zbuduj obraz
`docker build . backend:andrzej`

2. Uruchom dockera: `docker run .`

2. Po uruchomieniu obrazu wykonaj: `curl localhost:5000` 

3. Zobaczysz JSON z dostępnymi endpointami

## Obsługa
Obsługuje metody GET, POST i DELETE. Użycie innych zwróci błąd



