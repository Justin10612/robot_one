import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch_ros.actions import Node
from launch.event_handlers import OnProcessStart

def generate_launch_description():   
    
    # Change Meeee~~~~~~
    stm32_serial_port = "/dev/ttyACM4"
    
    set_serial_permission = ExecuteProcess(
        cmd=["sudo", "chmod", "666", stm32_serial_port],
        output='screen'
    )

    micro_ros_agent = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent',
        namespace='micro_ros_agent',
        output='screen',
        arguments=['serial', '-b', '115200', '--dev', stm32_serial_port])
    
    delayed_micro_ros_agent = RegisterEventHandler(
    event_handler=OnProcessStart(
        target_action=set_serial_permission,
        on_start=[micro_ros_agent],))

    # Launch!
    return LaunchDescription([
        # set_serial_permission,
        # delayed_micro_ros_agent,
        micro_ros_agent,
    ])
