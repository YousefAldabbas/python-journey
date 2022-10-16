class Phone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return print('mobile phone '+ self.number +' is turned on')

    def turn_off(self):
        return print('mobile phone is turned off')

    def call(self, call_number):
        return print('calling '+call_number)


first_phone = Phone("01632-960004")
second_phone = Phone("01632-960012")

first_phone.turn_on()
second_phone.turn_on()

first_phone.call("555-34343")

first_phone.turn_off()
second_phone.turn_off()