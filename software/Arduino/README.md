# capture_audio_samples.ino
Before doing anything, we need to collect audio samples from the Arduino. I recommend leaving the "PDM_SOUND_GAIN" to 50 
since I found that to yield good results later on. If this value is too small, then you might not be able to pick up noise 
that well, but if it is too high then the mic will be too sensitive to noise (PDM_SOUND_GAIN: 0 is min, 255 is the max).

If you change "TOTAL_SAMPLE", then you need to make sure each label has the same number of samples. Once you upload this to your Arduino, open the serial monitor and you should see the text ""# === Voice data start ===". This means you can start recording your audio and a new line with an array of "FEATURE_SIZE" data should print with the values for that audio sample. The values will be recorded if the the "SAMPLE_THRESHOLD" is exceeded.

Once you collect all the data, you should have "TOTAL_SAMPLE" number of lines. Copy and paste that into software/Model_Training/appliance_dataset_new.py and change the number of labels and appliance_data accordingly. Then follow the instructions in Model_Training.

# predict_appliances.ino
You should have trained the model in software/Model_Training/appliance_training.ipynb before you do this step. If you already did, replace the tf_lite_model.h file with the generated one from appliance_training.ipynb. Then, make sure the NUMBER_OF_LABELS in predict_appliances.ino is correct. Upload this sketch to the Arduino and watch it classify!