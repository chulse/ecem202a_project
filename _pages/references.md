---
permalink: /references/
title: "Reference Papers"
---

### [1] [Benchmark for Kitchen20, a Daily Life Dataset for Audio-based Human Action Recognition. Moreaux et al.](https://hal.archives-ouvertes.fr/hal-02901596/document)
This paper includes references to Kitchen20, a dataset useful in training our model to recognize a subset of our appliances. It also compares different types of models and arrives at a Convolutional Neural Network, which seems common with TinyML and other embedded system libraries.

### [2] [TinyML on Arduino and STM32: CNN example. Simone.](https://eloquentarduino.github.io/2020/11/tinyml-on-arduino-and-stm32-cnn-convolutional-neural-network-example/#tochow-to-run-a-cnn-on-arduino-and-stm32-boards-with-eloquenttinyml)
This is a quick tutorial on how to train CNNs and then run the corresponding model on a low power embedded microcontroller like arduino.

### [3] [Exploiting Environmental Sounds for Activity Recognition in Smart Homes. Tremblay et al.](https://www.aaai.org/ocs/index.php/WS/AAAIW15/paper/download/9697/10150)
This paper uses audio processing as a way to care for and monitor elderly people, with appliance classification as one way to detect human activity. To classify waveforms they use zero-crossing rates and a decision tree, which we can fall back on if the CNN with TinyML does not work, though it might not be robust enough to classify as diverse of an appliance pool as we would like.

### [4] [TinyEARS: Spying on House Appliances with Audio Sensor Nodes. Taysi et al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.8908&rep=rep1&type=pdf)
This paper uses audio to detect appliance states and correlate them with power draw. They try many different features and model types, and are able to succesffully monitor different states of a small number of appliances, along with how long they are on. Its more focused on power draw for given appliances, but is able to monitor how long they are on for pretty succesfully using several different types of models.

