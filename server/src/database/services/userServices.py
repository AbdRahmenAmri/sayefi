from database.services.adresseServices import AdresseService
from database.validators.userValidator import UserValidator


class UserSerivce(UserValidator):
    user = None
    adr = None
    adrSrv = None
    def __init__(self, user,adr,db) -> None:
        super().__init__(user)
        self.adr = adr
        self.db = db
        self.adrSrv = AdresseService(db)


    
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.adrSrv = AdresseService(db)

    
    def save(self) -> bool:
        from database.models.user import User
        if super().isValid() and self.adrSrv.validAdresse(self.adr):
            adr = AdresseService(self.adr)
            user = User(None,
            super().getUser().getPassword(),
            super().getUser().getName(),
            super().getUser().getPhoneNumber(),
            super().getUser().getSexe(),
            adr.save())
            self.db.session.add(user)
            self.db.session.flush()
            id = user.id
            self.db.commit()
            return id
        return False
    
    def deleteById(self,id:str) -> bool:
        user = self.findById(id)
        if user is None:
            return False
        else:
            self.db.session.delete(user)
            self.db.session.commit()
        return True
    
    def findById(self,id:str):
        if(id.isalnum()):
            from database.models.user import User

            return User.query.filter_by(id = id).first()
        else : return None

    def findByEmail(self,email:str):
        if UserValidator().validEmail(email):
            from database.models.user import User

            return User.query.filter_by(email = email).first()
        else : return None
    
    def findByName(self,name:str):
        if super().validName(name) :
            searchName = "%{}%".format(name)
            from database.models.user import User

            return  User.query.filter(User.name.like(searchName)).all()
        return False

    def updatePassword(self,id,password) -> bool:
        if not super().validPassword(password): return False
        try:
            self.findById(id).password = password
            self.db.commit()
            return True
        except:
            return False
    
    def problemsFinder(self) -> list:
        return super().problemsFinder()
