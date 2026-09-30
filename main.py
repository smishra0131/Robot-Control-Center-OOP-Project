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
              if sensor.sensor_id == sensor_id:
                print(f"Sensor found: {sensor}")
                return
       print(f"Sensor {sensor_id} was not found.")


   def perform_task(self, task):
       """Moves the robot."""
       print(f"{self.name} is performing {task}.")


   def __str__(self):
       """Displays the robot's current status."""
       return f"Robot: {self.name} ID: {self.robot_id} Battery: {self.battery}% Status: {self.status}"


class MobileRobot(Robot):
   """Class for mobile robots."""
   def __init__(self, robot_id, name, battery, status, max_speed):
       super().__init__(robot_id, name, battery, status)
       self.max_speed = max_speed
       self.items = []  # List to hold items being delivered


   def perform_task(self, item_location):
         """Moves the robot to a specified item location."""
         print(f"{self.name} is moving to item at {item_location} with a speed of {self.max_speed}.")
   
   def pick_up_item(self, item_name):
       """Picks up an item."""
       self.items.append(item_name)
       print(f"{self.name} is picking up {item_name}.")

   def place_item(self, item_name):
       """Places an item."""
       if item_name in self.items:
            self.items.remove(item_name)
            print(f"{self.name} is placing {item_name} in the box.")
            print("The box is ready to be shipped.")
       else:
           print(f"{item_name} is not currently being carried.")


   def __str__(self):
       """Displays the mobile robot's current status along with its maximum speed."""
       return f"{super().__str__()}, Maximum Speed: {self.max_speed} mph."

class DroneRobot(Robot):
   """Class for drone robots."""
   
   def __init__(self, robot_id, name, battery, status, max_altitude):
       super().__init__(robot_id, name, battery, status)
       self.max_altitude = max_altitude
       self.packages = []  # List to hold packages being delivered
    
   def pick_up_package(self, package_name):
        """Picks up a package."""
        self.packages.append(package_name)
        print(f"{self.name} is picking up {package_name}.")

   def fly(self):
       """Makes the drone robot fly."""
       print(f"{self.name} is flying with {len(self.packages)} packages. Maximum altitude of {self.max_altitude} feet.")
    
   def perform_task(self, package):
       """Delivers a package."""
       print(f"{self.name} is delivering {package}.")
       
   
   def land(self):
       """Makes the drone robot land."""
       print(f"{self.name} is landing.")

   def delivered_package(self, package):
       """Confirms that a package has been delivered."""
       if package in self.packages:
            self.packages.remove(package)
            print(f"{self.name} has delivered {package}.")
       else:
            print(f"{package} is not currently being carried.")

   def __str__(self):
       """Displays the drone robot's current status along with its maximum altitude."""
       return f"{super().__str__()}, Maximum Altitude: {self.max_altitude} feet"


def main():
   fleet = [] # List to hold all robots in the fleet
   mobile_robot_1 = MobileRobot(robot_id = 'MB01', name = "RoboMover", battery = 80, status = "Idle", max_speed = 4)
   mobile_robot_2 = MobileRobot(robot_id = 'MB02', name = "RoboCarrier", battery = 70, status = "Active", max_speed = 6)
   drone_robot_1 = DroneRobot(robot_id = 'DR01', name = "SkyDeliver", battery = 90, status = "Idle", max_altitude = 500)
   
   sensor_1 = Sensor("S01", "Camera", "Vision")
   sensor_2 = Sensor("S02", "Distance Sensor", "Proximity")
   sensor_3 = Sensor("S03", "GPS", "Navigation")
   
   mobile_robot_1.add_sensor(sensor_1)
   mobile_robot_1.add_sensor(sensor_2)
   mobile_robot_2.add_sensor(sensor_1)
   drone_robot_1.add_sensor(sensor_3)
   
   fleet.extend([mobile_robot_1, mobile_robot_2, drone_robot_1])
   
   item = input("Enter the item to be delivered: ")
   item_location = input("Enter the location of the item in the warehouse: ")
   destination = input("Enter the destination for delivery: ")
   
   mobile_robot_1.status = "Active"

   mobile_robot_1.perform_task(item_location)
   mobile_robot_1.pick_up_item(item)
   mobile_robot_1.place_item(item)
   
   mobile_robot_1.status = "Idle"

   package = item  # For simplicity, we treat the item as the package for delivery

   drone_robot_1.status = "Active"

   drone_robot_1.pick_up_package(package)
   print(f"{drone_robot_1.name} is flying to {destination}.")
   drone_robot_1.fly()
   drone_robot_1.perform_task(package)
   drone_robot_1.land()
   drone_robot_1.delivered_package(package)
   drone_robot_1.status = "Idle"
   print(f"Your item {item} has been delivered to {destination} by {drone_robot_1.name}.")


if __name__ == "__main__":
   main()
