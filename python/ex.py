import time


class CreateAccount:
    def __init__(self,user_id: int, username: str, email: str, birthday: str, adress: str, phonenumber: str | None = None) -> None:
        self.phonenumber = phonenumber
        self.birthday = birthday
        self.username = username
        self.user_id = user_id
        self.adress = adress
        self.email = email
        self.money = 0

    def userData(self):
        return self.user_id

    def moneyAccount(self):
        return self.money
    
    
print(time)

# main_user = CreateAccount()
# main_user.registerUser(1, "vitorMartins", "vitormartins@gmail.com", '07/10/1999', 'Rua Jóse Milani')
# print(main_user.userData())
