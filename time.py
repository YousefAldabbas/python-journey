from datetime import datetime
import time

class Time:

    def __init__(self,hours,minutes,second):
        self.hours = hours
        self.minutes = minutes
        self.second = second
    def __add__(self, other):
        if type(self) != type(other):
            raise Exception("Type miss match")
        self.hours += other.hours
        self.minutes += other.minutes
        self.second += other.second
        return '{}:{}:{}'.format(self.hours, self.minutes, self.second)

    def __sub__(self, other):

        if self.hours > other.hours:
            self.hours -= other.hours
        else:
            other.hours -= self.hours

        if self.minutes > other.minutes:
            self.minutes -= other.minutes
        else:
            other.minutes -= self.minutes

        if self.second > other.second:
            self.second -= other.second
        else:
            other.second -= self.second
        return '{}:{}:{}'.format(self.hours, self.minutes, self.second)

    def __str__(self):
        formatted_time = format(self.hours, '1.0f')+ ':'+ format(self.minutes, '1.0f')+ ':'+ format(self.second, '1.0f')
        return print(str(formatted_time))


x = Time(10, 15, 40)
y = Time(1, 0, 0)

# print(x+y)
# print(x-y)
print(x)