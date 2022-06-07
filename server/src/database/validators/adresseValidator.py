from database.interfaces.adresseInterfaces import AdresseInterfaces

class AdresseValidator(AdresseInterfaces):
    adr = None
    def __init__(self, adr) -> None:
        self.adr = adr

    def __init__(self) -> None:
        pass

    def isValid(self):
        return self.validRegion() and self.validAdresse() and self.validCity()
    
    def validRegion(self) -> bool:
        return super().validRegion(self.getAdr().getRegion())
    def validCity(self) -> bool:
        return super().validCity(self.getAdr().getAdresse())
    def validAdresse(self) -> bool:
        return super().validAdresse(self.getAdr().getCity())

    def validRegion(self, region) -> bool:
        return super().validRegion(region)
    def validCity(self, city) -> bool:
        return super().validCity(city)
    def validAdresse(self,adresse) -> bool:
        return super().validAdresse(adresse)
    
    def problemsFinder(self) -> list:
        problems = []
        if not self.validRegion():
            problems.append('region')
        if not self.validAdresse():
            problems.append('adresse')
        if not self.validCity():
            problems.append('city')
        

    def setAdr(self, adr) -> None:
        self.adr = adr

    def getAdr(self) -> str:
        return self.adr