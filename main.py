class Sensor:
   """Base class for all sensors."""


   def __init__(self, sensor_id, name, sensor_type):
       self.sensor_id = sensor_id
       self.name = name
       self.type = sensor_type

   def __str__(self):
       return f"Sensor ID: {self.sensor_id}, Name: {self.name}, Type: {self.type}"



class Robot:
   """Base class for all robots."""


   def __init__(self, robot_id, name, battery, status):
       self.robot_id = robot_id
       self.name = name
       self._battery = 0
       self.battery = battery
       self.status = status
       self.sensors = []
    
   @property
   def battery(self):
       """Getter: returns the internal _battery attribute."""
       return self._battery   
  
   @battery.setter
   def battery(self, value):
       """Setter: validates battery bounds whenever updated."""
       if value < 0 or value > 100:
           raise ValueError("Battery level must be between 0 and 100.")
       self._battery = value


   def add_sensor(self, sensor):
       """Adds a sensor to the robot's sensor list."""
       self.sensors.append(sensor)
      
   def check_sensor(self, sensor_id):
       """Checks if a sensor exists in the robot's sensor list by ID."""
       if len(self.sensors) == 0:
           print("No sensors are available.")
           return
       
       for sensor in self.sensors:
            print(f"Sensor found: {sensor}")
            return
       print(f"Sensor {sensor_id} was not found.")


   def move(self):
       """Moves the robot."""
       print(f"{self.name} is moving.")


   def __str__(self):
       """Displays the robot's current status."""
       return f"Robot: {self.name} ID: {self.robot_id} Battery: {self.battery}% Status: {self.status}"


class MobileRobot(Robot):
   """Class for mobile robots."""
   def __init__(self, robot_id, name, battery, status, speed):
       super().__init__(robot_id, name, battery, status)
       self.speed = speed


   def pick_up_object(self, object_name):
       """Picks up an object."""
       print(f"{object_name} is finished and is being shipped. {self.name} is picking up {object_name}.")

   def go_to_box(self, box_location):
         """Moves the robot to a specified box location."""
         print(f"{self.name} is moving to box at {box_location} with a speed of {self.speed}.")

   def place_object(self, object_name):
       """Places an object."""
       print(f"{self.name} is placing {object_name} in the box. The box is ready to be shipped.")


   def __str__(self):
       return f"{super().__str__()}, Wheel Count: {self.wheel_count} wheels."

class DroneRobot(Robot):
   """Class for drone robots."""
   
   def __init__(self, robot_id, name, battery, status, max_altitude):
       super().__init__(robot_id, name, battery, status)
       self.max_altitude = max_altitude
       self.objects = []  # List to hold objects being delivered
   
   def fly(self):
       """Makes the drone robot fly."""
       print(f"{self.name} is flying with {len(self.objects)} objects. Maximum altitude of {self.max_altitude} feet.")
    
   def delivering_package(self, package):
       """Delivers a package."""
       print(f"{self.name} is delivering {package}.")
       self.objects.append(package)
   
   def land(self):
       """Makes the drone robot land."""
       print(f"{self.name} is landing.")

   def delivered_package(self, package):
       """Confirms that a package has been delivered."""
       if package in self.objects:
            self.objects.remove(package)
            print(f"{self.name} has delivered {package}.")
       else:
            print(f"{package} is not currently being carried.")

   def __str__(self):
       return f"{super().__str__()}, Maximum Altitude: {self.max_altitude} feet"


def main():
   fleet = [] # List to hold all robots in the fleet
   robot_1 = MobileRobot(robot_id = 'MB01', name = "RoboMover", battery = 80, status = "Idle", wheel_count = 4)
   robot_2 = MobileRobot(robot_id = 'MB02', name = "RoboCarrier", battery = 70, status = "Active", wheel_count = 6)
   robot_3 = DroneRobot(robot_id = 'DR01', name = "SkyDeliver", battery = 90, status = "Idle", max_altitude = 500)
   fleet.extend([robot_1, robot_2, robot_3]) 
   print("Fleet of Robots:")
   for robot in fleet:
       print(robot)

if __name__ == "__main__":
   main()
