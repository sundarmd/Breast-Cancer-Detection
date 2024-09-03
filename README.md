# Breast-Cancer-Detection

## Overview
This project demonstrates the practical application of a logistic regression model on a real-world dataset to predict whether a tumor is benign (not breast cancer) or malignant (breast cancer) based on its characteristics. The dataset used is the well-known Breast Cancer Wisconsin (Diagnostic) dataset.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Dataset
The Breast Cancer Wisconsin (Diagnostic) dataset is available from the UCI Machine Learning Repository. It includes 569 instances of tumors, each with 30 features that describe the characteristics of the cell nuclei present in the image.

- **Features**: Mean, standard error, and worst (largest) values for 10 real-valued features computed for each cell nucleus:
  - Radius
  - Texture
  - Perimeter
  - Area
  - Smoothness
  - Compactness
  - Concavity
  - Concave points
  - Symmetry
  - Fractal dimension

- **Target**: 
  - 0: Malignant
  - 1: Benign

## Installation
To run this project, you need to have Python 3.x installed. Follow the steps below to set up the environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/sundarmd/Breast-Cancer-Detection.git
    cd Breast-Cancer-Detection
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To train and evaluate the logistic regression model, run the following command:
```
python main.py
```

## Model
The logistic regression model is implemented using the `scikit-learn` library. The steps involved in the model training and evaluation are:

1. **Data Preprocessing**:
    - Load the dataset
    - Handle missing values (if any)
    - Normalize the feature values

2. **Model Training**:
    - Split the dataset into training and testing sets
    - Train the logistic regression model on the training set

3. **Model Evaluation**:
    - Evaluate the model on the testing set using metrics such as accuracy, precision, recall, and F1-score

## Results
The model achieves the following performance metrics on the test set:
- **Accuracy**: 95%
- **Precision**: 94%
- **Recall**: 96%
- **F1-Score**: 95%

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- The UCI Machine Learning Repository for providing the dataset
- The `scikit-learn` library for the machine learning tools
- All contributors to this project
