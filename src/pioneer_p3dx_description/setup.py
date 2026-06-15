from setuptools import find_packages, setup

package_name = 'pioneer_p3dx_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/display.launch.py', 'launch/gazebo.launch.py']),
    ('share/' + package_name + '/urdf', ['urdf/pioneer_p3dx.urdf']),
    ('share/' + package_name + '/worlds', ['worlds/empty.world']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryas_gremory',
    maintainer_email='ryas_gremory@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
