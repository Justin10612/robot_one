 # `robot_one`

This package contains the code and configuration files for running the robot in simulation with the `uwb_localization` package.

## Package Structure

The package structure is as follows:

- `launch`: Contains the launch files for launching the simulation.
- `src`: Contains the source code and configuration files for the robot.
- `config`: Contains the configuration files for the robot.

## Dependencies

The `robot_one` package depends on the following packages:

- `uwb_localization`: Provides the ultra-wideband localization functionality.

## Installation

1. Clone the `robot_one` package into your ROS workspace.

2. Install the necessary dependencies:

   ```bash
   rosdep install --from-paths src --ignore-src --rosdistro <your_ros_distro>
   ```

## Usage
To launch the simulation, run the following command:

    ```bash
    ros2 launch robot_one launch_uwb_bot.launch.py
    ```

This will launch the robot_one package in simulation with the uwb_localization package.

## Launch Files
The package contains the following launch files:

launch_uwb_bot.launch.py: Launches the simulation with the uwb_localization package.
Configuration Files
The package contains the following configuration files:

config/robot_one.yaml: Configuration file for the robot.
Feel free to modify these files according to your requirements.

Contributing
Contributions to the robot_one package are welcome! Please follow the guidelines for contributing to this package.