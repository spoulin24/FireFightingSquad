import threading
import argparse
from .water_delivery_drone import WaterDeliveryDrone
from .water_pitching_drone import WaterPitchingDrone
from dronekit import LocationGlobalRelative

# Initialize global variables
bladder_location = LocationGlobalRelative(-35.363261, 149.166230, 20)  # Replace with actual bladder coordinates
fireline_location = LocationGlobalRelative(-35.363261, 149.167230, 20)  # Replace with actual fireline coordinates
water_source_location = LocationGlobalRelative(-35.363261, 149.165230, 20)  # Replace with actual water source coordinates

def run_water_delivery_drones(num_drones, connection_strings):
    """Deploys the water delivery drones."""
    drones = []
    for i in range(num_drones):
        drone = WaterDeliveryDrone(connection_strings[i], water_source_location, bladder_location)
        drone_thread = threading.Thread(target=drone.run_mission)
        drones.append(drone_thread)
        drone_thread.start()

    for drone in drones:
        drone.join()

def run_water_pitching_drones(num_drones, connection_strings):
    """Deploys the water pitching drones."""
    drones = []
    for i in range(num_drones):
        drone = WaterPitchingDrone(connection_strings[i], fireline_location)
        drone_thread = threading.Thread(target=drone.run_mission)
        drones.append(drone_thread)
        drone_thread.start()

    for drone in drones:
        drone.join()

def main(num_wdd, num_wpd, wdd_conn_strings, wpd_conn_strings):
    # Step 1: Deploy Water Delivery Drones to collect water and fill the bladder
    print(f"Starting mission with {num_wdd} Water Delivery Drones...")
    run_water_delivery_drones(num_wdd, wdd_conn_strings)
    print("Water Delivery Drones have completed their mission.")

    # Step 2: Deploy Water Pitching Drones to spray water on the fireline
    print(f"Starting mission with {num_wpd} Water Pitching Drones...")
    run_water_pitching_drones(num_wpd, wpd_conn_strings)
    print("Water Pitching Drones have completed their mission.")

    print("Firefighting mission completed successfully!")
