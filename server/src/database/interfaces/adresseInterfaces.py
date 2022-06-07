class AdresseInterfaces():
    regions = ['Tunis', 'Ariana', 'Ben Arous', 'Mannouba', 'Bizerte', 'Nabeul', 'Beja', 'Jendouba', 'Zaghouan', 'Siliana', 'Le Kef', 'Sousse', 'Monastir', 'Mahdia', 'Kasserine', 'Sidi Bouzid', 'Kairouan', 'Gafsa', 'Sfax', 'Gabes', 'Medenine', 'Tozeur', 'Kebili', 'Ttataouine']
    maxlength = 255

    def validRegion(self,region) -> bool:
        if not region.isalnum():
            return False
        for rg in self.regions:
            if(rg.lower == region):
                return True and len(region)<=self.maxlength
        return False

    def validAdresse(self,adresse) -> bool:
        if adresse is None: return False
        return adresse.isalnum() and len(adresse)<=self.maxlength

    def validCity(self,city) -> bool:
        return city.isalnum() and len(city)<=self.maxlength
    
'''    def validCoord(self, coord):
        coordTab = coord.split(',')
        if len(coordTab) == 2:
            try:
                float(coordTab[0])
                float(coordTab[1])
            except:
                return False
        else: return False
        return True'''