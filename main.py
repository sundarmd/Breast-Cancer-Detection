{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Logistic Regression",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q8X8xDwS6vgS",
        "colab_type": "text"
      },
      "source": [
        "# Logistic Regression"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PEGG4I6n60cM",
        "colab_type": "text"
      },
      "source": [
        "## Importing the libraries"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "D4b029YC7C-y",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Aa536pRY7Eq5",
        "colab_type": "text"
      },
      "source": [
        "## Importing the dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4POXlqg47Ny3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "dataset = pd.read_csv('breast_cancer.csv')\n",
        "X = dataset.iloc[:, 1:-1].values\n",
        "y = dataset.iloc[:, -1].values"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0AnzJQCj7TLO",
        "colab_type": "text"
      },
      "source": [
        "## Splitting the dataset into the Training set and Test set"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WOQwyng57dp2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pS1Q-n_A7iZ_",
        "colab_type": "text"
      },
      "source": [
        "## Training the Logistic Regression model on the Training set"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9V-LgiUa78lX",
        "colab_type": "code",
        "outputId": "ce5e5660-1b7c-4750-dc12-837be0ea2fc5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        }
      },
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "classifier = LogisticRegression(random_state = 0)\n",
        "classifier.fit(X_train, y_train)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
              "                   multi_class='auto', n_jobs=None, penalty='l2',\n",
              "                   random_state=0, solver='lbfgs', tol=0.0001, verbose=0,\n",
              "                   warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4cgD7EnB8Dnd",
        "colab_type": "text"
      },
      "source": [
        "## Predicting the Test set results"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1B4zQvOq8M7H",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "y_pred = classifier.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "26CHkZbs8Tu5",
        "colab_type": "text"
      },
      "source": [
        "## Making the Confusion Matrix"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5BN8qx6e8aNZ",
        "colab_type": "code",
        "outputId": "b7b0ba3d-3183-426c-f45a-72d5d8ddb075",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "source": [
        "from sklearn.metrics import confusion_matrix\n",
        "cm = confusion_matrix(y_test, y_pred)\n",
        "print(cm)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[84  3]\n",
            " [ 3 47]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kMErnLnu8hmb",
        "colab_type": "text"
      },
      "source": [
        "## Computing the accuracy with k-Fold Cross Validation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "waJZi8fw8m_2",
        "colab_type": "code",
        "outputId": "985787e6-54db-42ca-edde-950ade8d1ac6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "source": [
        "from sklearn.model_selection import cross_val_score\n",
        "accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)\n",
        "print(\"Accuracy: {:.2f} %\".format(accuracies.mean()*100))\n",
        "print(\"Standard Deviation: {:.2f} %\".format(accuracies.std()*100))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Accuracy: 96.70 %\n",
            "Standard Deviation: 1.97 %\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
