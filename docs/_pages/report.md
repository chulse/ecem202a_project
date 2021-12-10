---
permalink: /report/
title: "Report"
---

## Abstract

Current smart home monitoring requires many smart devices all reporting their status and collecting data. For many homes, the overhead and cost of replacing "dumb" appliances is not worth the new features that these new smart appliances provide. We would like to use a cheap single device placed in a per-room basis to monitor appliances and alert home-owners of unusual activity, like the fridge being left open, to "smartify" a home without replacing or upgrading all of its current appliances individually. We have achieved this on low power embedded device by monitoring ambient noises to classify which appliances are currently in use. We have successfully been able to classify home appliances with above 90% accuracy when they are in use by themselves, but future work is necesary before our system is robust enough to detect simultaneous appliances and truly compete with a home fully equipped with smart devices.

## Technical Approach
### Hardware
#### Arduino Nano 33 BLE
This is a small low cost device with a microphone and BLE. It is also very common for IOT project examples online and has many libraries built just for it. It allowed us to iterate our design and prototype quickly.
![Arduino Nano 33 BLE](/assets/images/tux.png)
#### Raspbeery Pi Zero W
This is again a small low-cost device that allowed us to prototype quickly. The RPI Zero W is a small computer capable of running linux and python, while also using BLE to connect to one or more Arduino Nano 33 BLE edge devices. We envision it acting as a hub in a house, connecting to a cheap low-cost appliance monitoring device in every room, capable of monitoring the whole home over BLE.
![Raspberry PI Zero W](/assets/images/tux.png)

### Datasets
### Edge Impulse and CNN
### BLE + IFTTT

## Results

## Future Work

## Team and Contribution Breakdown

## References

