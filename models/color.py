from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

inputs = [""]
labels = [""]


# Train the model only if it's not already trained and saved
def get_model(inputs="", labels=""):
    try:
        # Load the trained model from disk
        pipeline = joblib.load("color_classifier_model.pkl")
    except FileNotFoundError:
        # Create a pipeline with CountVectorizer and DecisionTreeClassifier
        pipeline = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', DecisionTreeClassifier())
        ])

        # Train the model
        pipeline.fit(inputs, labels)

        # Save the trained model to disk
        joblib.dump(pipeline, "color_classifier_model.pkl")
    return pipeline


# Function to predict color
def predict_color(pipeline, input_text):
    predicted_label = pipeline.predict([input_text])
    return predicted_label[0]


# # Test the model with some examples
# test_inputs = ["sky", "rose", "violet", "gold coin", "silverware"]
# for input_text in test_inputs:
#     predicted_color = predict_color(input_text)
#     print(f"The color of '{input_text}' is predicted as '{predicted_color}'")

X_train, X_test, y_train, y_test = train_test_split(inputs, labels, test_size=0.2, random_state=42)

# Train the model on the training set
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', DecisionTreeClassifier())
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict labels for the testing set
predicted_labels = pipeline.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy:", accuracy)