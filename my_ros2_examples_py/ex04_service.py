from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class Ex04Service(Node):

    def __init__(self):
        super().__init__('ex04_service')
        self.service = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        return response


def main(args=None):
    try:
        rclpy.init(args=args)
        ex04_service = Ex04Service()
        rclpy.spin(ex04_service)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
