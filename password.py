class User():

    def __init__(self, name, surname, age, nickname, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.nickname = nickname
        self.password = password
        self.attempts = 0

    def get_logged(self):
        
        nickname = input('Enter your nickname: ')

        if self.nickname == nickname:
            print('You have entered a correct nickname.')
        elif self.nickname != nickname:
            print('You have entered a wrong nickname.')
            self.attempts = self.attempts + 1
        
        if self.nickname == nickname:
            password = input('Enter your password: ')
                
            if self.password == password:
                    print('You have succesfully logged to our site!')
            else:
                while self.password != password and self.attempts < 1:
                    self.attempts = self.attempts + 1
                    print('You have entered a wrong password.')

    def incorrect_attempts(self):
        print(f"Incorrect attempts: {self.attempts}.")

new_user = User('jan', 'kowalski', 29, 'jkowal12', 'Haslo123')
new_user.get_logged()
new_user.incorrect_attempts()