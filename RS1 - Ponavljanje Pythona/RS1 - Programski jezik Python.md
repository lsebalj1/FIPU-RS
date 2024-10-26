# Raspodijeljeni sustavi (RS)

**Nositelj**: doc. dr. sc. Nikola Tanković  
**Asistent**: Luka Blašković, mag. inf.

**Ustanova**: Sveučilište Jurja Dobrile u Puli, Fakultet informatike u Puli

<img src="https://raw.githubusercontent.com/lukablaskovic/FIPU-PJS/main/0.%20Template/FIPU_UNIPU.png" style="width:40%; box-shadow: none !important; "></img>

# (1) Programski jezik Python

<img src="./RS_01.png" style="width:9%; border-radius: 8px; float:right;"></img>

<div style="float: clear; margin-right:5px;">Raspodijeljeni sustav je svaki računalni sustav koji se sastoji od više povezanih autonomnih računala koji zajedno rade kao jedinstveni kohezivni sustav za postizanje zajedničkog cilja. Drugim riječima, raspodijeljeni sustavi su skupina nezavisnih računala (čvorova u mreži) koji međusobno komuniciraju i koordiniraju svoje radnje kako bi izvršili određeni zadatak. Na ovom kolegiju studenti će se upoznati s osnovama raspodijeljenih sustava i njihovim karakteristikima, tehnologijama i alatima koji se koriste u njihovom razvoju te naučiti kako razvijati aplikacije s naglaskom na distribuiranu arhitekturu.</div>
<br>

**🆙 Posljednje ažurirano: 25.10.2024.**

## Sadržaj

- [Raspodijeljeni sustavi (RS)](#raspodijeljeni-sustavi-rs)
- [(1) Programski jezik Python](#1-programski-jezik-python)
  - [Sadržaj](#sadržaj)
- [1. Uvod](#1-uvod)
- [2. Priprema Python okruženja](#2-priprema-python-okruženja)
  - [2.1 Instalacija Pythona](#21-instalacija-pythona)
  - [2.2 Priprema virtualnog okruženja](#22-priprema-virtualnog-okruženja)
    - [2.2.1 Instalacija `conda` alata](#221-instalacija-conda-alata)
- [3. Python osnove](#3-python-osnove)
  - [3.1 VS Code okruženje](#31-vs-code-okruženje)
  - [3.2 Osnove Python sintakse](#32-osnove-python-sintakse)
    - [3.2.1 Varijable](#321-varijable)
    - [3.2.2 Logički izrazi](#322-logički-izrazi)
        - [Aritmetički operatori (Arithmetic operators)](#aritmetički-operatori-arithmetic-operators)
        - [Operatori pridruživanja (Assignment operators)](#operatori-pridruživanja-assignment-operators)
        - [Operatori usporedbe (Comparison operators)](#operatori-usporedbe-comparison-operators)
        - [Logički operatori (Logical operators)](#logički-operatori-logical-operators)
        - [Operatori identiteta (Identity operators)](#operatori-identiteta-identity-operators)
        - [Operatori pripadnosti (Membership operators)](#operatori-pripadnosti-membership-operators)
    - [3.2.3 Upravljanje tokom izvođenja programa](#323-upravljanje-tokom-izvođenja-programa)
      - [Selekcije](#selekcije)

<br>

# 1. Uvod

Razvoj raspodijeljenih sustava postao je ključan za ostvarivanje **visoke dostupnosti**, **skalabilnosti** i **performansi** aplikacija u današnjem digitalnom svijetu. Raspodijeljeni sustavi omogućuju stvaranje složenih sustava sposobnih za obrade koje nadilaze mogućnosti pojedinačnih računala. Ovi sustavi pružaju brojne prednosti, uključujući učinkovitiju obradu podataka, bolju prilagodbu velikim opterećenjima (_eng. High server load_) te veću otpornost na kvarove (_eng. Fault tolerance_).

**Razvoj raspodijeljenih sustava prvenstveno** temelji se prvenstveno na **distribuiranoj arhitekturi (_eng. Distributed architecture_)** te razvoju manjih aplikacija koje često nazivamo i **mikroservisima (_eng. Microservices_)**, imajući na umu da je svaki mikroservis zasebna i nezavisna aplikacija koja se izvršava u vlastitom procesu i komunicira s drugim mikroservisima putem mreže.

S obzirom na to da većina studenata koji upisuju ovaj kolegij već ima temeljna znanja stečena na kolegijima **Programsko inženjerstvo** i **Web aplikacije**, ovaj kolegij će se usredotočiti na proširivanje njihovih postojećih znanja i vještina te njihovu primjenu u kontekstu razvoja raspodijeljenih sustava. Primjerice, na vježbama će se kao glavni protokol za komunikaciju koristiti i dalje **HTTP/HTTPS** te **NoSQL** baza podataka, a ponovit će se i izrada jednostavnog sučelja kroz **Vue.js**.

Iako postoje mnogi jezici koji su svojim performansama i mogućnostima pogodni za razvoj raspodijeljenih sustava, poput jezika **Go (Golang)** koji se popularno koristi za razvoj mikroservisa zbog svoje servise i ugrađene podrške za konkurentnost, ili pak **Jave** koja ima snažnu podršku za višedretvenost (_eng. Multithreading_), mi smo izabrali **Python** kao jezik za ovaj kolegij.

**Python** nam omogućuje jednostavnu integraciju s postojećim bibliotekama i alatima koji već nude implementirane funkcionalnosti specifične za distribuirane sustave. Ovaj pristup omogućuje brže razvijanje aplikacija i fokusiranje na višu razinu apstrakcije, bez potrebe za implementacijom niskorazinskih komponenti. Python je jezik koji bi svaki developer trebao znati završetkom studija, a njegova popularnost i sveprisutnost kako u industriji tako i u znanosti čine ga neizostavnim alatom za rješavanje kompleksnih problema i razvoj kvalitetnih aplikacija.

# 2. Priprema Python okruženja

## 2.1 Instalacija Pythona

Python možete preuzeti i instalirati na više načina, a najjednostavniji način je za većinu korisnika preuzimanje i pokretanje instalacijskog programa sa [službene stranice Pythona](https://www.python.org/downloads/). Preporuka je odabrati veriziju **Python 3.9** ili noviju.

Kada pokrenete installer, ključno je odabrati opciju **Add Python to PATH** kako bi Python bio dostupan iz naredbenog retka (_eng. Command Prompt_). Nakon što završite instalaciju, možete provjeriti je li Python uspješno instaliran pokretanjem naredbe `python --version` u naredbenom retku. Ako je Python uspješno instaliran, trebali biste vidjeti verziju Pythona koju ste instalirali.

> **PATH** je environment varijabla na operacijskim sustavima poput Unix, Linux i Windows koja sadrži listu direktorija u kojima se nalaze skripte i izvršne datoteke koje možete pokrenuti iz naredbenog retka.

Jednom kada ste uspješno instalirali Python, možete provjeriti instaliranu verziju sljedećom naredbom u terminalu:

```bash
python --version
```

Ako dobijete grešku `"Python is not recognized as an internal or external command"` to znači da Python nije dodan u PATH. U tom slučaju, najčešće rješenje je ponovo pokrenuti Python installer i odabrati opciju **Add Python to PATH**.

Ako imate problema postavljanjem Pythona u PATH, kratki vodič [ovdje](https://realpython.com/add-python-to-path/).

Ako koristite Windows OS, možete provjeriti `PATH` varijablu pokretanjem naredbe `$Env:Path` u **Powershell terminalu**. Na Windowsu je svakako preporuka koristiti **Powershell terminal** umjesto Command Prompt terminala budući da je izlaskom Windowsa 10 Powershell postao glavni terminal za Windows.

```powershell
$Env:Path
```

Možete provjeriti i putem grafičkog sučelja, otvorite Start i ukucajte `environment` te odaberite **Edit the system environment variables**. U prozoru koji se otvori, kliknite na **Environment Variables** i u listi System variables pronađite **Path**. Kliknite na **Edit** i provjerite je li putanja do Pythona dodana.

![How to Set the Path and Environment Variables in Windows](./screenshots/windows_check_env.png)

---

Ako koristite **Linux** ili **MacOS**, Python je najvjerojatnije već instaliran na vašem sustavu. Možete provjeriti verziju Pythona pokretanjem naredbe:

```bash
python3 --version
```

Ako je Python instaliran, dobit ćete verziju Pythona koju koristite. Ako Python nije instaliran, možete ga instalirati putem **apt** ili **brew** package managera, ali i preuzimanjem instalacijskog paketa s [Pythonove službene stranice](https://www.python.org/downloads/).

> **Napomena**: Na Linuxu i MacOS-u, Python 3 se pokreće s naredbom `python3` kako bi se izbjegla konfuzija s Python 2 koji je još uvijek prisutan na nekim starijim sustavima.

Kako biste provjerili koji je Python interpreter postavljen kao zadani, možete pokrenuti naredbu:

```bash
which python3
```

Ova naredba će vam reći putanju do Python interpretera koji se koristi kada pokrenete `python3` naredbu. Ako želite, možete dodati alias za vaš Python terminal tako da možete pokrenuti Python interpreter jednostavno pokretanjem naredbe `python` umjesto `python3`.

Za `bash` korisnike, možete otvoriti `~/.bashrc` datoteku kroz `nano` editor:

```bash
nano ~/.bash_profile
```

i dodati sljedeću liniju na dno datoteke:

```bash
alias python=python3
```

Za `zsh` korisnike, možete otvoriti `~/.zshrc` datoteku kroz `nano` editor:

```bash
nano ~/.zshrc
```

i dodati sljedeću liniju na dno datoteke:

```bash
alias python=python3
```

Spremite izmjene naredbom `Ctrl + O`, pritisnite `Enter` i izađite iz editora naredbom `Ctrl + X`. Zatim pokrenite sljedeću naredbu kako bi se promjene primijenile:

```bash
source ~/.bashrc
```

odnosno za `zsh` korisnike:

```bash
source ~/.zshrc
```

Pokrenite novu sesiju terminala. Sada možete pokrenuti Python interpreter jednostavno pokretanjem naredbe `python`. Također, možete provjeriti koji je Python interpreter postavljen kao zadani pokretanjem naredbe:

```bash
which python
```

Trebali biste dobiti: `python: aliased to python3`.

Kao i jednake rezultate za `python3` i `python`.

```bash
python --version # Python [instalirana_verzija]
python3 --version # Python [instalirana_verzija]
```

TLDR; Većina korisnika će koristiti `python3` za pokretanje Python interpretera na Linuxu i MacOS-u, dok će koristiti `python` na Windowsu. Međutim, ako hoćete, možete dodati alias `python` za `python3` kako bi se izbjegla konfuzija.

## 2.2 Priprema virtualnog okruženja

Virtualno okruženje (_eng. Virtual Environment_) je tehnologija koja omogućuje kreiranje izoliranog okruženja za naše Python projekte. Virtualno okruženje rješava mnogobrojne probleme koji se javljaju kada radimo na više projekata koji koriste različite verziej Pythona ili različite verzije paketa.

Postoji više alata za upravljanje virtualnim okruženjim, a najpoznatiji su `venv`, `virtualenv` i `conda`.

Slobodni ste koristiti bilo koji od navedenih alata, međutim mi ćemo u sklopu ovog kolegija koristiti `conda` alat.

### 2.2.1 Instalacija `conda` alata

`conda` je open-source paketni menadžer i okruženje za upravljanje paketima i njihovim ovisnostima. `conda` je dostupan za Windows, Linux i MacOS operacijske sustave.

`conda` je podskup `Anaconda` distribucije, koja dolazi s preinstaliranim paketima i alatima za znanstveno računanje i analizu podataka. Međutim, za potrebe ovog kolegija, dovoljno je instalirati `conda` paketni menadžer.

To možete učiniti kroz `Anaconda Navigator` aplikaciju ili preuzimanjem samo `conda` instalacijskog paketa sa [službene stranice](https://docs.conda.io/en/latest/miniconda.html). Jednostavno odaberite verziju koja odgovara vašem operacijskom sustavu i slijedite upute za instalaciju.

Nakon što ste uspješno instalirali `conda` alat, možete provjeriti je li `conda` uspješno instaliran pokretanjem naredbe:

```bash
conda --version
```

Nije loše instalirati i ukupnu Anaconda distribuciju, jer dolazi s mnogim korisnim alatima, uključujući i graifčko sučelje `Anaconda Navigator` koje olakšava upravljanje okruženjima i paketima.

Anaconda distribuciju možete preuzeti s [službene stranice](https://www.anaconda.com/products/distribution). Naravno, `conda` je uključena u ovoj distribuciji pa možete provjeriti na isti način prepoznaje li ju naredbeni redak.

<img src="screenshots/anaconda.png" style="width:50%">

> Izgled Anaconda Navigator aplikacije i pregled izrađenih okruženja i paketa.

To je to! Spremni smo za rad s Pythonom! 🐍

---

# 3. Python osnove

**Python** je visokorazinski (eng. high-level) programski jezik opće namjene (eng. general-purpose) koji svojom jednostavnom sintaksom i čitljivošću koda naglašava čitljivost i brzinu razvoja projekata. Python je također dinamički tipiziran jezik (eng. dynamically typed language) što znači da se tipovi varijabli određuju za vrijeme izvođenja, a ne za vrijeme kompilacije.

Popularan je i široko korišten u mnogim područjima, uključujući: web razvoj, data science i analiza podataka, matematika, strojno učenje i umjetna inteligencija itd.

I ono što nam je još važno za zapamatiti, Python je tzv. multi-paradigmatski jezik, što znači da podržava više stilova programiranja, uključujući proceduralno, objektno orijentirano i funkcijsko programiranje. Korisnik može odabrati stil programiranja koji najbolje odgovara problemu koji rješava, dakle moguće je kombinirati različite stilove programiranja što čini ovaj jezik vrlo fleksibilnim.

## 3.1 VS Code okruženje

Za rad s Pythonom preporučujemo korištenje **Visual Studio Code** editora. VS Code je besplatan, open-source IDE (eng. Integrated development environment) kojeg razvija Microsoft, a nudi bogat ekosustav ekstenzija i alata koji olakšavaju razvoj aplikacija u Pythonu. Naravno, možete koristiti IDE po želji, međutim mi ćemo na vježbama iz ovog kolegija koristiti VS Code.

VS Code možete preuzeti s [službene stranice](https://code.visualstudio.com/Download) i instalirati na vaš operacijski sustav. Nakon instalacije, možete pokrenuti VS Code i instalirati ekstenziju koja će vam olakšati rad s Pythonom.

[**Python** ekstenzija](https://marketplace.visualstudio.com/items?itemName=ms-python.python): nudi generalnu podršku za Python razvoj, uključujući IntelliSens, debugger (Python Debugger), formatiranje, linting, itd.

- ova ekstenzija instalirat će vam još i `Python Debugger` i `Pylance` ekstenzije koje upotpunjuju rad s Pythonom u VS Code-u.

Provjerite jesu li sve ekstenzije uspješno instalirane i aktivirane. Možete ih pronaći u **Extensions** panelu na lijevoj strani VS Code sučelja.

## 3.2 Osnove Python sintakse

Za početak nećemo raditi s bibliotekama i alatima, već ćemo se upoznati s osnovama Python sintakse, stoga nam za sada neće niti trebati virtualno okruženje.

Krenimo s izradom osnovne Python skripte. Kreirajte novu datoteku s ekstenzijom `.py`. Na primjer, nazovite datoteku `hello.py`.

U donjem desnom kutu VS Code sučelja primjetit ćete trenutni Python interpreter koji se koristi. Provjerite je li to Python interpreter koji ste instalirali i koji želite koristiti. Ako nije, možete promijeniti interpreter klikom na trenutni interpreter i odabirom željenog.

<img src="screenshots/interpreter_vscode.png" style="width:50%">

> Odabran je Python interpreter (Python 3.13.0 /usr/local/bin/python3) koji će se koristiti za izvršavanje Python skripte.

U pythonu možemo ispisivati poruke u konzolu koristeći naredbu `print()`. Na primjer, možemo ispisati poruku "Hello, World!" koristeći sljedeći kod:

```python
print("Hello, World!")
```

Spremite datoteku i pokrenite je klikom na gumb **Run** u gornjem desnom kutu datoteke ili pritiskom na `Ctrl + Alt + N` odnosno `Cmd + Alt + N` na MacOS-u.
Trebali biste vidjeti ispis "Hello, World!" u terminalu.

Drugi način je pokretanje skripte iz terminala. Otvorite terminal u VS Code-u klikom na **Terminal** > **New Terminal** i odaberite terminal po želji, preferabilno `bash` ili `zsh` terminal.

U terminalu se pozicionirajte u direktorij gdje se nalazi vaša Python skripta i pokrenite je naredbom:

```bash
python hello.py
```

Ili naredbom `python3` ako koristite Linux ili MacOS i niste dodali alias za `python`:

```bash
python3 hello.py
```

**Kratki podsjetnik za navigaciju u terminalu (Windows, Linux, macOS)**

- `cd [ime direktorija]` - promjena direktorija
- `cd ..` - povratak u prethodni direktorij
- `ls` - ispis sadržaja direktorija
- `pwd` - ispis trenutne putanje
- `cls` ili `clear` - brisanje sadržaja terminala

### 3.2.1 Varijable

Varijable u Pythonu se deklariraju na sljedeći način:

```python
a = 5

b = "Hello, World!"

c = 3.14
```

Dakle, primjetite da se ne navodi tip varijable prilikom deklaracije, već se Python sam brine o tipu varijable. Varijabla `a` je tipa `int`, varijabla `b` je tipa `str`, a varijabla `c` je tipa `float`.

Varijable u Pythonu su **dinamički tipizirane**, što znači da se tip varijable određuje za vrijeme izvođenja, a ne za vrijeme kompilacije.

Moguće je pregaziti vrijednost varijable:

```python
a = 5

a = 10

print(a) # 10
```

Varijablu možemo ispisati koristeći naredbu `print()`:

```python
a = 5
b = 10

print(a + b) # 15
```

```python
a = "Hello, "

b = "World!"

print(a + b) # Hello, World!
```

Osim što se mogu pregaziti vrijednostima, varijable se mogu i zamijeniti pregaziti tipom varijable:

```python
a = 5

a = "Hello, World!" # može i s jednostrukim navodnicima

print(a) # Hello, World!
```

Varijable u Pythonu mogu sadržavati slova, brojeve i znak `_`, ali ne smiju započinjati brojem.

```python

# Ovo je ispravno

my_variable = 5
myVariable = 10
myVariable2 = 15

# Ovo nije ispravno (SyntaxError)

2myVariable = 5 # ne može započinjati brojem
my-Variable = 10 # ne može sadržavati znak -
my Variable = 15 # ne može sadržavati razmak
```

Varijable u Pythonu su **case-sensitive**, što znači da se razlikuju velika i mala slova.

```python
my_variable = 5
My_Variable = 10
MY_VARIABLE = 15

print(my_variable) # 5
print(My_Variable) # 10
print(MY_VARIABLE) # 15
```

Jednolinijske komentare u Pythonu možemo pisati koristeći znak `#`:

```python
# Ovo je komentar

a = 5 # Ovo je komentar
```

Dok višelinijske komentare možemo pisati koristeći znakove `"""` ili `'''`:

```python
"""
Ovo
je
višelinijski
komentar
"""

# Ili

'''
Ovo
je
isto višelinijski
komentar
'''
```

Međutim, **moguće je** specificirati tip varijable koristeći tzv. [_Casting_](https://www.geeksforgeeks.org/type-casting-in-python/):

```python
a = 5
# ili
a = int(5)
```

Rezultat će biti isti, no ovime se naglašava tip varijable.

```python
x = str(3)
y = int(3)
z = float(3)
```

Što će biti pohranjeno u varijable `x`, `y` i `z`?

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  x = "3"
  y = 3
  z = 3.0
</details>

<hr>

Ako se želimo uvjeriti, možemo uvijek provjeriti tip varijable koristeći funkciju `type()`:

```python
x = str(3)
y = int(3)
z = float(3)

print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'float'>
```

Prilikom imenovanja varijabli s više riječi, može se koristiti tehnika po izboru, međutim u Pythonu je uobičajeno koristiti **Camel Case** ili **Snake Case** notaciju.

**Camel Case**

```python
myVariable = 5
```

**Pascal Case**

```python
MyVariable = 5
```

**Snake Case**

```python
my_variable = 5
```

Python dozvoljava i tzv. **Multiple Assignment**, odnosno dodjeljivanje više vrijednosti više varijablama u jednoj liniji koda:

Primjerice imamo varijable `a`, `b` i `c` i hoćemo im dodijeliti vrijednosti `5`, `10` i `15`:

```python
a, b, c = 5, 10, 15

print(a) # 5
print(b) # 10
print(c) # 15
```

Može se koristiti i s drugim tipovima varijabli:

```python
a, b, c = "Hello", 5, 3.14

print(a) # Hello
print(b) # 5
print(c) # 3.14
```

> **Napomena**: Broj varijabli mora odgovarati broju vrijednosti koje se dodjeljuju, inače će Python baciti grešku.

Moguće je i dodjeljivanje iste vrijednosti više varijablama:

```python
a = b = c = "same value"

print(a) # same value
print(b) # same value
print(c) # same value
```

Moguće je i ispisati vrijednosti varijabli u jednom redu koristeći `print()` funkciju:

```python
a = 5
b = 10
c = 15

print(a, b, c) # 5 10 15
```

Pa i izvršiti konkatenaciju varijabli:

```python
a = "Moje "
b = "ime "
c = "je "
d = "Pero"

print(a + b + c + d) # Moje ime je Pero
```

Primjetite da smo nakon svake varijable dodali razmak kako bi rezultat bio čitljiv. Nećemo to raditi, već ćemo navoditi varijable odvojene zarezom:

```python
a = "Moje"
b = "ime"
c = "je"
d = "Pero"

print(a, b, c, d) # Moje ime je Pero
```

Na ovaj način Python će automatski dodati razmak (`" "`) između varijabli. Ako želimo promijeniti separator, možemo to učiniti koristeći `sep` argument:

```python
a = "Moje"
b = "ime"
c = "je"
d = "Pero"

print(a, b, c, d, sep="-") # Moje-ime-je-Pero
```

`print` naredba vrlo je korisna i često se koristi za ispisivanje poruka u konzolu, ali njena upotreba je prvenstveno u svrhu debugiranja i testiranja. Međutim, u stvarnim projektima, koristit ćemo `logging` biblioteku koja pruža naprednije mogućnosti za upravljanje logovima.

### 3.2.2 Logički izrazi

Pri oblikovanju računskih postupaka često je potrebno usmjeriti tok izvođenja programa ovisno o nekom **uvjetu**. Uvjet može biti ispunjen ili ne, a ta dva ishoda se obično postovjećuju s vrijednostima istinotisti iz matematičke logike odnosno logike sudova:

- istinito (eng. true)
- neistinito (eng. false)

Python za prikaz vrijednosti istinitosti definira poseban ugrađeni tip podatka `bool`, čije su moguće vrijednosti `True` (istinito) i `False` (neistinito). Obratite pažnju na **velika početna slova** ovih ključnih riječi Pythona!

Logički izrazi se koriste za **usporedbu vrijednosti** i **provjeru određenog uvjeta**. Svaki logički izraz vraća vrijednost tipa `bool`.

Izraze možemo graditi koristeći operatore. U pythonu postoji 7 skupina operatora:

1. **Aritmetički operatori** (eng. Arithmetic operators)
2. **Operatori pridruživanja** (eng. Assignment operators)
3. **Operatori usporedbe** (eng. Comparison operators)
4. **Logički operatori** (eng. Logical operators)
5. **Operatori identiteta** (eng. Identity operators)
6. **Operatori pripadnosti** (eng. Membership operators)
7. **Operatori bitovnih operacija** (eng. Bitwise operators)

##### Aritmetički operatori (Arithmetic operators)

Aritmetički operatori se koriste za izvođenje matematičkih operacija na brojevima. U Pythonu postoje sljedeći aritmetički operatori:

| Operator | Opis                            | Primjer  | Rezultat |
| -------- | ------------------------------- | -------- | -------- |
| `+`      | Zbrajanje                       | `5 + 3`  | `8`      |
| `-`      | Oduzimanje                      | `5 - 3`  | `2`      |
| `*`      | Množenje                        | `5 * 3`  | `15`     |
| `/`      | Dijeljenje (float)              | `5 / 2`  | `2.5`    |
| `//`     | Cjelobrojno dijeljenje          | `5 // 2` | `2`      |
| `%`      | Ostatak pri dijeljenju (modulo) | `5 % 2`  | `1`      |
| `**`     | Potenciranje                    | `5 ** 3` | `125`    |

Pogledajmo nekoliko primjera aritmetičkih operacija:

```python
a = 5
b = 3

print(a + b) # 8
print(a - b) # 2
print(a * b) # 15
print(a / b) # 1.6666666666666667 (float)
print(a // b) # 1 (int)
print(a % b) # 2
print(a ** b) # 125
```

U Pythonu se realni brojevi prikazuju ugrađenim tipom `float`, dok se cijeli brojevi prikazuju tipom `int`. Kao što je i uobičajeno, možemo ih stvarati konverzijom objekata drugih tipova primjenom konstruktora `float`:

Što će biti ispisano u sljedećem primjeru?

```python
float(31), float(1 < 2) # konverzija brojeva
```

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  (31.0, 1.0)
</details>

Pored toga, realni brojevi mogu nastati i kao rezultat dijeljenja cijelih brojeva:

```python
print(1/11) # 0.09090909090909091
```

Za vrlo velike ili vrlo male brojeve često je praktičnije koristiti tzv. znanstveni zapis (eng. scientific notation) kod kojega se red veličine broja izražava prikladnom potencijom broja 10. Pritom se eksponent označava malim ili velikim slovom `E`, a može biti i negativan. Na primjer:

```python
print(1.23e-4) # 0.000123
print(1.23e4) # 12300.0
```

Ako literal premaši najveću vrijednost koju može prikazati, Python će ga zapisati kao specijalnu vrijednost `inf` koja odgovra neizmjerno velikom broju (eng. infinity):

```python
print(1e309) # inf
```

Prilikom dijeljenja s nulom, Python će baciti grešku `ZeroDivisionError`:

```python
print(1/0) # ZeroDivisionError: division by zero
```

Što se tiče ugrađenih funkcija nad realnim brojevima, ima ih mnogo i možete ih pronaći vrlo lako na Internetu, za sada možemo spomenuti nekoliko njih koje se često koriste:

```python
print(abs(-5)) # 5 (apsolutna vrijednost)
print(round(3.14159, 2)) # 3.14 (zaokruživanje na n decimala)
print(max(1, 2, 3, 4, 5)) # 5 (maksimalna vrijednost)
print(min(1, 2, 3, 4, 5)) # 1 (minimalna vrijednost)
```

Iz `math` biblioteke možemo koristiti veliki broj funkcija koje primaju realne brojeve. Uključene su važnije matematičke funkcije, korisne konverzije, uobičajene trigonometrijske i hiperbolne funkcije, te neke specijalne funkcije i konstante:

```python
import math

print(math.sqrt(16)) # 4.0 (kvadratni korijen)
print(math.pow(2, 3)) # 8.0 (potenciranje))

print(math.exp(1)) # 2.718281828459045 (e^x)
print(math.log(10)) # 2.302585092994046 (ln(x))

print(math.trunc(3.14)) # 3 (odbacuje decimalni dio)
print(math.ceil(3.14)) # 4 (zaokružuje prema gore)
print(math.floor(3.14)) # 3 (zaokružuje prema dolje)
```

Nekoliko praktičnih funkcija za testiranje konačnosti realnih brojeva koje su dostupne u `math` biblioteci:

```python
import math

print(math.isfinite(1.0)) # True (je li broj konačan)
print(math.isinf(1.0)) # False (je li broj beskonačan tj. neizmjerno velik)

print(math.isnan(1.0)) # False (je li broj NaN, tj. Not a Number)
```

##### Operatori pridruživanja (Assignment operators)

Operatori pridruživanja se koriste za dodjeljivanje vrijednosti varijablama. U Pythonu postoje sljedeći operatori pridruživanja:

| Operator | Opis                            | Primjer   | Ekvivalent   |
| -------- | ------------------------------- | --------- | ------------ |
| `=`      | Pridruživanje                   | `x = 5`   | `x = 5`      |
| `+=`     | Dodaj i pridruži                | `x += 3`  | `x = x + 3`  |
| `-=`     | Oduzmi i pridruži               | `x -= 3`  | `x = x - 3`  |
| `*=`     | Pomnoži i pridruži              | `x *= 3`  | `x = x * 3`  |
| `/=`     | Podijeli i pridruži             | `x /= 3`  | `x = x / 3`  |
| `//=`    | Cjelobrojno podijeli i pridruži | `x //= 3` | `x = x // 3` |
| `%=`     | Modulo i pridruži               | `x %= 3`  | `x = x % 3`  |
| `**=`    | Potenciraj i pridruži           | `x **= 3` | `x = x ** 3` |

##### Operatori usporedbe (Comparison operators)

Operatori usporedbe se koriste za usporedbu dvije vrijednosti. U Pythonu postoje sljedeći operatori usporedbe:

| Operator | Opis                 | Primjer  | Rezultat |
| -------- | -------------------- | -------- | -------- |
| `==`     | Jednako              | `5 == 3` | `False`  |
| `!=`     | Nije jednako         | `5 != 3` | `True`   |
| `>`      | Veće od              | `5 > 3`  | `True`   |
| `<`      | Manje od             | `5 < 3`  | `False`  |
| `>=`     | Veće ili jednako od  | `5 >= 3` | `True`   |
| `<=`     | Manje ili jednako od | `5 <= 3` | `False`  |

Pogledajmo nekoliko usporedba cjelobrojnih podataka:

```python
a = 5
b = 10

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True
```

**Napomena**: Treba biti oprezan prilikom uspoređivanja realnih brojeva zbog ograničenja u točnosti prikaza brojeva s pomičnim zarezom, odnosno zbog nepreciznosti njihova prikaza. Posebno se to odnosi na cjelobrojne razlomke i decimalne konstante jer nam njihov sažeti izvorni zapis može sugerirati jednaku sažetost njihovog internog prikaza u memoriji računala. Nikad ne smijemo smetnuti s uma da to gotovo nikada nije slučaj jer većina racionalnih brojeva u koje uvrštavamo i decimalne konstante nemjau konačan prikaz u binarnom brojevnom sustavu. Stoga, uvijek treba koristiti odgovarajuće funkcije za usporedbu realnih brojeva koje uzimaju u obzir određenu toleranciju.

Razmotrimo prvo dva razlomka čija bi razlika trebala biti točno 1, ali u praksi se to ne događa:

```python
print(5/3 == 1+2/3) # False
```

Jednako tako moramo biti oprezni i s decimalnim brojevima:

```python
print(0.1 + 0.2 == 0.3) # False
# ili
print(0.1 * 3 == 0.3) # False
```

U ovakvim slučajevima koristimo funkcije za usporedbu realnih brojeva koje uzimaju u obzir određenu toleranciju:

```python
import fractions

print(fractions.Fraction(5, 3) == 1 + fractions.Fraction(2, 3)) # True

import decimal

print(decimal.Decimal('0.1') * 3) == decimal.Decimal('0.3') # True
```

Operatore usporedbe moguće je primjenjivati i na većinu ostalih ugrađenih tipova podataka u Pythonu, kao i na korisničke tipove koji podržavaju odgovarajuće operatore, pri čemu će smisao usporedbi ovisiti od tipa do tipa.

Ono što je zanimljivo u Pythonu, i pomalo nekonvencionalno u odnosu na druge jezike, jest da se operatori usporedbe mogu ulančavati, kao matematički izrazi:

```python
a = 5
b = 10
c = 15

print(a < b < c) # True (5 < 10 < 15)
```

Moguće je graditi "lance" proizvoljne duljine, npr.

```python
print(0 < 3 < 5 < 100) # True
```

To naravno mogu biti bilo kakvi izrazi, ne samo "veće" i "manje" usporedbe:

```python
print(4 == 2*2 == 2**2) # True
```

Slično kao i u drugim jezicima, u Pythonu se određeni "non-boolean" izrazi tumače kao `True` ili `False` odnosno tzv. "truthy" i "falsy" vrijednosti. Na isti način kao što koristimo _Casting_ za promjenu ili definiranje tipa varijable (npr. `int()`, `str()`, `float()`), možemo koristiti i `bool()` konstruktor za pretvaranje vrijednosti u `bool` tip.

Vrijede uobičajena pravila:

```python
print(bool(0)) # False (0 se tumači kao False)
print(bool(1)) # True (svi brojevi osim 0 se tumače kao True)
print(bool(-1)) # True (pa i negativni brojevi)

print(bool("")) # False (prazan string se tumači kao False)
print(bool("cvrčak")) # True (svi stringovi osim praznog se tumače kao True)
print(bool(" ")) # True (čak i prazan string s razmakom se tumači kao True)
```

##### Logički operatori (Logical operators)

Logički operatori se koriste za kombiniranje logičkih izraza. Nad objektima logičkog tipa `bool` moguće je primjenjivati uobičajene operatore `and`, `or` i `not`.

| Operator | Opis                                                                  | Primjer          | Rezultat |
| -------- | --------------------------------------------------------------------- | ---------------- | -------- |
| `and`    | Konjukcija ili logičko "I" - `True` ako su oba izraza `True`          | `True and False` | `False`  |
| `or`     | Disjunkcija ili logičko "ILI - `True` ako je barem jedan izraz `True` | `True or False`  | `True`   |
| `not`    | Negacija ili logičko "NE"                                             | `not True`       | `False`  |

Izračunavanje logičkih operatora prestaje **čim konačna vrijednost izraza postane jasna**. Uzmimo za primjer izraze:

```python
False and x

True or x
```

Je li nam bitna vrijednost `x` u ovim izrazima?

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  Ne, jer u prvom slučaju, ako je jedan od izraza `False`, cijeli izraz je `False`, a u drugom slučaju, ako je jedan od izraza `True`, cijeli izraz je `True`.
</details>

---

Sad kad smo uveli logičke, usporedne i aritmetičke operatore, možemo reći da se ulančani operatori usporedbe interpretiraju kao **konjukcija pojedinačnih binarnih usporedbi**. Primjerice, izraz `1 < x < 6` se interpretira poput: `1 < x and x < 6`. Pritom ssvaki od ugniježđenih operanada ovakvih izraza **izračunava samo jednom** , a vrijednost cijelog izraza postaje `False` čim neka od usporedbi ne bude zadovoljena - **naknadne usporedbe se u tom slučaju više neće provoditi**.

Primjer:

```python
1 < 2+3 < 6 # koliko će se usporedbi izvršiti?
```

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  
  <p>Izraz se interpretira kao `1 < 2+3 and 2+3 <p 6`, dakle izvršit će se dvije usporedbe.</p>
  <p>Međutim, zbrajanje će se izvršiti samo jednom, budući da Python izračunava izraz (2+3) samo jednom, a onda primjenjuje dobivenu vrijednost na obe usporedbe.</p>
</details>

```python
1 < 4 < 3 < 6 # koliko će se usporedbi izvršiti?
```

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  
  <p>Izraz se interpretira kao `1 < 4 and 4 < 3 and 3 < 6`.</p>
  <p>Prva usporedba je zadovoljena, ali druga nije, pa se izračunavanje prekida i cijeli izraz se tumači kao `False`.</p>
  <p>Drugim riječima, treća usporedba se neće uopće izvesti.</p>
</details>

<hr>

Logičke operatore možemo primijeniti i na podatke ostalih tipova. Operator `not` jednostavno vraća negiranu logičku vrijednost svog argumenta.

- Operator `and` vraća lijevi argument ako je njegova logička vrijednost `False`, inače vraća desni argument.
- Operator `or` vraća lijevi argument ako je njegova logička vrijednost `True`, a u protivnom vraća desni argument.

```python
print(not True) # False

print(5 and 3) # 3 - jer je 5 True, a 3 je zadnji argument

print(0 and 3) # 0 - jer je 0 False, a 3 se neće ni provjeravati

print(5 or 3) # 5 - jer je 5 True, a 3 se neće ni provjeravati

print(0 or 3) # 3 - jer je 0 False, a 3 je zadnji argument
```

OK, što će vratiti izraz `5 and 'cvrčak`?

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  'cvrčak' - jer je 5 True, a 'cvrčak' je zadnji argument
</details>

A što će vratiti izraz `'' and 42`?

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  '' - jer je '' False, a 42 se neće ni provjeravati
</details>

Iako je `bool` zasebni podatkovni tip, on je ujedno i podtip cijelih brojeva. Stoga se vrijednosti `True` i `False` mogu pojaviti i u aritmetičkom kontekstu, pri čemu se ponašaju kao brojevi 1, odnosno 0, kao što ilustriraju sljedeći primjeri:

```python
print(True + True) # 2

print(False + False) # 0

print (True + 1) # 2

print (False * 3) # 0
```

##### Operatori identiteta (Identity operators)

Postoje dva operatora identiteta: `is` i `is not`. Ovi operatori koriste se za usporedbu objekata, ne njihovih vrijednosti. Što to znači?

Objekti su pohranjeni u memoriji računala, a varijable su referenca na te objekte. Operator `is` vraća `True` ako su objekti jednaki odnosno ako se objekti nalaze na istoj memorijskoj lokaciji, odnosno `False` ako se objekti nalaze na različitim memorijskim lokacijama.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # False (memorijske lokacije su različite i liste su promjenjive)

print (a == b) # True (vrijednosti su jednake)
```

Što se događa u sljedećem primjeru?

```python
a = [1, 2, 3]
b = a

print(a is b) # ?
print(a == b) # ?
```

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  <p>a is b # True</p>
  <p>a == b # True</p>
</details>

A ovdje, što će biti?

```python
a = 10
b = 10

print(a is b) # ?
print(a == b) # ?
```

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  <p>a is b # True</p>
  <p>a == b # True</p>
  
  Simple answer: Brojevi su pohranjeni na istoj memorijskoj lokaciji i nisu promijenjivi (eng. immutable)
</details>

Operator `is not` vraća `True` ako objekti nisu jednaki, odnosno ako se objekti ne nalaze na istoj memorijskoj lokaciji.

```python
a = 10
b = 20
print(a is not b) # True

str1 = "hello"
str2 = "hello"

print(str1 is not str2) # Nisu na istoj memorijskoj lokaciji, ali Python optimizira na jednak način kao i manje brojeve, dakle False
```

##### Operatori pripadnosti (Membership operators)

Sve kolekcije Pythona mogu ustanoviti pripadnost zadanog elementa operatorima `in` i `not in`. Ovi operatori koriste se za provjeru pripadnosti elementa kolekciji. Neki ih svrstavaju u logičke operatore ili operatore usporedbe jer kao rezultat daju logičku vrijednost. Operator `in` vraća `True` ako se određeni element nalazi u kolekciji, a `False` ako se ne nalazi. Operator `not in` radi obrnuto.

Ovi operatori često se koriste u Pythonu.

```python
a = [1, 2, 3, 4, 5]

print(1 in a) # True
print(6 in a) # False
print(1 not in a) # False
print(6 not in a) # True
```

```python
iks = 'x'
print (iks in 'cvrčak') # True

samoglasnici = 'aeiou'

print('a' in samoglasnici) # True
print('b' in samoglasnici) # False
```

```python
stabla = ['hrast', 'bukva', 'javor', 'bor']

print('bukva' in stabla) # True

print('jela' not in stabla) # True
```

### 3.2.3 Upravljanje tokom izvođenja programa

Kontrola toka (_eng. flow control_) odnosi se na programske konstrukte koji omogućuju izvršavanje određenih dijelova koda ovisno o zadanim uvjetima. U Pythonu se, kao i u većini programskih jezika, kontrola toka postiže prvenstveno korištenjem selekcija (_eng. selection_) i iteracija (_eng. iteration_).

#### Selekcije

Selekcija se definira korištenjem `if`, `elif` i `else` naredbi.

Logička pravila su ista kao i u većini programskih jezika, međutim treba obratiti pažnju na specifičnosti Python sintakse kao što su indentacija koda.

Indentacija koda je **obavezna** u Pythonu i koristi se za označavanje blokova koda. Blok koda se označava uvlačenjem koda za **4 prazna mjesta** (ili 2 ovisno o postavkama) ili **jedan tabulator**. Python ne koristi vitičaste zagrade `{}` kao što je to slučaj u većini programskih jezika (C familija jezika, Java, JavaScript itd.), već koristi indentaciju koda za označavanje blokova koda.

Na primjer, možemo provjeriti je li broj paran ili neparan:

```python
a = 5

if a % 2 == 0:
  print("Broj je paran")
else:
  print("Broj je neparan")
```

Primjetite da je blok koda nakon `if` i `else` naredbi uvučen za 4 prazna mjesta. Ovo je obavezno i Python će baciti grešku ako se ne pridržavate ovog pravila.
Indentaciju želimo raditi koristeći **tabulator** - `Tab`.

Primjetite još dvije stvari u ovom primjeru:

- **nemamo zagrade oko uvjeta/logičkog izrada**, dakle ne pišemo `if (a % 2 == 0)`, već samo `if a % 2 == 0`
- **oznakom `:` označavamo kraj uvjeta/logičkog izrada** i početak bloka koda koji će se izvršiti ako je uvjet ispunjen

Ekvivalentan kod u C++ bi izgledao ovako:

```cpp
int a = 5;

if (a % 2 == 0) {
  cout << "Broj je paran" << endl;
} else {
  cout << "Broj je neparan" << endl;
}
```

ili u JavaScriptu:

```javascript
let a = 5;

if (a % 2 == 0) {
  console.log("Broj je paran");
} else {
  console.log("Broj je neparan");
}
```

Ukoliko imamo više od dva uvjeta, koristimo `elif` naredbu:

```python
a = 5

if a % 2 == 0:
  print("Broj je paran")
elif a % 2 == 1:
  print("Broj je neparan")
else:
  print("Broj nije ni paran ni neparan")
```

Od korisnika možemo zatražiti unos koristeći `input()` funkciju:

```python
a = input("Unesite broj: ")

if a % 2 == 0:
  print("Broj je paran")
elif a % 2 == 1:
  print("Broj je neparan")
else:
  print("Broj nije ni paran ni neparan")
```

Što se dešava ako korisnik unese "1"?

<details>
  <summary>Spoiler alert! Odgovor na pitanje</summary>
  Greška! Neče se izvršiti else blok budući da je a tipa string, dakle program javlja grešku prilikom prvog izraza a % 2 == 0
</details>
