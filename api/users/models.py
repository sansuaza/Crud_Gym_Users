import uuid
class User:

    def  __init__(self, name, last_name,identification, phone_number, wight, height, age):
        self.name = name
        self.last_name = last_name
        self.identification = identification
        self.phone_number = phone_number
        self.wight = height
        self.height = height
        self.age = age
        self.uid = uuid.uuid4()

    def to_dict(self):
        """Handle of return the atributes of a user, like a dictionary."""
        return vars(self)
        #vars en una función global que retorna en diccionario el objeto

    @staticmethod
    def schema():
        return ['name', 'last_name', 'identification', 'phone_number', 'wight', 'height', 'age', 'uid']