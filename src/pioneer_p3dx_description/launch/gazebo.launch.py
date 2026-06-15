from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = FindPackageShare('pioneer_p3dx_description')

    world_file = PathJoinSubstitution([
        pkg_share,
        'worlds',
        'empty.world'
    ])

    urdf_file = PathJoinSubstitution([
        pkg_share,
        'urdf',
        'pioneer_p3dx.urdf'
    ])

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ]),
        launch_arguments={
            'gz_args': ['-r ', world_file]
        }.items()
    )

    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-file', urdf_file,
                    '-name', 'pioneer_p3dx',
                    '-x', '0',
                    '-y', '0',
                    '-z', '0.16'
                ],
                output='screen'
            )
        ]
    )

    cmd_vel_bridge = Node(
    	package='ros_gz_bridge',
    	executable='parameter_bridge',
    	arguments=[
       		'/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
    	],
    	output='screen'
    )

    return LaunchDescription([
        gz_sim,
        spawn_robot,
	cmd_vel_bridge
    ])
