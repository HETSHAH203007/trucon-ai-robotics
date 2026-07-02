import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

def generate_launch_description():

    pkg = get_package_share_directory('trucon_description')

    urdf_file = os.path.join(pkg, 'urdf', 'trucon_robot.urdf')
    world_file = os.path.join(pkg, 'worlds', 'trucon_world.world')

    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', '/robot_description', '-entity', 'trucon_robot'],
            output='screen'
        ),

        TimerAction(
            period=5.0,
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'joint_state_broadcaster'],
                    output='screen'
                ),
            ]
        ),

        TimerAction(
            period=6.0,
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'gripper_controller'],
                    output='screen'
                ),
            ]
        ),

    ])
