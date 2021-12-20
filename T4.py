import urllib.request, json

def GetRegisteredCompanies(city):
    url = f"https://avoindata.prh.fi/bis_v1.fi.json/bis/v1?totalResults=false&maxResults=10&resultsFrom=0&registeredOffice={city}&companyForm=OY&companyRegistrationFrom=1978-03-14"
    request = urllib.request.Request(url, headers={'content-type': 'application/json', 'Accept': 'text/html'})

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read())
            print(result) # Printtaa koko vastauksen, ilman käsittelyä toistaiseksi kunnes saan validin vastauksen..
    except Exception as e:
        print(e) # Virhe, tässä tapauksessa yleisin 404 :(

GetRegisteredCompanies("Ylitornio")
GetRegisteredCompanies("Merikarvia")
GetRegisteredCompanies("Parikkala")

# Valitettavasti tätä en saanut toimimaan, 404 tuli joka kerta vastauksena vaikka kokeilin heidän omaa palvelinta, postman-ohjelmaa ja muita tapoja.
# URL https://avoindata.prh.fi/bis_v1.fi.json näyttää toimivan, mutta https://avoindata.prh.fi/bis_v1.fi.json/bis/v1? + args palauttaa aina 404.
# Olisin jatkanut resultin käsittelyä jos olisin saanut edes yhden vastauksen api:lta ja nähnyt mitä se puskisi ulos.
