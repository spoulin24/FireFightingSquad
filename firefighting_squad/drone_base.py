from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

class BaseDrone:
    def __init__(self, connection_string):
        self.vehicle = connect(connection_string, wait_ready=True)

    def arm_and_takeoff(self, target_altitude):
        while not self.vehicle.is_armable:
            print("Waiting for vehicle to become armable...")
            time.sleep(1)
        
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            print("Waiting for vehicle to become armed...")
            time.sleep(1)
        
        print("Taking off!")
        self.vehicle.simple_takeoff(target_altitude)

        while True:
            print(f"Altitude: {self.vehicle.location.global_relative_frame.alt}")
            if self.vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
                print("Reached target altitude")
                break
            time.sleep(1)

    def goto_location(self, location):
        self.vehicle.simple_goto(location)
        while self.vehicle.mode.name == "GUIDED":
            current_location = self.vehicle.location.global_relative_frame
            if self.calculate_distance(current_location, location) <= 1.0:  # 1 meter tolerance
                print("Reached target location")
                break
            time.sleep(1)

    def calculate_distance(self, loc1, loc2):
        return ((loc1.lat - loc2.lat)**2 + (loc1.lon - loc2.lon)**2)**0.5

    def land(self):
        print("Landing...")
        self.vehicle.mode = VehicleMode("LAND")
        while self.vehicle.armed:
            time.sleep(1)
        print("Landed and mission complete.")
        self.vehicle.close()
