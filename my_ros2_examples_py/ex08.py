import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class FizzBuzz:

    def convert(self, num):
        if num % 15 == 0:
            return 'fizzbuzz'
        elif num % 3 == 0:
            return 'fizz'
        elif num % 5 == 0:
            return 'buzz'

        return str(num)


class Ex08Node(Node):

    def __init__(self):
        super().__init__('ex08_node')
        self.publisher = self.create_publisher(String, 'ans', 10)
        self.subscription = self.create_subscription(Int32, 'num', self.callback, 10)
        self.fizz_buzz = FizzBuzz()

    def callback(self, msg):
        ans = String()
        ans.data = self.fizz_buzz.convert(msg.data)
        self.publisher.publish(ans)


def main(args=None):
    try:
        rclpy.init(args=args)
        ex08_node = Ex08Node()
        rclpy.spin(ex08_node)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
