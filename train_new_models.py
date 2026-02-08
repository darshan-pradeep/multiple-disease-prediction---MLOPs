import pickle
import os
import ssl
from ucimlrepo import fetch_ucirepo
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Bypass SSL verification for UCI fetch
ssl._create_default_https_context = ssl._create_unverified_context

# Define paths
working_dir = os.path.dirname(os.path.abspath(__file__))
saved_models_dir = os.path.join(working_dir, 'saved_models')

if not os.path.exists(saved_models_dir):
    os.makedirs(saved_models_dir)

def train_breast_cancer_model():
    print("Training Breast Cancer model...")
    from sklearn.datasets import load_breast_cancer
    import pandas as pd
    
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    model_path = os.path.join(saved_models_dir, 'breast_cancer_model.sav')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Breast Cancer model saved to {model_path}")

def train_maternal_health_model():
    print("Training Maternal Health model...")
    import pandas as pd
    
    # Try fetching via URL directly if ucimlrepo fails
    try:
        url = "https://archive.ics.uci.edu/static/public/863/data.csv"
        df = pd.read_csv(url)
        X = df.drop('RiskLevel', axis=1)
        y = df['RiskLevel']
    except Exception as e:
        print(f"Failed to fetch via URL: {e}")
        # fallback to ucimlrepo if URL fails (though it failed before)
        maternal_health_risk = fetch_ucirepo(id=863)
        X = maternal_health_risk.data.features
        y = maternal_health_risk.data.targets
    
    # ravel y if it's a dataframe
    if hasattr(y, 'values'):
        y_raveled = y.values.ravel()
    else:
        y_raveled = y
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y_raveled, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    model_path = os.path.join(saved_models_dir, 'maternal_health_model.sav')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Maternal Health model saved to {model_path}")

if __name__ == "__main__":
    train_breast_cancer_model()
    train_maternal_health_model()
