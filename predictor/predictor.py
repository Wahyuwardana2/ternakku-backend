import numpy as np

kamus = {0: "Cocciodiosis", 1: "Healthy Chickens", 2: "Healthy Cows", 3: "Lumpy Cows", 4: "Salmonella"}

def predict_image(model, image):
    X_test = np.expand_dims(image, axis=0)

    # predict
    y_pred = model.predict(X_test)
    predicted_class_index = np.argmax(y_pred)
    predicted_class = kamus[predicted_class_index]

    return predicted_class
