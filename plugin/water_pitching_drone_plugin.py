from .drone_base import BaseDrone

class WaterPitchingDrone(BaseDrone):
    def __init__(self, connection_string, fireline_location):
        super().__init__(connection_string)
        self.fireline_location = fireline_location

    def spray_water(self, jet_strength=100, orientation_angle=-45):
        print(f"Orienting at {orientation_angle} degrees...")
        self.vehicle.gimbal.rotate(orientation_angle, 0, 0)
        print(f"Spraying water with jet strength {jet_strength}...")
        time.sleep(10)

    def run_mission(self):
        self.arm_and_takeoff(20)
        self.goto_location(self.fireline_location)
        self.spray_water()
        self.land()
