import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = Node('ex01_node')
    node.get_logger().info('Hello, ROS2 Python world!')


if __name__ == '__main__':
    main()
