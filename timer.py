class Timer:
    def __init__(self, start):
        self.hours = start #Em horas absolutas
        self.minutes = 0
        self.days = 1


    def add_time(self, time_passed):
        self.minutes += time_passed #SEMPRE EM MINUTOS! MUITO IMPORTANTE.
        while self.minutes >=60:
            self.hours += 1
            self.minutes -= 60
            while self.hours >= 24:
                self.days += 1
                self.hours -= 24

    
    def clock(self):
        return f'São {self.hours} hora(s) e {self.minutes} minuto(s) do dia {self.days}.'






    
        