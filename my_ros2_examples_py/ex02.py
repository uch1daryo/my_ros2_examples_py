import rclpy
from rclpy.node import Node


def main(args=None):
    try:
        rclpy.init(args=args)
        node = Node('ex02_node')
        node.get_logger().info('Hello, ROS2 Python world!')
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
