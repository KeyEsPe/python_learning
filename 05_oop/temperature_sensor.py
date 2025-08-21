import random
import statistics

class TemperatureSensor:

    def __init__(self, name, location):
        self.name = name 
        self.location = location

    def read_temperature(self):
        return random.randint(18, 30)     # Draws random numbers from the range
    
class SensorSystem:

    def __init__(self):
        self.sensors = []
    
    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def calculate_average_temperature(self):
        temperatures = []  
        for sensor in self.sensors:
            temp = sensor.read_temperature()  
            temperatures.append(temp)  
        
        if temperatures:      # Check if the list is not empty 
            return statistics.mean(temperatures)     # Thanks to statistics module we can calculate average directly 
        else:
            return 0

my_sensors = SensorSystem()

sensor1 = TemperatureSensor("Netherlands", "Assen")
sensor2 = TemperatureSensor("Curacao", "Willemstad")
sensor3 = TemperatureSensor("Poland", "Busko-Zdroj")


my_sensors.add_sensor(sensor1)
my_sensors.add_sensor(sensor2)
my_sensors.add_sensor(sensor3)

average_temp = my_sensors.calculate_average_temperature()
rounded_average_temp = round(average_temp, 1)
print(f"Average temperature from all the sensors is: {rounded_average_temp}°C")


