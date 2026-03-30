import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# FIX 1: Import the necessary library and load the model
# -----------------------------------------------------
from tensorflow.keras.models import load_model 

# Load the model you saved in the notebook
try:
    model = load_model('mnist_model.h5')
    print("Model loaded successfully from mnist_model.h5")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Please make sure you ran 'model.save(\"mnist_model.h5\")' in your notebook.")
    exit() # Stop the script if the model can't be loaded

# 1. Create a blank black image (28x28 pixels)
# We use zeros for black background, matching the MNIST data format.
my_test_image = np.zeros((28, 28))

# 2. "Draw" a digit '1' manually (You can change this to draw other digits)
# Setting pixels in the middle to white (1.0) to form a vertical line for '1'
my_test_image[4:24, 13:15] = 1.0  
my_test_image[5:7, 12:13] = 1.0 # Add a small corner to the top left of '1'

# 3. Preprocessing (Making it fit the model)
# The model expects one sample with 784 features (28*28 flattened).
processed_image = my_test_image.reshape(1, 784).astype('float32')

# 4. Ask the model to predict (This line now works because 'model' is defined)
prediction_probabilities = model.predict(processed_image)
predicted_label = np.argmax(prediction_probabilities)

# 5. Show the result
# Display the image we drew
plt.figure(figsize=(4, 4))
plt.imshow(my_test_image, cmap='gray')
plt.title(f"I drew a '1'. Model predicts: {predicted_label}")
plt.show()

# 6. Check if it worked
if predicted_label == 1:
    print("\n✅ Success! The model correctly identified the custom image.")
else:
    print(f"\n❌ Oops! The model predicted: {predicted_label}. The model missed the digit '1'.")

# Print the confidence scores (useful for debugging)
print("\nConfidence Scores (Probabilities for each digit 0-9):")
print(prediction_probabilities)