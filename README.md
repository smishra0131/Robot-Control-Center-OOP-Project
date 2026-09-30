# Robot-Control-Center-OOP-Project

# Description
    The system will store robot data, monitor integrated sensors, update operational states, and execute custom commands.

# Features
    Has 2 mobile robots.
    
    Has 1 drone robot.
    
    Asks the user what item they want.
    
    The drone robot delivers the item to them.

# Instructions
	Run main.py
    
    Enter the item you want.
    
    Enter the location of the item in the warehouse.
    
    Enter the destination you want it to be delivered in. 
    
    Mobile robot will pick up the item and place it in the package.
    
    The drone will deliver it to the destination.
	
# OOP Concepts Breakdown
	Uses 4 classes, Sensor class, Robot class, 	MobileRobot class, and DroneRobot. 
	
    Uses the __init__() constructor to initialize.
    
    Uses property for the battery attributes.
    
    MobileRobot and DroneRobot inherit from the Robot class.
    
    Polymorphism is demonstrated through the perform_task() method.
    
    Composition is demonstrated through the Sensor and Robot classes.
    
    Magic methods are demonstrated by the use of __str__()

# Testing & Edge Cases
	Uses a setter that alerts the user when the battery is above 100 or below 0.
    
    Uses check_sensor() to search for a sensor.
    
    Both mobile robot and drone check whether they are carrying an item.
