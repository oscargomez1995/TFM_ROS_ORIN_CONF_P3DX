# TFM ROS2 Pioneer P3-DX

## Español

Repositorio del Trabajo Fin de Máster (TFM) para la integración del robot móvil Pioneer P3-DX real y su simulación en ROS 2 Humble.

### Contenido

* Integración del Pioneer P3-DX real mediante ros2aria.
* Sensor MPU9250 conectado a una Jetson Orin Nano.
* Registro experimental de datos mediante rosbag2.
* Fusión sensorial inicial utilizando robot_localization.
* Simulación y descripción URDF del Pioneer P3-DX.

### Paquetes ROS 2

* `src/Pioneer-3DX-ROS2/ros2aria`
* `src/Pioneer-3DX-ROS2/p3dx_description`
* `src/pioneer_p3dx_description`
* `src/pioneer_imu_driver`
* `src/pioneer_real_driver`

### Datasets

* `datasets/preliminary`: pruebas iniciales.
* `datasets/static`: pruebas estáticas.
* `datasets/linear`: movimiento lineal.
* `datasets/rotation`: giros.
* `datasets/fusion`: pruebas con EKF.

### Configuración

* `config/ekf_pioneer.yaml`

---

## English

Master's Thesis repository for the integration of the real Pioneer P3-DX mobile robot and its simulation using ROS 2 Humble.

### Contents

* Real Pioneer P3-DX integration through ros2aria.
* MPU9250 sensor connected to a Jetson Orin Nano.
* Experimental data recording using rosbag2.
* Initial sensor fusion using robot_localization.
* Pioneer P3-DX simulation and URDF description.

### ROS 2 Packages

* `src/Pioneer-3DX-ROS2/ros2aria`
* `src/Pioneer-3DX-ROS2/p3dx_description`
* `src/pioneer_p3dx_description`
* `src/pioneer_imu_driver`
* `src/pioneer_real_driver`

### Datasets

* `datasets/preliminary`: initial tests.
* `datasets/static`: static tests.
* `datasets/linear`: linear motion tests.
* `datasets/rotation`: rotation tests.
* `datasets/fusion`: EKF fusion experiments.

### Configuration

* `config/ekf_pioneer.yaml`

---

## Hardware Platform

* Pioneer P3-DX Mobile Robot
* NVIDIA Jetson Orin Nano
* MPU9250 IMU Sensor
* ROS 2 Humble Hawksbill

## Research Objectives

This project aims to develop and evaluate a multimodal perception and localization framework for autonomous mobile robots operating in indoor and semi-structured environments. The system combines wheel odometry, inertial sensing, and sensor fusion techniques to improve localization accuracy and provide a foundation for future autonomous navigation experiments.
