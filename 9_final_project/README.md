# Predicting House Prices 
#### Video Demo:  < 'you don't need this' >
#### Description:

This project involves building and evaluating a linear regression model to predict house prices based on various features . The main goal is to create a pipeline that processes the data, trains a model, and makes predictions on new data.

### Project Structure

1. **project.py**: Contains the main function and the custom functions for data preprocessing, model training, and prediction.
    - `main()`: Handles the overall workflow, including loading data, preprocessing, training the model, making predictions, and evaluating the model.
    - `preprocess_data(data)`: Takes a DataFrame and drops missing values, encodes categorical variables, and scales numerical features.
    - `train_model(X_train, y_train)`: Trains a Linear Regression model using the preprocessed training data.
    - `predict(model, X_test)`: Makes predictions on the test data using the trained model.

2. **test_project.py**: Contains test functions for each of the custom functions in `project.py`.
    - `test_preprocess_data()`: Tests the `preprocess_data` function to ensure correct preprocessing of data.
    - `test_train_model()`: Tests the `train_model` function to ensure the model is trained correctly.
    - `test_predict()`: Tests the `predict` function to ensure accurate predictions.

3. **requirements.txt**: Lists the necessary libraries.
    - `pandas`: For data manipulation.
    - `scikit-learn`: For machine learning.
    - `joblib`: For saving the model.

### How to Run the Project

1. **Install the required libraries**:
    ```
    pip install -r requirements.txt
    ```

2. **Run the main script**:
    ```
    python project.py
    ```

3. **Run the tests**:
    ```
    pytest test_project.py
    ```

### Project Workflow

1. **Data Loading**: The main function loads the house price data from a CSV file.
2. **Data Preprocessing**: The data is cleaned and preprocessed using `preprocess_data`.
3. **Model Training**: The preprocessed data is split into training and test sets, and the model is trained using `train_model`.
4. **Prediction**: The trained model makes predictions on the test data using `predict`.
5. **Evaluation**: The model's performance is evaluated using Mean Squared Error (MSE).

### Conclusion

This project demonstrates the entire machine learning workflow from data preprocessing to model training and evaluation. The resulting model can be used to predict house prices based on various input features.
I chose this project because i learned python for machine learning and deep learning to pursue a career in AI.
