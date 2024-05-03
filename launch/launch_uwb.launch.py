import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node 
from launch.substitutions import Command
from launch.actions import RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessStart


def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='robot_one' #<--- CHANGE ME

    twist_mux_params = os.path.join(get_package_share_directory(package_name),
                                    'config',
                                    'twist_mux_1.yaml')

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name),'launch','rsp.launch.py')]
        ), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    joystick = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name),'launch','joystick.launch.py')]
        ), launch_arguments={'use_sim_time': 'false'}.items()
    )

    # lidar = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         [os.path.join(get_package_share_directory("ydlidar_ros2_driver"),'launch','ydlidar_launch.py')]
    #     )
    # )

    robot_controller = Node(
        package='robot_controller_cpp',
        executable='robot_controller_cpp',
        output='screen',
    )

    uwb_sensor = Node(
        package='uwb_localization',
        executable='uwb_receiver',
        output='screen'
    )

    uwb_localization = Node(
        package='uwb_localization',
        executable='3d_localization',
        output='screen'
    )

    # Launch them all!
    return LaunchDescription([
        rsp,
        robot_controller,
        joystick,
        uwb_sensor,
        uwb_localization
    ])