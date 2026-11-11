# RDK-X5-Room-Organizer
AI-powered mobile robot for detecting, picking up, and organizing household objects using RDK X5 and ROS 2.

# RDK X5 Room Organizer

## Project Overview

This project is being developed for the Robotics Dream Keeper Winter 2026 Challenge.

The goal is to create an intelligent mobile robot that can detect misplaced household objects, pick them up using a robotic arm, and organize them into designated baskets.

## Hardware

- D-Robotics RDK X5
- 64GB microSD card
- 5.1V/5A USB-C power supply
- Jumper wire for GPIO testing

Additional robotics hardware will be determined in Stage 2.

## Stage 1 — Ignite

### Task 1: Board Bring-Up
- Operating system: RDKOS 3.5.0 Desktop (Ubuntu 22.04)
- Flashing: In progress
- SSH connection: Pending

### Task 2: Sensor Explorer
- Interface: GPIO
- Planned experiment: GPIO loopback using a jumper wire
- Status: Pending

### Task 3: First AI Task
- Planned task: Image classification

I successfully ran the MobileNetV2 image classification demo on the D-Robotics RDK X5 using RDKOS 3.5.0 (Ubuntu 22.04).

The model executed using BPU core 0 and classified the sample image as a **zebra with 99.36% confidence**.

**Command used:**
```bash
cd /app/pydev_demo/01_classification_sample/02_mobilenetv2
python3 mobilenetv2.py
```

**Result:** Successful on-device AI inference.
## Setup Instructions

To be documented after successful board setup.

## Commands and Dependencies

To be added as experiments are completed.

## Results and Evidence

Screenshots, test logs, and results will be added after successful execution.

## Troubleshooting

Setup problems and their solutions will be documented here.

## Future Development

Stage 2 will focus on robot architecture, navigation, object detection, manipulation, and the hardware integration plan.
