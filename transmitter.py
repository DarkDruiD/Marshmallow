import time
import random
import uav_pb2

import paho.mqtt.client as mqtt


def read_gps():
    gps = uav_pb2.GPS()

    gps.time_stamp = time.strftime("%H:%M:%S")
    gps.longitude = random.randint(0, 360)
    gps.latitude = random.randint(0, 360)

    return gps


def read_height():
    height = uav_pb2.Height()

    height.time_stamp = time.strftime("%H:%M:%S")
    height.height = random.randint(0, 100)

    return height


def read_gyro():
    gyro = uav_pb2.Gyroscope()

    gyro.time_stamp = time.strftime("%H:%M:%S")
    gyro.pitch = random.randint(0, 100)
    gyro.roll = random.randint(0, 100)

    return gyro


def read_accel():
    accel = uav_pb2.Accelerometer()

    accel.time_stamp = time.strftime("%H:%M:%S")
    accel.x = random.randint(0, 100)
    accel.y = random.randint(0, 100)
    accel.z = random.randint(0, 100)

    return accel


def build_drone_pkg():
    drn_pkg = uav_pb2.DronePackage()

    drn_pkg.time_stamp = time.strftime("%H:%M:%S")
    drn_pkg.gps.CopyFrom(read_gps())
    drn_pkg.height.CopyFrom(read_height())
    drn_pkg.gyro.CopyFrom(read_gyro())
    drn_pkg.accel.CopyFrom(read_accel())

    return drn_pkg


def on_connect(client, userdata, flags, rc):
    print "Connected!"


mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("127.0.0.1", 1883, 60)

mqttc.loop_start()

while True:
    drn_pkg = build_drone_pkg().SerializeToString()

    body = drn_pkg.encode('base64')
    #drn_pkg = bytearray(drn_pkg, 'ascii')
    #body = bytes(drn_pkg)

    mqttc.publish("uav/data", body)

    print "Sent data!"

    time.sleep(5)
