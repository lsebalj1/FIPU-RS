# Raspodijeljeni sustavi (RS)

**Nositelj**: doc. dr. sc. Nikola Tanković  
**Asistent**: Luka Blašković, mag. inf.

**Ustanova**: Sveučilište Jurja Dobrile u Puli, Fakultet informatike u Puli

<img src="https://raw.githubusercontent.com/lukablaskovic/FIPU-PJS/main/0.%20Template/FIPU_UNIPU.png" style="width:40%; box-shadow: none !important; "></img>

# (1) Ponavljanje Pythona

<img src="./RS_01.png" style="width:9%; border-radius: 8px; float:right;"></img>

<div style="float: clear; margin-right:5px;">Raspodijeljeni sustav je svaki računalni sustav koji se sastoji od više povezanih autonomnih računala koji zajedno rade kao jedinstveni kohezivni sustav za postizanje zajedničkog cilja. Drugim riječima, raspodijeljeni sustavi su skupina nezavisnih računala (čvorova u mreži) koji međusobno komuniciraju i koordiniraju svoje radnje kako bi izvršili određeni zadatak. Na ovom kolegiju studenti će se upoznati s osnovama raspodijeljenih sustava i njihovim karakteristikima, tehnologijama i alatima koji se koriste u njihovom razvoju te naučiti kako razvijati aplikacije s naglaskom na distribuiranu arhitekturu.</div>
<br>

**🆙 Posljednje ažurirano: 25.10.2024.**

## Sadržaj

- [Raspodijeljeni sustavi (RS)](#raspodijeljeni-sustavi-rs)
- [(1) Ponavljanje Pythona](#1-ponavljanje-pythona)
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
    - [3.2.2. Kontrola toka i selekcija](#322-kontrola-toka-i-selekcija)

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

Međutim, **moguće je** specificirati tip varijable koristeći tzv. _Casting_:

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

### 3.2.2. Kontrola toka i selekcija

Kontrola toka (_eng. flow control_) odnosi se na programske konstrukte koji omogućuju izvršavanje određenih dijelova koda ovisno o zadanim uvjetima. U Pythonu se, kao i u većini programskih jezika, kontrola toka postiže prvenstveno korištenjem selekcija (_eng. selection_) i iteracija (_eng. iteration_).

Selekcija se postiže korištenjem `if`, `elif` i `else` naredbi.

Logička pravila su ista kao i u većini programskih jezika, međutim treba obratiti pažnju na specifičnosti Python sintakse kao što su indentacija koda.

Indentaciaj koda je **obavezna** u Pythonu i koristi se za označavanje blokova koda. Blok koda se označava uvlačenjem koda za **4 prazna mjesta** (ili 2 ovisno o postavkama) ili **jedan tabulator**. Python ne koristi vitičaste zagrade `{}` kao što je to slučaj u većini programskih jezika (C familija jezika, Java, JavaScript itd.), već koristi indentaciju koda za označavanje blokova koda.

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
- **oznakom `:` označavamo kraj uvjeta/logičkog izrada** i početak bloka koda

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
