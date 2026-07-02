import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration


class ArmControlNode(Node):

    def __init__(self):
        super().__init__('arm_control_node')
        self.publisher = self.create_publisher(
            JointTrajectory,
            '/arm_controller/joint_trajectory',
            10
        )
        self.timer = self.create_timer(2.0, self.run_sequence)
        self.step = 0
        self.get_logger().info('Arm control node started')

    def send_trajectory(self, right_angle, left_angle, duration_sec):
        msg = JointTrajectory()
        msg.joint_names = ['right_arm_joint', 'left_arm_joint']
        point = JointTrajectoryPoint()
        point.positions = [right_angle, left_angle]
        point.time_from_start = Duration(sec=duration_sec)
        msg.points = [point]
        self.publisher.publish(msg)
        self.get_logger().info(f'Sent: right={right_angle:.2f}, left={left_angle:.2f}')

    def run_sequence(self):
        if self.step == 0:
            self.get_logger().info('Step 1: Arms up')
            self.send_trajectory(1.0, 1.0, 2)
        elif self.step == 1:
            self.get_logger().info('Step 2: Arms down')
            self.send_trajectory(-1.0, -1.0, 2)
        elif self.step == 2:
            self.get_logger().info('Step 3: Arms neutral')
            self.send_trajectory(0.0, 0.0, 2)
        elif self.step >= 3:
            self.get_logger().info('Sequence complete')
            self.timer.cancel()
            return
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = ArmControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
