import tensorflow as tf
from tensorflow.keras import layers, models

def main():
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    
    model = models.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(X_train, y_train, epochs=3)
    
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print("Accuracy:", test_acc)

if __name__ == "__main__":
    main()
