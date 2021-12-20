import urllib.request, json

header = {'content-type': 'application/json', 'Accept': 'text/html'}

def GetRegisteredCompanies(city, result_limit):
    url = f"https://avoindata.prh.fi/bis/v1?totalResults=true&maxResults={result_limit}&resultsFrom=0&registeredOffice={city}&companyForm=OY&companyRegistrationFrom=1978-03-14"
    request = urllib.request.Request(url, headers = header)

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read())
            totalResults = result["totalResults"] # Näyttää kätevästi kokonaismäärän, result_limit ei vaikuta tähän arvoon.
            print(f"{city} Kokonaismäärä: {totalResults}")

            endedCompanies = 0
            for loopedResult in result["results"]:
                if loopedResult.get("detailsUri"):
                    request2 = urllib.request.Request(loopedResult["detailsUri"], headers = header)
                    with urllib.request.urlopen(request2) as response2:
                        result2 = json.loads(response2.read())
                        for idx, r in enumerate(result2["results"]):
                            names = r["names"][idx].get("endDate")
                            if "None" not in str(names):
                                endedCompanies += 1

            print(f"Lopettanut: {endedCompanies}") # Näyttää result_limitin sisällä olevat, ei siis kokonaismäärää databasessa.
    except Exception as e:
        print(e) 

GetRegisteredCompanies(city="Ylitornio", result_limit=50)
GetRegisteredCompanies(city="Merikarvia", result_limit=50)
GetRegisteredCompanies(city="Parikkala", result_limit=50)
