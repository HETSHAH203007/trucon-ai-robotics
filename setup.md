# TRUCON AI — Development Environment Setup

**Intern:** Het Patel
**Role:** Robotics Software & Simulation Lead (Intern)
**Workspace:** `~/trucon_ws`

---

## System

| Component | Details |
|-----------|---------|
| OS | Ubuntu 22.04 LTS (via WSL2 on Windows) |
| ROS Version | ROS 2 Humble Hawksbill |
| Simulator | Gazebo (Classic / Fortress) |
| Shell | Bash |

---

## Prerequisites

Before cloning this repo, install the following:

```bash
# ROS 2 Humble (full desktop)
sudo apt install ros-humble-desktop

# Gazebo
sudo apt install gazebo

# Colcon build tool
sudo apt install python3-colcon-common-extensions

# Common ROS 2 extras
sudo apt install ros-humble-gazebo-ros-pkgs
sudo apt install ros-humble-robot-state-publisher
sudo apt install ros-humble-joint-state-publisher
```

---

## Clone & Build

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/trucon-ai-robot.git ~/trucon_ws/src/trucon-ai-robot

# Go to workspace root
cd ~/trucon_ws

# Build
colcon build

# Source
source install/setup.bash
```

---

## .bashrc Configuration

Add these lines to `~/.bashrc` in this exact order:

```bash
source /opt/ros/humble/setup.bash
source ~/trucon_ws/install/setup.bash

# Headless Gazebo (WSL2)
export LIBGL_ALWAYS_SOFTWARE=1
```

Then reload:

```bash
source ~/.bashrc
```

---

## Verify Setup

```bash
# Should return: /opt/ros/humble
echo $ROS_DISTRO

# Should list trucon packages (after adding them)
ros2 pkg list | grep trucon

# Health check
ros2 doctor
```

---

## Workspace Structure

```
trucon_ws/
├── src/
│   └── (ROS 2 packages go here)
├── build/        ← auto-generated, not committed
├── install/      ← auto-generated, not committed
└── log/          ← auto-generated, not committed
```

---

## Notes

- Always run `colcon build` from `~/trucon_ws/` (not from inside `src/`)
- After every build, re-source: `source install/setup.bash`
- For headless Gazebo in WSL2, prepend: `LIBGL_ALWAYS_SOFTWARE=1 gz_headless_mode:=True`