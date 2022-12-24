from dataclasses import dataclass, field
@dataclass
class Account(object):
    userid: int
    firstname: str
    lastname: str
    phonenumber: int
    email:str
    password: str = field(default='123')
    cpassword: str = field(default='123')
    
    @property
    def password_match(self) -> bool:
        return self.password == self.cpassword
    # Class properties are declared and initialized by @dataclass