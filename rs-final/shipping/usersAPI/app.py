from aiohttp import web

korisnici = [
    {"id": 1, "ime": "Ana", "prezime": "Anić", "email": "aanic@gmail.com", "broj_telefona": "0911234453", "adresa" : {"grad": "Zagreb", "ulica": "Ilica 15", "postanski_broj": "10000"}},
    {"id": 2, "ime": "Marko", "prezime": "Markić", "email": "mmarkic@gmail.com", "broj_telefona": "0919876543", "adresa" : {"grad": "Split", "ulica": "Riva 3", "postanski_broj": "21000"}},
    {"id": 3, "ime": "Ivana", "prezime": "Ivić", "email": "iivic@gmail.com", "broj_telefona": "0921234567", "adresa" : {"grad": "Rijeka", "ulica": "Korzo 5", "postanski_broj": "51000"}},
    {"id": 4, "ime": "Petar", "prezime": "Perić", "email": "pperic@gmail.com", "broj_telefona": "0952345678", "adresa" : {"grad": "Osijek", "ulica": "Europska avenija 10", "postanski_broj": "31000"}},
    {"id": 5, "ime": "Maja", "prezime": "Majić", "email": "mmajic@gmail.com", "broj_telefona": "0973456789", "adresa" : {"grad": "Zadar", "ulica": "Kalelarga 20", "postanski_broj": "23000"}},
    {"id": 6, "ime": "Luka", "prezime": "Lukić", "email": "llukic@gmail.com", "broj_telefona": "0998765432", "adresa" : {"grad": "Dubrovnik", "ulica": "Stradun 8", "postanski_broj": "20000"}}
]

async def get_users(request):
    return web.json_response(korisnici)

async def get_user_by_email(request):
    email = request.match_info.get('email')
    if email is None:
        return web.json_response({"error": "Email nije proslijeđen"}, status=400)
    if "@" not in email or "." not in email:
        return web.json_response({"error": "Email nije ispravnog formata"}, status=400)
    user = next((k for k in korisnici if k['email'] == email), None)
    if user is None:
        return web.json_response({"error": "Korisnik nije pronađen"}, status=404)

    return web.json_response(user)

app = web.Application()
app.router.add_get('/korisnici', get_users)
app.router.add_get('/korisnici/{email}', get_user_by_email)

if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=8080)

# python3 app.py
