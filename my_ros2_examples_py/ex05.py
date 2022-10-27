import rclpy
from rclpy.node import Node


class Ex05Node(Node):

    def __init__(self):
        super().__init__('ex05_node')
        self.declare_parameter('my_parameter', 'world')
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value
        self.get_logger().info('Hello, %s!' % my_param)

        my_new_param = rclpy.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)


def main(args=None):
    try:
        rclpy.init(args=args)
        ex05_node = Ex05Node()
        rclpy.spin(ex05_node)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
