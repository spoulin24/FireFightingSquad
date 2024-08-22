from .drone_base import BaseDrone

class WaterDeliveryDrone(BaseDrone):
    def __init__(self, connection_string, water_source, bladder_location):
        super().__init__(connection_string)
        self.water_source = water_source
        self.bladder_location = bladder_location

    def take_water_with_gimbal(self):
        print("Positioning gimbal...")
        self.vehicle.gimbal.rotate(-90, 0, 0)
        print("Filling water...")
        while not self.is_water_full():
            time.sleep(1)
        print("Water tank is full. Stopping the pump.")

    def is_water_full(self):
        return True

    def position_over_bladder_and_drop_water(self):
        print("Positioning over bladder using GPS...")
        self.goto_location(self.bladder_location)
        print("Dropping water...")
        self.drop_water()

    def drop_water(self):
        print("Releasing water...")
        time.sleep(5)

    def run_mission(self):
        self.arm_and_takeoff(20)
        self.goto_location(self.water_source)
        self.take_water_with_gimbal()
        self.position_over_bladder_and_drop_water()
        self.land()
