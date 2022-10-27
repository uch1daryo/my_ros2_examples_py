import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class Ex04Client(Node):

    def __init__(self):
        super().__init__('ex04_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        self.request = AddTwoInts.Request()

    def send_request(self, a, b):
        self.request.a = a
        self.request.b = b
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    ex04_client = Ex04Client()
    response = ex04_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    ex04_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))


if __name__ == '__main__':
    main()
