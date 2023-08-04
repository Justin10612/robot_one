import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():   
    # Note:Original command looks like 'docker run -it ...... --dev /dev/ttyACM0 -v6'
    # Replace "-it" to "-d":Means the program will backgroud running
    # Remove "-it"
    docker_run_command = "docker run --rm -v /dev:/dev -v /dev/shm:/dev/shm --privileged --net=host microros/micro-ros-agent:foxy serial --dev /dev/ttyACM0 -v6"
    
    docker_container = ExecuteProcess(
            cmd=["/bin/bash", "-c", docker_run_command],
            output="screen",
    )

    # Launch!
    return LaunchDescription([
        docker_container,
    ])