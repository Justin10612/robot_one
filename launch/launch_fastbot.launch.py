import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='robot_one' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name),'launch','rsp.launch.py')]
        ), launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    joystick = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','joystick.launch.py'
        )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    rb_controller = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('rb_controller'),'launch','launch_rb_controller.launch.py')]
        )
    )

    diff_drive_controller = Node(
        package='diff_drive_controller_cpp',
        executable='diff_cont_cpp',
        output='screen',
    )

    # robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])
    # # robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])
    # controller_params_file = os.path.join(get_package_share_directory(package_name),'config','robot_control.yaml')


    # Launch them all!
    return LaunchDescription([
        rsp,
        rb_controller,
        joystick,
        diff_drive_controller,
    ])