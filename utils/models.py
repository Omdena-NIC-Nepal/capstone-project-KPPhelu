import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, model_type):
    """
    train the model based on the the model type
    Model type can be one of: ["Regression", "Multi-Class Classifier", "Binary Classifier"]
    """
    scaler = None
    if model_type == "Regression":
        model = LinearRegression()
        # Scaling for regression
        scaler = StandardScaler()
        
    elif model_type == "Multi-Class Classifier":
        model = RandomForestClassifier()
        # No Scaling for RandomForestClassifier. No need scaling for tree-based models
    elif model_type == "Binary Classifier":
        model = RandomForestClassifier()
        # No Scaling for RandomForestClassifier. No need scaling for tree-based models
    else:
        raise ValueError('"model_type" must be one of ["Regression", "Multi-Class Classifier", "Binary Classifier"]')

    if scaler:
        # fit the scaler to the train set, it will learn the parameters
        scaler.fit(X_train)
        # Transform train and test set
        X_train_scaled = scaler.transform(X_train)
        model.fit(X_train_scaled, y_train)
    else:
        model.fit(X_train, y_train)
    return model, scaler

def predict_model(X_test, model, scaler=None):
    """
    Predict using the trained model. Apply scaling if needed.
    """
    if scaler:
        # Scale the test data using the same scaler fitted on training data
        X_test_scaled = scaler.transform(X_test)
        return model.predict(X_test_scaled)
    else:
        return model.predict(X_test)
    
def evaluate_model(model, scaler, X_train, y_train, X_test, y_test, model_type):
    """
    Evaluate the model based on its type.
    Model type can be one of: ["Regression", "Multi-Class Classifier", "Binary Classifier"]
    Evaluate the model and return the metrics
    """
    # Get predictions for both train and test sets
    y_pred_train = predict_model(X_train, model, scaler)
    y_pred_test = predict_model(X_test, model, scaler)

    if model_type == "Regression":
        # Calculate the metrics for Linear Regression
        metrics = {
            'train_rmse' : np.sqrt(mean_squared_error(y_train, y_pred_train)),
            'test_rmse' : np.sqrt(mean_squared_error(y_test, y_pred_test)),
            'train_r2' : r2_score(y_train, y_pred_train),
            'test_r2' : r2_score(y_test, y_pred_test),
            'y_test' : y_test,
            'y_pred_test': y_pred_test
        }
        
    elif model_type in ["Multi-Class Classifier", "Binary Classifier"]:
        # Calculate the metrics for Classification
        metrics = {
            'train_accuracy': accuracy_score(y_train, y_pred_train),
            'test_accuracy': accuracy_score(y_test, y_pred_test),
            'train_confusion_matrix': confusion_matrix(y_train, y_pred_train),
            'test_confusion_matrix': confusion_matrix(y_test, y_pred_test),
            'train_classification_report': classification_report(y_train, y_pred_train),
            'test_classification_report': classification_report(y_test, y_pred_test)
        }
    else:
        raise ValueError('"model_type" must be one of ["Regression", "Multi-Class Classifier", "Binary Classifier"]')

    return metrics
