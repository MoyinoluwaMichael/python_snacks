import datetime


class DateTime:

    def __init__(self):
        self.__date_time = datetime.datetime.now()
        self.__year: int = self.__date_time.year
        self.__month: int = self.__date_time.month
        self.__day: int = self.__date_time.day
        if self.__date_time.hour > 12:
            self.suffix: str = "PM"
            self.__hour: int = self.__date_time.hour % 12
        else:
            if self.__date_time.hour == 0:
                self.__hour = 12
            else:
                self.__hour: int = self.__date_time.hour
            self.suffix: str = "AM"
        self.__minute: int = self.__date_time.minute

    def __str__(self):
        return f"""
        Date: {self.__day}-{self.__month}-{self.__year}
        Time: {self.__hour}:{self.__minute} {self.suffix}"""
