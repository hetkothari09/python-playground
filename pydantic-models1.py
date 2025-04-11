from pydantic import BaseModel, PositiveInt, ValidationError, field_validator
from datetime import datetime, date

'''
Pydantic is basically used to validate your data.
You can provide type hints that you require and pydantic will accordingly validate the data for you.
'''

class Person(BaseModel):

    name: str = "Het Kothari"
    age: int
    birth_date: date
    hobbies: dict[str, PositiveInt]

    @field_validator("birth_date")
    @classmethod
    def check_age(cls, birth_date: date) -> date:
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)

        if birth_date > eighteen_years_ago:
            raise ValueError("You must be atleast 18 years old!!!")

        return birth_date


data_validate = {
    "name": "Het Jaikar",
    "age": 21,
    "birth_date": "2004-03-29",
    "hobbies": {
        "sports": 3,
        "movies": 1,
        "songs": 2,
        "cooking": 5
    }
}

data_validate2 = {
    "name": "Het Jaikar",
    "age": 10,
    "birth_date": "2015-03-29",
    "hobbies": {
        "sports": 3,
        "movies": 1,
        "songs": 2,
        "cooking": 5
    }
}

try:
    person1 = Person(**data_validate)
    print(person1.name)
    print(person1.hobbies)
except ValidationError:
    print(f"All the validation checks for person1 donot pass!")


try:
    person2 = Person(**data_validate2)
    print(person2.name)
    print(person2.hobbies)
except ValidationError:
    print(f"All the validation checks for person2 donot pass!")