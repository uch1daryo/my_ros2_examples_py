import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Ex03Subscriber(Node):

    def __init__(self):
        super().__init__('ex03_subscriber')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    try:
        rclpy.init(args=args)
        ex03_subscriber = Ex03Subscriber()
        rclpy.spin(ex03_subscriber)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
