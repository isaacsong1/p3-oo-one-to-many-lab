# import ipdb; ipdb.set_trace()

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception            
        else:
            self._name = new_name
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type in type(self).PET_TYPES:
            self._pet_type = new_pet_type
        else:
            raise Exception
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        if not (isinstance(new_owner, Owner) or not new_owner):
            raise TypeError("Object is not of type Owner")
        else:
            self._owner = new_owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input but be of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

