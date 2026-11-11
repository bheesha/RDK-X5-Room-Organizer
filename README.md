# RDK X5 Room Organizer

## Project Overview

This project is being developed for the Robotics Dream Keeper Winter 2026 Challenge.

The goal is to build an intelligent mobile robot that can navigate a room, detect misplaced household objects, pick them up using a robotic arm, and organize them into designated baskets.

The project is currently in Stage 1.

## Hardware

- D-Robotics RDK X5
- 64GB microSD card
- 5.1V/5A USB-C power adapter
- Female-to-female jumper wire
- MacBook for development and SSH access

## Stage 1 — Ignite

### Task 1: Board Bring-Up — Completed

Successfully flashed RDKOS 3.5.0 Desktop (Ubuntu 22.04) using RDK Studio.

Booted the RDK X5 and established an SSH connection over USB-C.

**SSH command:**

`ssh root@192.168.128.10`

**Verification commands:**

`uname -a`

`cat /etc/os-release`

**Result:** Ubuntu 22.04.5 LTS, Linux kernel 6.1.83, ARM64.

### Task 2: Sensor Explorer — Completed

**Interface:** GPIO

Implemented a GPIO loopback experiment using a jumper wire connecting physical pins 31 and 37.

- Pin 31: Output
- Pin 37: Input
- Sent alternating HIGH and LOW signals
- Verified each signal using Python and the Hobot.GPIO library

**Run command:**

`python3 gpio_loopback.py`

**Result:** 4/4 tests passed.

### Task 3: First AI Task — Completed

**Task:** Image classification

**Model:** MobileNetV2

**Hardware:** RDK X5 BPU, core 0

Executed the preinstalled MobileNetV2 classification example using:

`cd /app/pydev_demo/01_classification_sample/02_mobilenetv2`

`python3 mobilenetv2.py`

**Result:** The model classified the sample image as a zebra with 99.36% confidence.

### Dependencies

- RDKOS 3.5.0 Desktop
- Ubuntu 22.04
- Python 3
- Hobot.GPIO
- Preinstalled D-Robotics MobileNetV2 demo and BPU runtime

### Troubleshooting

During setup, the USB-C SSH connection was interrupted. Reconnecting the board through RDK Studio restored communication.

The MobileNetV2 demo displayed a warning about differing model-builder and BPU-runtime versions, but inference completed and produced predictions.

## Stage 1 Evidence

Screenshots, wiring photographs, and the GPIO test script are stored in the `stage1/` directory.

## Stage 2 — Build

The next stage will focus on designing the mobile robot, robotic arm, vision system, navigation, ROS 2 architecture, and integration roadmap.
