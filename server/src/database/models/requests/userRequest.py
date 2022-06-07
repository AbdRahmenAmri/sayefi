class UserRequest():
    def __init__(self) -> None:
        pass

    def __init__(self,request,adresse) -> None:
        self.email = request['userEmail']
        self.password = request['userPassword']
        self.name = request['userName']
        self.phone_number = request['userPhoneNumber']
        self.sexe = request['userSexe']
        self.adresse = adresse
    
    def setEmail(self,email) -> None:
        self.email = email
    def setPassword(self,password) -> None:
        self.password = password
    def setName(self,name) -> None:
        self.name = name
    def setPhoneNumber(self,phone_number) -> None:
        self.phone_number = phone_number
    def setSexe(self,sexe) -> None:
        self.sexe = sexe
    def setAdresse(self,adresse) -> None:
        self.adresse = adresse
    
    def getEmail(self) -> str:
        return self.email
    def getPassword(self) -> str:
        return self.password
    def getName(self) -> str:
        return self.name
    def getPhoneNumber(self) -> str:
        return self.phone_number
    def getSexe(self) -> str:
        return self.sexe
    def getAdresse(self):
        return self.adresse
    