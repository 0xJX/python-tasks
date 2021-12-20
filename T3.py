def GetDictionaryStr():
    retString = ""
    newDict = {}
    for i in range(1, 21):
        newDict[i] = i * i

    # Tämän olisi voinut tehdä edellisessä loopissa jo, mutta tehdään se erikseen että tulee dict käyttöön. :)
    for i in newDict:
        retString += f"{i}**2={newDict[i]}"
        if i is not len(newDict): # Lisää pilkku, jos 'i' ei ole listan viimeinen.
            retString += ", "
    return retString

print(GetDictionaryStr())
