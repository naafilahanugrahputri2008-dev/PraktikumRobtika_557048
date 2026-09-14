import rclpy
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node
from std_msgs.msg import Float32


class ProcessingNode(Node):

    def __init__(self):
        super().__init__('processing_node')
        self.declare_parameter('threshold', 0.5)
        self.count_above = 0
        self.sub = self.create_subscription(
            Float32, 'sensor_data', self.on_data, 10
        )
        self.pub = self.create_publisher(Float32, 'processed_data', 10)
        self.add_on_set_parameters_callback(self.on_param)
        self.get_logger().info('Processing Node telah aktif!')

    def on_param(self, params):
        for p in params:
            if p.name == 'threshold':
                try:
                    val = float(p.value)
                    if val < 0.0:
                        return SetParametersResult(
                            successful=False,
                            reason='threshold must be >= 0',
                        )
                except (ValueError, TypeError):
                    return SetParametersResult(
                        successful=False,
                        reason='threshold must be numeric',
                    )
        return SetParametersResult(successful=True)

    def on_data(self, msg):
        th = float(self.get_parameter('threshold').value)
        if abs(msg.data) > th:
            self.count_above += 1
            self.pub.publish(msg)
            self.get_logger().info(
                f'Data sensor di atas threshold ({th}): {msg.data:.2f}'
            )


def main(args=None):
    rclpy.init(args=args)
    node = ProcessingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
