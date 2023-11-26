import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='robot_one' #<--- CHANGE ME

    twist_mux_params = os.path.join(get_package_share_directory(package_name),
                                    'config',
                                    'twist_mux.yaml')

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

    robot_controller = Node(
        package='robot_controller_cpp',
        executable='robot_controller_cpp',
        output='screen',
    )

    diff_drive_controller = Node(
        package='diff_drive_controller_cpp',
        executable='diff_cont_cpp',
        output='screen',
    )

    human_follower_py = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('rb_controller'), 'launch', 'human_follower.launch.py')]
        )
    )

    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        parameters=[
            {'use_sim_time': False},
            twist_mux_params],
        # remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
    )


    # Launch them all!
    return LaunchDescription([
        rsp,
        robot_controller,
        joystick,
        diff_drive_controller,
        human_follower_py,
        twist_mux,
    ])