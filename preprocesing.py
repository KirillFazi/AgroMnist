from keras.datasets import mnist
from keras.utils import np_utils


def data_preprocessing():
    num_train = 60000
    num_test = 10000

    height, width, depth = 28, 28, 1
    num_classes = 10

    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    X_train = (X_train
               .reshape(num_train, height * width)
               .astype('float32')
               ) / 255

    X_test = (X_test
              .reshape(num_test, height * width)
              .astype('float32')
              ) / 255

    Y_train = np_utils.to_categorical(y_train, num_classes)
    Y_test = np_utils.to_categorical(y_test, num_classes)

    with open('data/preprocessed/mnist_train.csv', 'w') as f:
        for i in range(num_train):
            f.write(','.join([str(x) for x in X_train[i]]))
            f.write('\n')

    with open('data/preprocessed/mnist_test.csv', 'w') as f:
        for i in range(num_test):
            f.write(','.join([str(x) for x in X_test[i]]))
            f.write('\n')

    with open('data/preprocessed/mnist_train_label.csv', 'w') as f:
        for i in range(num_train):
            f.write(','.join([str(x) for x in Y_train[i]]))
            f.write('\n')

    with open('data/preprocessed/mnist_test_label.csv', 'w') as f:
        for i in range(num_test):
            f.write(','.join([str(x) for x in Y_test[i]]))
            f.write('\n')
