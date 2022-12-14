from glob import glob
import os

from setuptools import setup

package_name = 'my_ros2_examples_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Uchida Ryo',
    maintainer_email='uchidaryo.gm@gmail.com',
    description='my ROS2 Python examples',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ex01_node = my_ros2_examples_py.ex01:main',
            'ex02_node = my_ros2_examples_py.ex02:main',
            'ex03_publisher = my_ros2_examples_py.ex03_publisher:main',
            'ex03_subscriber = my_ros2_examples_py.ex03_subscriber:main',
            'ex04_service = my_ros2_examples_py.ex04_service:main',
            'ex04_client = my_ros2_examples_py.ex04_client:main',
            'ex05_node = my_ros2_examples_py.ex05:main',
            'ex07_node = my_ros2_examples_py.ex07:main',
            'ex08_node = my_ros2_examples_py.ex08:main',
        ],
    },
)
