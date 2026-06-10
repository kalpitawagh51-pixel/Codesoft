import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Iris.csv")

# Remove Id column
if "Id" in df.columns:
    df = df.drop("Id", axis=1)

# Convert species into numbers
le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])

# Features
X = df.drop("species", axis=1)

# Target
y = df["species"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")

# Graph
sns.countplot(x="species", data=df)
plt.title("Iris Species Count")
plt.show()
Index(['Id',
       'SepalLengthCm',
       'SepalWidthCm',
       'PetalLengthCm',
       'PetalWidthCm',
       'species'])

