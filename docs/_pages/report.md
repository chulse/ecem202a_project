---
permalink: /report/
title: "Report"
---

## Abstract

Current smart homes require many smart devices all reporting their status and collecting data. For many homes, the overhead and cost of replacing "dumb" appliances is not worth the new features that these new smart appliances provide. We would like to use a cheap single device placed in a per-room basis to monitor appliances and alert home-owners of unusual activity, like the fridge being left open, to "smartify" a home without replacing or upgrading all of its current appliances individually. We have achieved this on low power embedded device by monitoring ambient noises to classify which appliances are currently in use. We have successfully been able to classify home appliances with above 90% accuracy when they are in use by themselves, but future work is necessary before our system is robust enough to detect simultaneous appliances and truly compete with a home fully equipped with smart devices.


![BlockDiagram]({{ site.url }}{{ site.baseurl }}/assets/images/block_diagram.PNG){: .align-center}

## Technical Approach
### Hardware
#### Arduino Nano 33 BLE
This is a small low cost device with a microphone and BLE. It is also very common for IOT project examples online and has many libraries built just for it. It allowed us to iterate our design and prototype quickly.
![ArduinoNano33BLE]({{ site.url }}{{ site.baseurl }}/assets/images/nano33ble.jpg){: .align-center}
#### Raspberry Pi Zero W
This is again a small low-cost device that allowed us to prototype quickly. The RPI Zero W is a small computer capable of running linux and python, while also using BLE to connect to one or more Arduino Nano 33 BLE edge devices. We envision it acting as a hub in a house, connecting to a cheap low-cost appliance monitoring device in every room, capable of monitoring the whole home over BLE.
![RPIZeroW]({{ site.url }}{{ site.baseurl }}/assets/images/RPI.jpg){: .align-center}

### Datasets
One important piece of our project is creating a product that can be used in a variety of situations without a specific setup. One key way we accomplish this is to train our machine learning classifier on public datasets for many different kinds of the same appliance. We used two main datasets for this, [Kitchen20]((https://github.com/marc-moreaux/kitchen20) and [HAASD](https://github.com/JYongSmile/paper-2018-HAASD/tree/master/HAASD). For appliances that we couldn't find reliable sources for, we recorded our own data at two of our apartments and then used a third apartment as our "test" set, where we tested our end result on data that wasn't used to train our model. This gave us a pretty robust classification system for the appliances we were targeting, assuming only one was on at once. One thing we think would be interesting in the future would be classifying multiple devices at once. This could potentially  be achieved by training the classifier on combined datasets or take a more elegant signal processing approach.

### Edge Impulse and CNN
We chose to use a machine learning framework called [Edge Impulse](https://www.edgeimpulse.com/). This website presents a nice way to visualize audio data and the corresponding features you generate with, for example, an FFT.

Not only did it have great visualizations, it also let you import data as .mp3 files, or even record from an iphone or an arduino. Recording data from the arduino microphone we were actually planning to classify from was super useful, as its acoustic properties are obviously different from whatever kitchen20 or our iphone microphones. We imported the datasets mentioned before and then strengthened their classifying by supplementing this dataset with data recorded directly on our arduino.

After visualizing features and sampling data, Edge Impulse lets you train various neural networks with different parameters and different augmentations on your data. We were able to add random noise and try different numbers of layers until we achieved a model that performed well without overfitting.

Finally, edge impulse supports exporting a library that implements your desired CNN in C++ that can be loaded directly onto an Arduino. This was a huge timesaver for prototyping, we could just write arduino code that calls their basic functions and rapidly iterate different machine learning libraries on the Arduino BLE until we were happy with it.

### BLE + IFTTT
Our last major goal of the project was notifying the user if appliances were being used for too long. The Arduino Nano 33 BLE doesn't support wifi, and buying an Arduino that does would increase the low-cost aspect of having one of these in every room with appliances. Instead, we envisioned a network of Arduinos transmitting classified appliances to a central raspberry pi hub over BLE. BLE is perfect for the low power transmissions we need, with the only downside being privacy implications which could be fixed in future work with a different communication scheme.

With this network, the nearby Arduinos all transmit an appliance characteristic with "Notify" properties. A raspberry pi subscribes to this characteristic, and every time it is notified stores timing information for that appliance. If a threshold for notifications is reached, like water running for more than 10 seconds, or the fridge being open for longer than 15 seconds, it will send an HTTP request to IFTTT to trigger an email notification to the owner.

The raspberry pi bluetooth code was created to be independent from the arduino to allow for easy testing, you can simulate any appliances by just sending BLE messages without needing a working classifier and vice versa. This also allows room in the future for new sensors or IOT devices to publish device information to the same raspberry pi hub.

## Results

Our classifier is able to reach a test accuracy of 91%. For a list of 10 appliances this is a significant achievement. Our biggest struggle was properly classifying the water kettle, which is surprising considering how distinct the sound is to our human ears. 

![ConfusionMatrix]({{ site.url }}{{ site.baseurl }}/assets/images/confusion.png){: .align-center}

This was also true of our experiments in person, the kettle misclassified much more often than any of our other appliances, while the rest seemed to have a test accuracy around 90%, as shown in our demo video. If I were to guess, I'd say that this was because of distortions in our different microphones, the relatively high frequency of the sound was poorly captured by our audio devices.


## Future Work
We've thought of a couple future directions this project could take:
 - Explore classification of multiple appliances at once, whether that be through some kind of multi-microphone setup, signal processing, or machine learning classification.
 - Collect data on usage patterns over time and train models on what appliance usage is notification worthy vs. what is excessive and unnecessary.
  - Potentially have each arduino or raspberry pi learn on the edge. Everyone's usage patterns will have slight different quirks.
 - Explore fusing different input sensor data, such as ambient light or vibrations.

## Team and Contribution Breakdown

Chester Hulse:
 - Edge Impulse data collection
 - Initial Arduino classifier prototyping
 - Arduino BLE application
 - Raspberry PI BLE and IFTTT application
 - Website markdown

Jackie Lam: 
 - Edge Impulse data collection
 - Initial Arduino classifier prototyping
 - Edge Impulse Classifier Work
   - Training
   - Tuning model
   - Configuring features
 - Integration of Edge Impulse library code and BLE code

Michelle Tan: 
 - Edge Impulse data collection
 - Initial Arduino classifier prototyping
 - Edge Impulse Classifier Work
   - Training
   - Tuning model
   - Configuring features

## References

See our [Project Proposal](https://chulse.github.io/ecem202a_project/proposal/#related-work).