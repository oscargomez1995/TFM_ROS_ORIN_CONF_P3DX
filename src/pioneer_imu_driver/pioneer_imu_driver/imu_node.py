import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from smbus2 import SMBus
import math

class ImuNode(Node):
    def __init__(self):
        super().__init__('pioneer_imu_driver')

        self.bus_num = 7
        self.addr = 0x68
        self.bus = SMBus(self.bus_num)

        self.bus.write_byte_data(self.addr, 0x6B, 0x00)

        self.pub = self.create_publisher(Imu, '/imu/data_raw', 10)
        self.timer = self.create_timer(0.02, self.publish_imu)

        self.get_logger().info('IMU node started on I2C bus 7 address 0x68')

    def read_word(self, reg):
        high = self.bus.read_byte_data(self.addr, reg)
        low = self.bus.read_byte_data(self.addr, reg + 1)
        value = (high << 8) | low
        if value >= 0x8000:
            value -= 65536
        return value

    def publish_imu(self):
        ax = self.read_word(0x3B)
        ay = self.read_word(0x3D)
        az = self.read_word(0x3F)

        gx = self.read_word(0x43)
        gy = self.read_word(0x45)
        gz = self.read_word(0x47)

        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_link'

        accel_scale = 16384.0
        gyro_scale = 131.0

        msg.linear_acceleration.x = (ax / accel_scale) * 9.80665
        msg.linear_acceleration.y = (ay / accel_scale) * 9.80665
        msg.linear_acceleration.z = (az / accel_scale) * 9.80665

        msg.angular_velocity.x = math.radians(gx / gyro_scale)
        msg.angular_velocity.y = math.radians(gy / gyro_scale)
        msg.angular_velocity.z = math.radians(gz / gyro_scale)

        msg.orientation_covariance[0] = -1.0

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()