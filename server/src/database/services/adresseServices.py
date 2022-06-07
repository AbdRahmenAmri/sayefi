from database.validators.adresseValidator import AdresseValidator

class AdresseService(AdresseValidator):
    adr = None
    def __init__(self,adr,db) -> None:
        super().__init__(adr)
        self.adr = adr
        self.db = db
    
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db


    def save(self):
        if(super().isValid()):
            from database.models.adresse import Adresse

            validAdresse = Adresse(None,self.adr.getRegion(),self.adr.getAdresse,self.adr.getCity())
            self.db.session.add(validAdresse)
            self.db.session.flush()
            id = validAdresse.id
            self.db.commit()
            return id
        return False
    
    def findById(self,id:str):
        if(id.isalnum()):
            from database.models.adresse import Adresse

            return Adresse.query.filter_by(id = id).first()
        else : return None
    
    def deleteById(self,id:str) -> bool:
        adr = self.findById(id)
        if adr is None:
            return False
        else:
            self.db.session.delete(adr)
            self.db.session.commit()
        return True

    def findByRegion(self,region):
        if not super().validRegion(region):
            return None
        from database.models.adresse import Adresse
        return Adresse.query.filter_by(region = region).all()
    
    def findByAdresse(self,adresse):
        if not super().validAdresse(adresse):
            return None
        from database.models.adresse import Adresse
        return Adresse.query.filter_by(adresse = adresse).all()
    
    def findByCity(self,city):
        if not super().validCity(city):
            return None
        from database.models.adresse import Adresse
        return Adresse.query.filter_by(region = city).all()