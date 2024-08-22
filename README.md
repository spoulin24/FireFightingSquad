# Firefighting Squad
## QGIS Plugin for Drone System

## Overview

This project implements a multi-drone firefighting system that is seamlessly integrated as a QGIS plugin for ease of use. The system consists of two main types of drones: Water Delivery Drones (WDD) and Water Pitching Drones (WPD), with a built-in file-flying and space-keeping mechanism. Through the QGIS interface, users can easily manage and coordinate drone operations for firefighting missions, leveraging geographic data to control drone navigation and actions.

The system leverages drone synchronization, image recognition, real-time sensors, and autonomous navigation to coordinate the drones in performing their tasks.

![image](https://github.com/user-attachments/assets/e584a24c-eac4-4015-a8b3-ddfd947dac53)


### Features

- **Water Delivery Drones (WDD):** Collect water from a source, position themselves over a bladder using GPS and image recognition, and then drop the water into the bladder. All actions are controlled through the QGIS interface.
- **Water Pitching Drones (WPD):** Position themselves over a fireline, maintain a safe distance from the fire, and spray water with a controlled jet strength and orientation, all managed through QGIS.
- **File Flying and Space-Keeping Mechanism:** Ensures that drones in a file formation maintain proper spacing and orientation during movement from point A to point B, enhancing coordination and safety.
- **QGIS Integration:** Easily define regions of interest (ROI) using QGIS tools, visualize drone paths, and manage the entire firefighting operation within the familiar QGIS environment.

## Requirements

- QGIS (latest version)
- Python 3.x
- `dronekit` library
- A connected drone or SITL (Software in the Loop) simulation environment
- Water level sensor and pump mechanism for water collection (WDD)
- Gimbal for orientation control (WPD)
- Image recognition module (optional for advanced bladder positioning)
- Geographic data for the region of interest (ROI)

### Python Dependencies

You can install the required Python packages using pip:

```bash
pip install dronekit
```

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/drone-firefighting-system.git
   cd drone-firefighting-system
   ```

2. **Install QGIS Plugin:**
   - Copy the plugin folder from the repository into your QGIS plugin directory (typically found in `~/.qgis2/python/plugins` or `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins` depending on your QGIS version).

3. **Install Python Dependencies:**
   ```bash
   pip install dronekit
   ```

4. **Connect Your Drone:**
   - Ensure your drone is connected to your computer via a telemetry module, USB, or a simulated environment like SITL.
   - Modify the connection string in each script to match your setup (e.g., `127.0.0.1:14550` for SITL).

5. **Load the Plugin in QGIS:**
   - Open QGIS, navigate to the `Plugins` menu, and click on `Manage and Install Plugins`.
   - Find and activate the `Firefighting Squad` plugin.

## Project Structure

```plaintext
.
├── README.md                    # Project documentation
├── main.py                      # Main coordination script
├── water_delivery_drone.py       # Water Delivery Drone class
├── water_pitching_drone.py       # Water Pitching Drone class
├── drone_base.py                 # Base Drone class (common functionality)
└── roi.txt                       # Example ROI file containing coordinates
```

## Usage

### 1. Defining Regions of Interest (ROI)

Within QGIS, you can use existing geographic layers or draw your own polygons to define regions of interest (ROI) for water collection and firefighting.

- Use the `Select ROI` tool from the plugin toolbar to designate areas for water collection and fire suppression.
- Save these areas as files that will be used by the drones during their mission.

### 2. Running the Main Coordination Script

The main script manages the entire firefighting operation by deploying both Water Delivery Drones (WDD) and Water Pitching Drones (WPD). The number of drones and their respective connection strings are passed as command-line arguments.

#### Example Command:

```bash
python main.py --wdd 3 --wpd 3 --wdd_conns 127.0.0.1:14550 127.0.0.1:14551 127.0.0.1:14552 --wpd_conns 127.0.0.1:14553 127.0.0.1:14554 127.0.0.1:14555
```

- **`--wdd`:** Number of Water Delivery Drones to deploy.
- **`--wpd`:** Number of Water Pitching Drones to deploy.
- **`--wdd_conns`:** Connection strings for Water Delivery Drones.
- **`--wpd_conns`:** Connection strings for Water Pitching Drones.

### 3. Water Delivery Drone (WDD)

This drone collects water from a specified source and delivers it to a central bladder. The connection string for each drone is provided as a command-line argument.

#### Running the WDD Mission:

```bash
python water_delivery_drone.py --conn 127.0.0.1:14550
```

### 4. Water Pitching Drone (WPD)

This drone flies to the fireline and sprays water at a controlled jet strength and orientation. The connection string for each drone is provided as a command-line argument.

#### Running the WPD Mission:

```bash
python water_pitching_drone.py --conn 127.0.0.1:14553
```

### 5. File Flying and Space-Keeping Mechanism

This script manages drones flying in a file formation, ensuring they maintain proper spacing during movement. It is integrated into the QGIS plugin, allowing you to visualize and adjust formations in real-time.

## Configuration

### Adjusting Drone Parameters

- **Formation Distance:** Modify the `formation_distance` variable in the file-flying script to change the distance between drones in the file.
- **Jet Strength and Orientation:** Modify the `jet_strength` and `orientation_angle` parameters in the Water Pitching Drone script to control how water is sprayed.

### Gimbal and Sensor Integration

The scripts assume that your drone is equipped with a gimbal and water level sensor. If you're using SITL or if you need to customize these components, you'll need to modify the respective functions in the Water Delivery Drone script:

- **Gimbal Control:** The `vehicle.gimbal.rotate()` method controls the gimbal. Adjust the angles as needed.
- **Water Level Sensor:** The `is_water_full()` function is a placeholder. Integrate your sensor's logic to accurately monitor water levels.

## Troubleshooting

### Common Issues

- **Connection Issues:** Ensure your connection string is correct and the drone is properly connected.
- **Altitude Control:** If the drone doesn't reach the desired altitude, check the `arm_and_takeoff()` function for proper configuration.
- **Collision Avoidance:** If using real drones, implement additional safety measures like obstacle detection to prevent collisions.

### Debugging

- **Real-Time Feedback:** Use print statements in the scripts to monitor the drone's status and ensure the correct execution of commands.
- **Testing in SITL:** Before deploying on real hardware, test the system in a SITL environment to ensure everything functions as expected.

## Future Enhancements

- **Autonomous Task Allocation:** Implement dynamic task allocation where drones adjust roles based on the firefighting scenario.
- **Advanced Image Recognition:** Integrate an advanced image recognition system to further improve bladder positioning and fire detection.
- **Real-Time Communication:** Implement real-time communication between drones to enhance coordination and safety.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact

For any questions or support, feel free to contact the project maintainer at your-email@example.com.
