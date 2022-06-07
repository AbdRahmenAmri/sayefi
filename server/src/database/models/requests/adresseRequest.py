class AdresseRequest():
    def __init__(self) -> None:
        pass

    def __init__(self, request) -> None:
        self.region = request['adrRegion']
        self.adresse = request['adrAdresse']
        self.city = request['adrCity']

    def setRegion(self, region) -> None:
        self.region = region
    def setAdresse(self, adresse) -> None:
        self.adresse = adresse
    def setCity(self, city) -> None:
        self.city = city

    def getRegion(self) -> str:
        return self.region
    def getAdresse(self) -> str:
        return self.adresse
    def getCity(self) -> str:
        return self.city
