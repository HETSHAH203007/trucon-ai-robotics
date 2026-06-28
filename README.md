# Trucon AI — Humanoid Desk Robot

**Robotics Software & Simulation | Intern Project**
Developed under the supervision of Founder — Ruchi M. Rajput

---

## About

This repository contains all ROS 2 software, Gazebo simulations, and hardware integration code for the Trucon AI humanoid desk robot — a privacy-first AI desk robot incubated at IIT Gandhinagar and Rashtriya Raksha University.

---

## Progress

| Week | Focus | Status |
|------|-------|--------|
| Week 1 | Environment Setup, Simulation, Vision, Movement | Done |
| Week 2 | Humanoid Simulation, Arm Integration | Upcoming |
| Week 3 | Voice Commands, Mobile App | Upcoming |

---

## Repository Structure

    trucon-ai-robot/
    ├── src/
    │   ├── trucon_description/     # URDF, Gazebo world, sensor plugins, diff drive
    │   ├── trucon_camera/          # Camera feed, face detection, human detection
    │   └── trucon_simulation/      # Reserved for future simulation worlds
    ├── SETUP.md
    └── README.md

---

## Tech Stack

- ROS 2 Humble — middleware and communication
- Gazebo 11 — physics simulation
- OpenCV + Haar Cascade + HOG — computer vision
- ESP32 — hardware microcontroller (Week 2)
- Python 3 — node development

---

## Setup

See SETUP.md for full environment setup instructions.

---

## Week 1 Deliverables

- [x] ROS 2 workspace configured
- [x] GitHub repository created
- [x] Gazebo simulation world
- [x] Robot URDF — 6 links, camera, IMU, proximity sensors
- [x] Robot spawn demo in Gazebo
- [x] Differential drive + keyboard teleoperation
- [x] Live camera feed via OpenCV
- [x] Face detection + human detection with bounding boxes
- [ ] ESP32 serial bridge — skipped (no hardware available)

---

## ROS 2 Topics

| Topic | Type | Description |
|-------|------|-------------|
| /head_camera/image_raw | sensor_msgs/Image | Robot head camera |
| /imu/data | sensor_msgs/Imu | IMU sensor |
| /proximity/range | sensor_msgs/Range | Proximity sensor |
| /cmd_vel | geometry_msgs/Twist | Velocity command input |
| /odom | nav_msgs/Odometry | Odometry output |

---

## Quick Start

    ros2 launch trucon_description gazebo.launch.py
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
    ros2 run trucon_camera camera_node
    ros2 run trucon_camera vision_node

---

## Daily Reports

Daily reports are submitted per the Trucon AI internship format covering tasks completed, code pushed, screenshots/videos, problems faced, hours worked, and next day's plan.

---

Working Hours: 6:00 PM - 12:00 AM (Mon-Sun)
