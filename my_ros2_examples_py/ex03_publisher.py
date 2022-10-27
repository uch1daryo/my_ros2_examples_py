import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Ex03Publisher(Node):

    def __init__(self):
        super().__init__('ex03_publisher')
        self.publisher = self.create_publisher(String, 'topic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, ROS2 Python world!'
        self.publisher.publish(msg)


def main(args=None):
    try:
        rclpy.init(args=args)
        ex03_publisher = Ex03Publisher()
        rclpy.spin(ex03_publisher)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
