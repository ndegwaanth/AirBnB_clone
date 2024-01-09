import uuid
import datetime


class BaseModel:
    """define all the common attribute/methods for other classes"""
    def __init__(self):
        """
            id (str):
                    this id is string in nature
            created_at (int):
                    this created_at attribut a datetime
            updated_at (int):
                    this also a datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """this method print the class name, id and all method in it"""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """update update_at with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """return a dictionary containing all the keys"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj


mybasemodelclass = BaseModel()
print(mybasemodelclass)
mybasemodelclass.save()
convert_basemode_dict = mybasemodelclass.to_dict()
print(convert_basemode_dict)
