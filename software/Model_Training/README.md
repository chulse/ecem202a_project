Upload appliance_training.ipynb and appliance_dataset_new.py to a folder in your Google Drive (they must be in the same folder). You can open this file by clicking on it and it will automatically redirect you to Google Colab, which is similar to Jupyter Notebook. You will need to change the line: 

''' with open('/content/gdrive/My Drive/ECE202A/model_training/tf_lite_model.h', 'w') as f: '''

so that the generated file "tf_lite_model.h" is in whichever path you specify. Then run all the cells to see the performance of the model and its accuracy. Once you see that "tf_lite_model.h" is generated, copy that file into the same directory as predict_appliances.ino, which is the Arduino sketch that will do the real time predictions.