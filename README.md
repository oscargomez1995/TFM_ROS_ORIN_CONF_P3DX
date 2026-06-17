# TFM ROS2 Pioneer P3-DX

Repositorio del TFM para integración del Pioneer P3-DX real y simulación en ROS 2 Humble.

## Contenido

- Pioneer P3-DX real mediante ros2aria.
- MPU9250 conectado a Jetson Orin Nano.
- Registro experimental mediante rosbag2.
- Fusión sensorial inicial con robot_localization.
- Simulación y descripción URDF del Pioneer P3-DX.

## Paquetes ROS 2

- src/Pioneer-3DX-ROS2/ros2aria
- src/Pioneer-3DX-ROS2/p3dx_description
- src/pioneer_p3dx_description
- src/pioneer_imu_driver
- src/pioneer_real_driver

## Datasets

- datasets/preliminary: pruebas iniciales.
- datasets/static: pruebas estáticas.
- datasets/linear: movimiento lineal.
- datasets/rotation: giros.
- datasets/fusion: pruebas con EKF.

## Configuración

- config/ekf_pioneer.yaml
