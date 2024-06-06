import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import joblib

def main():
    data = pd.read_csv('house_prices.csv')
    
    # preparing the data
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # creating our model and using it
    model = train_model(X_train, y_train)
    predictions = predict(model, X_test)
    print("Mean Squared Error: ", mean_squared_error(y_test, predictions))
    
    joblib.dump(model, 'house_price_model.pkl')


def preprocess_data(data):
    data = data.dropna()
    X = data.drop('price', axis=1)
    y = data['price']
    
    # encoding categorical data and scaling numerical features
    X = pd.get_dummies(X, drop_first=True)
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y  # X variable has all our features and y is our target variable(the price)


def train_model(X_train, y_train):
    model = LinearRegression()  # the most basic machine learning algorithm: linear regression
    model.fit(X_train, y_train)
    return model


def predict(model, X_test):
    return model.predict(X_test)


if __name__ == "__main__":
    main()