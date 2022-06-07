import validators

class UserInterface():
    allowedSymbol = ['.','-' ,'_' ,'$','*','(',')', '#','@', '!','%','/',' ']
    minlength = 8
    maxlength = 255
    allowedsexe = ['F','M']

    def validEmail(self,email) -> bool:
        return validators.email(email) and len(email) <= 255
    
    def validPassword(self,password) -> bool:
        if len(password)<self.minlength :
            return None
        for c in password:
            if(not c.isalnum() or c not in self.allowedSymbol):
                return False
        return True
    def validName(self,name) -> bool:
        name_tab = name.split(' ')
        for singel_name in name_tab:
            if not singel_name.isalpha():
                return False
        return True
    def validPhoneNumber(self,phone_number) -> bool:
        if not len(phone_number) != 8 and not phone_number.isnumeric():
            phone_number = int(phone_number)
            if phone_number[0:2] in range(40,47) or phone_number[0] in [2,9,5]:
                return True
        return False
    def validSexe(self,sexe) -> bool:
        if sexe is not None:
            return sexe.upper() in self.allowedsexe
        return sexe is None
    

