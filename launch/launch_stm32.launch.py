import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():   

    set_serial_permission = ExecuteProcess(
        cmd=["sudo", "chmod", "666", "/dev/ttyACM0"],
        output='screen'
    )

    micro_ros_agent = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent',
        namespace='micro_ros_agent',
        output='screen',
        arguments=['serial', '-b', '115200', '--dev', '/dev/ttyACM0'])

    # Launch!
    return LaunchDescription([
        set_serial_permission,
        micro_ros_agent,
    ])