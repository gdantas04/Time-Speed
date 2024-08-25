from datetime import datetime

class fastDT():
    def __init__(self, real_time , virtual_time):
        self._start = datetime.now()
        self.acceleration_factor = (real_time*3600)/virtual_time

    def get_simulated_time(self):
        elapsed_real_time = datetime.now() - self._start
        simulated_time_passed = elapsed_real_time * self.acceleration_factor
        return self._start + simulated_time_passed


fastTime = fastDT(24, 3) # quero que 24 horas passe em 3 segundos

