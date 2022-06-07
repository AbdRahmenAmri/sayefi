from database.interfaces.userInterfaces import UserInterface
class UserValidator(UserInterface):
    user = None


    def __init__(self,user) -> None:
        super().__init__()
        self.user = user
    
    def __init__(self) -> None:
        super().__init__()
    
    
    def isValid(self):
        return self.validEmail and self.validName and self.validPassword and self.validPhoneNumber and self.validSexe

    def validEmail(self, email) -> bool:
        return super().validEmail(email)
    def validName(self, name) -> bool:
        return super().validName(name)
    def validPassword(self, password) -> bool:
        return super().validPassword(password)
    def validPhoneNumber(self, phone_number) -> bool:
        return super().validPhoneNumber(phone_number)
    def validSexe(self, sexe) -> bool:
        return super().validSexe(sexe)

    def validEmail(self) -> bool:
        return super().validEmail(self.getUser().getEmail())
    def validName(self) -> bool:
        return super().validName(self.getUser().getName())
    def validPassword(self) -> bool:
        return super().validPassword(self.getUser().getPassword())
    def validPhoneNumber(self) -> bool:
        return super().validPhoneNumber(self.getUser().getPhoneNumber())
    def validSexe(self) -> bool:
        return super().validSexe(self.getUser().getSexe())

    def problemsFinder(self) -> list:
        problems = []
        if not self.validEmail():
            problems.append('email')
        if not self.validName():
            problems.append('name')
        if not self.validPhoneNumber():
            problems.append('phone')
        if not self.validPassword():
            problems.append('password')
        if not self.validSexe():
            problems.append('sexe')
        return problems
        
    
    def setUser(self,user) -> None:
        self.user = user

    def getUser(self):
        return self.user