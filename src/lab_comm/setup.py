import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py')),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='dev@todo.todo',
    description='Package Komunikasi ROS 2 Modul 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = lab_comm.sensor_publisher:main',
            'processing_node = lab_comm.processing_node:main',
            'reset_service = lab_comm.reset_service:main',
            'motion_action_server = lab_comm.motion_action_server:main',
        ],
    },
)
