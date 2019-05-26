# Indeksownik
Odkoduj indeksy

##### Podaj indeksy oraz bazę plików z indeksami, a program automatycznie utworzy plik, który odkoduje te indeksy czyli pokaże imię i nazwisko osoby pod tym indeksem oraz pokaże na jakim kierunku studiuje.
***


### Format pliku z bazą danych
Jest to plik o rozszerzeniu .csv

Dane muszą być w formacie:

**Pierwszy wiersz powinien zawierać nazwy kolumn:**

Pełny indeks,Indeks,Imię,Imię 2,Nazwisko,Kierunek 1,Specjalność 1,Kierunek 2,Specjalność 2

### Format pliku z indeksami do wyszukania
Są to po prostu numery indeksów w nowych linijkach zapisane do zwykłego pliku tekstowego
***

### Działanie programu
**Wymagany jest Python3 **

Aby uruchomić program należy pobrać zawartośc repozytorium a następnie będąc w katalogu tego repozytorium należy wpisać komendę:

*python3 script.py baza.csv indeksy.txt*

Wygeneruje to plik "wynik.csv" który zawiera szukane przez nas indeksy wraz z danymi
