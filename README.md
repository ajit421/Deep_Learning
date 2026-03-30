# Deep Learning Projects

A comprehensive collection of deep learning implementations focusing on image classification and convolutional neural networks using TensorFlow/Keras and the MNIST dataset.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Projects](#projects)
  - [Image Classification](#image-classification)
  - [CNN Implementation](#cnn-implementation)
  - [Custom Digit Recognition](#custom-digit-recognition)
- [Model Architecture](#model-architecture)
- [Visualization Resources](#visualization-resources)
- [Requirements](#requirements)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains practical implementations of deep learning concepts, specifically focusing on:
- **Image Classification** using neural networks
- **Convolutional Neural Networks (CNN)** for pattern recognition
- **MNIST Handwritten Digit Recognition**
- **Custom Image Prediction** using trained models

The projects demonstrate the complete machine learning workflow from data preprocessing, model training, evaluation, to deployment and inference.

## 📁 Project Structure

```
Deep_Learning/
│
├── Image_Classification/
│   ├── Image_Classification.ipynb    # Image classification implementation
│   └── mnist_model.h5                # Trained model (Simple NN)
│
├── CNN_Implementation/
│   ├── CNN.ipynb                     # Convolutional Neural Network implementation
│   ├── mnist_cnn_model.h5            # Trained CNN model
│   └── Session_Notes_lyst1761380366935.pdf  # Session notes and documentation
│
├── task.py                           # Standalone script for custom digit prediction
├── mode_visulaziton.md              # Neural network visualization resources
└── README.md                         # This file
```

## ✨ Features

- **Multiple Model Architectures**: Implementation of both simple Neural Networks and CNNs
- **MNIST Dataset Integration**: Automatic loading and preprocessing of the MNIST dataset
- **Model Persistence**: Trained models saved in HDF5 format for reuse
- **Custom Image Testing**: Create and test custom images with trained models
- **Visualization**: Display predictions with confidence scores
- **Error Handling**: Robust error handling for model loading and prediction


## 🚀 Usage

### Running Jupyter Notebooks

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Navigate to desired notebook**
   - For image classification: `Image_Classification/Image_Classification.ipynb`
   - For CNN implementation: `CNN_Implementation/CNN.ipynb`

3. **Run cells sequentially** to train models and see results

### Using the Custom Digit Recognition Script

1. **Ensure the model exists**
   - Make sure `mnist_model.h5` is in the same directory as `task.py`

2. **Run the script**
   ```bash
   python task.py
   ```

3. **View the results**
   - The script will display a custom-drawn digit '1'
   - Show the model's prediction
   - Display confidence scores for all digits (0-9)

## 📊 Projects

### Image Classification

**Location**: `Image_Classification/`

A basic neural network implementation for classifying MNIST handwritten digits.

**Key Features:**
- Simple feedforward neural network
- Flattened input layer (784 neurons)
- Dense hidden layers with activation functions
- Softmax output layer for 10-digit classification
- Model saved as `mnist_model.h5`

**Notebook**: `Image_Classification.ipynb`

### CNN Implementation

**Location**: `CNN_Implementation/`

Advanced implementation using Convolutional Neural Networks for improved accuracy.

**Key Features:**
- Convolutional layers for feature extraction
- MaxPooling layers for dimensionality reduction
- Dropout layers for preventing overfitting
- Dense layers for classification
- Higher accuracy compared to simple neural networks
- Model saved as `mnist_cnn_model.h5`

**Notebook**: `CNN.ipynb`

### Custom Digit Recognition

**Location**: `task.py`

A standalone Python script demonstrating how to use trained models for custom image prediction.

**Features:**
- Creates custom 28x28 pixel images programmatically
- Draws a digit '1' using NumPy arrays
- Loads pre-trained model (`mnist_model.h5`)
- Performs prediction and displays results
- Shows confidence scores for all digit classes

**Example Output:**
```
Model loaded successfully from mnist_model.h5
✅ Success! The model correctly identified the custom image.

Confidence Scores (Probabilities for each digit 0-9):
[[probability_array]]
```

## 🏗️ Model Architecture

### Simple Neural Network (Image Classification)
```
Input Layer (784 neurons) → Dense Layer → Dense Layer → Output Layer (10 neurons)
```

### Convolutional Neural Network (CNN)
```
Input (28×28×1) → Conv2D → MaxPooling → Conv2D → MaxPooling → Flatten → Dense → Dropout → Output (10 neurons)
```

## 🎨 Visualization Resources

The project includes links to excellent neural network visualization tools in `mode_visulaziton.md`:

### Interactive Visualizations:
- **3D MLP Visualization**: [https://adamharley.com/nn_vis/mlp/3d.html](https://adamharley.com/nn_vis/mlp/3d.html)
- **3D CNN Visualization**: [https://adamharley.com/nn_vis/cnn/3d.html](https://adamharley.com/nn_vis/cnn/3d.html)
- **2D MLP Visualization**: [https://adamharley.com/nn_vis/mlp/2d.html](https://adamharley.com/nn_vis/mlp/2d.html)
- **2D CNN Visualization**: [https://adamharley.com/nn_vis/cnn/2d.html](https://adamharley.com/nn_vis/cnn/2d.html)

### Additional Resources:
- **GitHub Repository**: [https://github.com/aharley/nn_vis](https://github.com/aharley/nn_vis)
- **MNIST Interactive**: [https://www.ccom.ucsd.edu/~cdeotte/programs/MNIST.html](https://www.ccom.ucsd.edu/~cdeotte/programs/MNIST.html)

## 📦 Requirements

All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

### Key Dependencies:
- **TensorFlow 2.20.0**: Deep learning framework
- **Keras 3.12.0**: High-level neural networks API
- **NumPy 2.3.5**: Numerical computing library
- **Matplotlib 3.10.8**: Visualization library
- **Pandas 2.3.3**: Data manipulation and analysis
- **Jupyter**: Interactive notebook environment

For the complete list of all dependencies with exact versions, see [`requirements.txt`](requirements.txt).

## 📈 Results

### Expected Performance:

- **Simple Neural Network**: ~97-98% accuracy on test set
- **CNN Model**: ~98-99% accuracy on test set

### Custom Image Testing:

The `task.py` script successfully:
- Loads pre-trained models
- Processes custom-drawn images
- Predicts digit labels with confidence scores
- Visually displays results using matplotlib

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🎓 Learning Objectives

This repository demonstrates:

✅ **Data Preprocessing**: Loading and normalizing MNIST dataset  
✅ **Model Building**: Creating neural networks using Keras  
✅ **Training & Evaluation**: Fitting models and assessing performance  
✅ **Model Persistence**: Saving and loading trained models  
✅ **Inference**: Using models for predictions on new data  
✅ **Visualization**: Displaying results and understanding model behavior  

## 📚 Further Reading

- [TensorFlow Documentation](https://www.tensorflow.org/tutorials)
- [Keras Documentation](https://keras.io/)
- [MNIST Database](http://yann.lecun.com/exdb/mnist/)
- [Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/)

