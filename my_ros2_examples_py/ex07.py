import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Foo:

    def func(self, num):
        return num + 1


class Ex07Node(Node):

    def __init__(self):
        super().__init__('ex07_node')
        self.publisher = self.create_publisher(Int32, 'ans', 10)
        self.subscription = self.create_subscription(Int32, 'num', self.callback, 10)
        self.foo = Foo()

    def callback(self, msg):
        ans = Int32()
        ans.data = self.foo.func(msg.data)
        self.publisher.publish(ans)


def main(args=None):
    try:
        rclpy.init(args=args)
        ex07_node = Ex07Node()
        rclpy.spin(ex07_node)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
