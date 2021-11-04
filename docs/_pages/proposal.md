---
permalink: /proposal/
title: "Proposal"
---

# Motivation & Objective
We want to create a non-invasive smart home monitoring system that uses one cheap device to monitor many appliances in a central room. This will allow homeowners to receive alerts when a certain appliance has been left running for an extended period of time. Users rely on many home appliances in their day to day lives, and having a monitoring system would allow users to direct their priorities to school or work, without having to stress about potentially leaving something on. 

# State of the Art & Its Limitations
Current smart home monitoring devices require every appliance to be smart, or many devices around the room, each monitoring a single appliance individually. Buying all these devices is expensive and generates lots of e-waste, which we hope to overcome with a cheap single device that can be placed in an arbitrary room and adjust to ambient conditions.

# Novelty & Rationale
Typical devices to detect whether certain kitchen appliances are being used depend on invasive sensors such as checking current and voltage values. However, our approach is non-invasive by placing a singular device in a room to detect multiple appliances primarily via audio classification. We have experimented with the Arduino Nano’s microphone by collecting raw values of various appliances and have experience loading machine learning models loaded onto the board. There are also large data sets on kitchen appliance noises available for us to use when training our audio classification model, so that our project could work in any household. 

# Potential Impact
The project has the ability to alert homeowners and college students alike when certain appliances have been left on, which can help them save on energy and utilities costs. Not only would this project help homeowners financially, it would also help the environment by reducing electricity and water usage.The project also has a safety aspect, as it can detect when the stove is left on and send a notification to users. This feature also serves as a convenient way for users to keep themselves and their home safe. On a technical level, this project relies heavily on audio datasets and can serve as the groundwork for detecting more safety-critical appliances, such as when the door has been opened, to prevent theft. 

# Challenges
Monitoring a room full of devices primarily using a microphone could be difficult depending on many factors, including: acoustic properties of the room, background noise, lots of appliances running at once, cheap hardware, and more. We hope to overcome these issues with machine learning techniques presented in our references section. This presents another challenge in training a model that accurately detects appliances in our home without overfitting to our environment. We hope to use a different apartment with different appliances at the end of our development to test how well our device would work in the real world.

# Requirements for Success
The main technical areas we plan to touch upon are: sensor data processing, machine learning, and bluetooth. We plan to use Arduino, PyTorch and tinyML libraries/tutorials to build our project. Skills in C and Python programming are necessary to record the audio for the datasets and to perform training and inference with the neural net model. Furthermore, the project requires skills in filtering data and performing simple audio processing techniques, to reduce the noise in the audio samples. 

# Metrics of Success
The main metric for success would be to check for a high test accuracy and/or low loss value on our kitchen appliance classification model. 

We would like to identify these 10 appliances:
 - Dishwasher
 - Microwave
 - Blender
 - Fridge (opening and closing)
 - Sink (water flowing) 
 - Stove fan running
 - Water boiling from kettle
 - Frying pan
 - Washing Machine
 - Dryer

Furthermore, we would like to be able to place our device in an unvisited apartment and still successfully identify nearby appliances. If anything unusual happens, like the fridge staying open longer than 5 minutes, the user will be notified of a potential problem. Too many notifications is worse than none at all, so we’d like to limit the false positive rate as much as possible.

# Execution Plan
Key tasks, sorted by author, include:
 - Chester:
  - Github pages website.
 - Jackie:
  - Collecting audio data on Arduino by experimenting with volume thresholds so that random noise is not collected and triggers the model appropriately to predict an output. 
 - Michelle:
  - Initial ML prototyping.

Other tasks (will be sorted by author as they are completed):
 - Preprocessing audio data to feed in the model
 - Experimenting with various models (neural net, svm, knn, random forest classifier) to see which yields highest test accuracy
 - Developing code for performing inference with the NN model on the Arduino
 - Communicating with a raspberry pi or phone over BLE to send notifications via email.
 - With possible back-end logic through IFTTT
 - Identifying kitchen appliance audio datasets and incorporating into model

# Related Work
## 9.a. Papers
### [1] [Benchmark for Kitchen20, a Daily Life Dataset for Audio-based Human Action Recognition. Moreaux et al.](https://hal.archives-ouvertes.fr/hal-02901596/document)
This paper includes references to Kitchen20, a dataset useful in training our model to recognize a subset of our appliances. It also compares different types of models and arrives at a Convolutional Neural Network, which seems common with TinyML and other embedded system libraries.

### [2] [TinyML on Arduino and STM32: CNN example. Simone.](https://eloquentarduino.github.io/2020/11/tinyml-on-arduino-and-stm32-cnn-convolutional-neural-network-example/#tochow-to-run-a-cnn-on-arduino-and-stm32-boards-with-eloquenttinyml)
This is a quick tutorial on how to train CNNs and then run the corresponding model on a low power embedded microcontroller like arduino.

### [3] [Exploiting Environmental Sounds for Activity Recognition in Smart Homes. Tremblay et al.](https://www.aaai.org/ocs/index.php/WS/AAAIW15/paper/download/9697/10150)
This paper uses audio processing as a way to care for and monitor elderly people, with appliance classification as one way to detect human activity. To classify waveforms they use zero-crossing rates and a decision tree, which we can fall back on if the CNN with TinyML does not work, though it might not be robust enough to classify as diverse of an appliance pool as we would like.

### [4] [TinyEARS: Spying on House Appliances with Audio Sensor Nodes. Taysi et al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.8908&rep=rep1&type=pdf)
This paper uses audio to detect appliance states and correlate them with power draw. They try many different features and model types, and are able to successfully monitor different states of a small number of appliances, along with how long they are on. It's more focused on power draw for given appliances, but is able to monitor how long they are on for pretty successfully using several different types of models.

### [5] [Ubicoustics: Plug-and-Play Acoustic Activity Recognition. Chris Harrison et al.](https://dl.acm.org/doi/10.1145/3242587.3242609)
This paper uses audio recognition to enable context-aware computing, where a device can tell what room it is in by recognizing certain appliance noises. The coolest part was how they synthesized new datasets by playing sound effects with emulated acoustic properties of different rooms. This let them train on a very large, high quality labeled dataset.

## 9.b. Datasets
[ESC-70](https://github.com/marc-moreaux/kitchen20). A dataset created in the Kitchen20 paper[1] that recognizes a subset of the appliances we are interested in.
[HAASD] (https://github.com/JYongSmile/paper-2018-HAASD/tree/master/HAASD) A dataset with audio files for washing machines.

## 9.c. Software
[Minimal Mistakes Jekkyl Theme.](https://github.com/mmistakes/minimal-mistakes)
[Edge Impulse Studio](https://docs.edgeimpulse.com/docs/audio-classification)

# 10. References
### [1] [Benchmark for Kitchen20, a Daily Life Dataset for Audio-based Human Action Recognition. Moreaux et al.](https://hal.archives-ouvertes.fr/hal-02901596/document)

### [2] [TinyML on Arduino and STM32: Convolutional Neural Network example. Simone.](https://eloquentarduino.github.io/2020/11/tinyml-on-arduino-and-stm32-cnn-convolutional-neural-network-example/#tochow-to-run-a-cnn-on-arduino-and-stm32-boards-with-eloquenttinyml)

### [3] [Exploiting Environmental Sounds for Activity Recognition in Smart Homes. Tremblay et al.](https://www.aaai.org/ocs/index.php/WS/AAAIW15/paper/download/9697/10150)

### [4] [TinyEARS: Spying on House Appliances with Audio Sensor Nodes. Taysi et al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.8908&rep=rep1&type=pdf)

### [5] [Ubicoustics: Plug-and-Play Acoustic Activity Recognition. Chris Harrison et al.](https://dl.acm.org/doi/10.1145/3242587.3242609)
