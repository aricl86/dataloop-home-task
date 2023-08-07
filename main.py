from dataclasses import dataclass

@dataclass
class Data:
    """
    A Pythonic data model class with to_dict and from_dict methods,
    ability to instantiate directly from the class, default value, autocomplete,
    dynamic and general usability for the class, and ability to reflect inner value on the main level.
    """
    id: str = "1"
    name: str = "first"
    size: float = 10.7
    height: int = 100
    metadata: dict = dataclasses.field(default_factory=dict)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_dict(cls, data: dict) -> "Data":
        """
        Create an object from a dictionary.

        """
        return cls(**data)

    def to_dict(self):
        """
        Convert the object to a dictionary.

        """
        return dataclasses.asdict(self)

    def __getattr__(self, item):
        """
        Get an attribute from the object.

        """
        if item == "me":
            return self.metadata
        raise AttributeError(f"'Data' object has no attribute '{item}'")
        
        
def main():

    # Read a dictionary and create a Data object from it
    dict_data = {
        "id": "1",
        "name": "first",
        "size": 10.7,
        "metadata": {"system": {"size": 10.7}, "user": {"batch": 10}},
    }
    new_data = Data.from_dict(dict_data)
    print(new_data)  # the dictionary representation of the new Data object

    # Convert the Data object to a dictionary
    data_dict = Data.to_dict(new_data)
    print(data_dict)  # the dictionary representation of the Data object

    
    data = Data(id="2", name="second", size=83.21, metadata={"system": {"size": 83.21}, "user": {"batch": 50}})

    # Reflect inner value on the main level
    print(data.me)

    # Ability to instantiate directly from the class
    data_2 = Data()
    print(data_2.id)

    # Default value
    print(data_2.height)

    # Autocomplete
    # Show the names of the attributes in the Data class
    print(dir(data))

    # Dynamic and general usability for the class (easily define new data structures)
    data_3 = Data(id="2", name="David", size=45.6, metadata={"dog": {"age": 6.5}, "owners": {"numer_of": 1}})
    print(data_3.me)  # Print the dictionary representation of the Data object


if __name__ == "__main__":
    main()
