# Logger by andrzej
Modeon

## Uruchomienie
1. Po sklonowaniu repozytorium, skopiuj plik **config.json** z maila
do katalogu z Dockerfile a następnie zbuduj obraz
`docker build . backend:andrzej`

2. Uruchom dockera: `docker run . -p 5000:5000/tcp -p 5000:5000/udp`
3. Po uruchomieniu obrazu wykonaj: `curl localhost:5000` 
4. Zobaczysz JSON z dostępnymi endpointami

jeżeli Docker nie zadziała:

1. Utwórz nowy virtualenv
2. Sklonuj repo do pliku src
3. Zainstaluj pakiety z pliku requirements.txt
4. Ustaw zmienne środowiskowe:
    `export FLASK_APP=logger`
    `export FLASK_ENV=development`
5. Przejdz do katalogu nadrzędnego dla src (we włączonym venvie)
6. Uruchom `flask run`
7. `curl localhost:5000` zwróci listę endpointów

## Obsługa
Obsługuje metody GET i POST 
GET do wyświetlania, POST do tworzenia nowych danych

przykładowe payloady w katalogu **test_payloads**

nie działa zagnieżdżanie komentarzy do logów, i nie jest pozabezpieczany :(

