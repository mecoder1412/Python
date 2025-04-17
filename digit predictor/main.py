# Import necessary libraries

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# load MNIST dataset
(x_train, y_train), (x_test, y_test)=tf.keras.datasets.mnist.load_data()
#Normalize the data
x_train,x_test=x_train/255.0,x_test/255.0
# Build the model
model= models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
#compile model
model.compile(optimizer='adam',
loss='spares_categorical_crossentopy',
metrics=['accuracy'])
#train model
model.fit(x_train, y_train, epochs=5)
#evaluate the model
test_loss, test_acc=model.evaluate(x_test,y_test)
print(f"Testing accuracy: {test_acc}")
#make predict
predictions=model.predict(x_test)
#display the first image and prediction
plt. imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()

