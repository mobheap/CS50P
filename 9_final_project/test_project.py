import pandas as pd
from sklearn.linear_model import LinearRegression
from project import preprocess_data, train_model, predict


def main():
    test_predict()
    test_preprocess_data()
    test_train_model()


def test_preprocess_data():
    data = pd.DataFrame({
        'size': [1500, 1600, 1700],
        'location': ['A', 'B', 'A'],
        'bedrooms': [3, 4, 3],
        'price': [300000, 400000, 350000]
    })
    X, y = preprocess_data(data)
    assert X.shape == (3, 4)
    assert y.shape == (3,)

def test_train_model():
    X_train = [[1500, 3, 1, 0], [1600, 4, 0, 1], [1700, 3, 1, 0]]
    y_train = [300000, 400000, 350000]
    model = train_model(X_train, y_train)
    assert isinstance(model, LinearRegression)
    assert model.coef_ is not None

def test_predict():
    model = LinearRegression()
    model.coef_ = [1000, 50000, 20000, -20000]
    model.intercept_ = 10000
    X_test = [[1600, 4, 0, 1]]
    predictions = predict(model, X_test)
    assert len(predictions) == 1
    assert abs(predictions[0] - 400000) < 1e-6


if __name__ == '__main__':
    main()