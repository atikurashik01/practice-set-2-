import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# -----------------------------
# 1. Load MNIST dataset
# -----------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize input
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encoding of labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# -----------------------------
# 2. Build a simple model
# -----------------------------
model = Sequential([
    Flatten(input_shape=(28,28)),       # Flatten 28x28 image to vector
    Dense(128, activation='relu'),      # Hidden layer
    Dense(10, activation='softmax')     # Output layer
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# -----------------------------
# 3. Train the model
# -----------------------------
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# -----------------------------
# 4. Evaluate
# -----------------------------
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test Accuracy: {accuracy*100:.2f}%')