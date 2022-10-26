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
            'ex01_node = my_ros2_examples_py.ex01:main'
        ],
    },
)
