import numpy as np
from PIL import Image
import os, glob, random
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.preprocessing.image import ImageDataGenerator
import sys
from keras.callbacks import TerminateOnNaN
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.callbacks import CSVLogger
from keras.callbacks import TensorBoard
from keras.utils.np_utils import to_categorical
from keras.layers.convolutional import *
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
from keras.layers.pooling import GlobalAveragePooling2D


def create_image_dataset(num_photo):
    x_data = []
    y_data = []

    for p in paths:
        files = glob.glob(p + "*.jpg")

        i = 0
        for f in files:
            if i >= num_photo:
                break
            if f in used_file:
                continue
            used_file[f] = True
            i += 1

            img = Image.open(f)
            img = img.convert("RGB")
            img = img.resize((photo_size, photo_size))
            img = np.asarray(img)
            img = np.reshape(img, (75, 75, 3))

            x_data.append(img)
            y_data.append(int(paths.index(p)))

    x_data = np.array(x_data, dtype=np.float32)
    # y_data = to_categorical(y_data, num_class)
    y_data = np.array(y_data, dtype=np.float32)

    return x_data, y_data


def train():
    # Create image dataset
    x_train, y_train = create_image_dataset(num_train_photo)
    x_test, y_test = create_image_dataset(num_test_photo)

    x_train = np.reshape(x_train, (-1, 75, 75, 3))
    x_test = np.reshape(x_test, (-1, 75, 75, 3))

    y_train = to_categorical(y_train, num_class)
    y_test = to_categorical(y_test, num_class)

    # To stop training when loss is NaN
    terminator = TerminateOnNaN()

    # To save best model only
    check_pointer = ModelCheckpoint(
        filepath='/opt/project/photoz/model.h5',
        save_best_only=True,
        verbose=1,
        monitor='val_acc',
        save_weights_only=False,
        mode='auto',
        period=1, )

    # To stop training early
    early_stop = EarlyStopping(
        monitor='val_acc',
        min_delta=0.0001,
        patience=50,
        verbose=1,
        mode='auto')

    # To export results to a csv log file
    csv_logger = CSVLogger('/opt/project/photoz/csv_logger.log')

    model_ = Sequential([BatchNormalization(input_shape=(75, 75, 3), name='batch_1'),
                         Conv2D(32, (3, 3), kernel_initializer='glorot_normal',
                                activation='relu', name='conv_1'),
                         BatchNormalization(name='batch_2'),
                         Conv2D(32, (3, 3), kernel_initializer='glorot_normal',
                                activation='relu', name='conv_2'),
                         MaxPooling2D((2, 2), name='max_pool_1'),
                         BatchNormalization(name='batch_3'),
                         Conv2D(64, (3, 3), kernel_initializer='glorot_normal',
                                activation='relu', name='conv_3'),
                         BatchNormalization(name='batch_4'),
                         Conv2D(64, (3, 3), kernel_initializer='glorot_normal',
                                activation='relu', name='conv_4'),
                         BatchNormalization(name='batch_5'),
                         MaxPooling2D((2, 2), name='max_pool_2'),
                         Conv2D(num_class, (3, 3), padding='same', name='conv_5'),
                         GlobalAveragePooling2D(),
                         Activation('softmax')])

    model_.compile(
        loss='sparse_categorical_crossentropy',
        optimizer='sgd',
        metrics=['accuracy'])

    model_.fit(x_train, y_train,
               batch_size=5,
               epochs=80,
               verbose=2,
               validation_data=(x_test, y_test),
               shuffle=False,
               callbacks=[terminator, check_pointer,
                          early_stop, csv_logger])

    scores_ = model_.evaluate(x_test, y_test)

    return model_, scores_


def make_prediction(model_, fname):
    img = Image.open(fname)
    img = img.convert('RGB')
    img = img.resize((photo_size, photo_size))
    data = np.asarray(img).reshape(75, 75, 3)
    res = model_.predict([data])[0]
    y_ = res.argmax()
    percent_ = int(res[y_] * 100)
    print("{0} ({1} %)".format(labels[y_], percent_))


if __name__ == "__main__":
    num_train_photo = 75
    num_test_photo = 25
    photo_size = 75
    used_file = {}
    data_size = photo_size * photo_size * 3
    labels = ["cat", "dog"]
    paths = ["/opt/project/photoz/cat/", "/opt/project/photoz/dog/"]
    num_class = len(paths)

    # if len(sys.argv) <= 1:
    #     print('Please input filename of photo needed for prediction')
    #     quit()

    # Train and evaluate model
    model, scores = train()
    print('loss=', scores[0])
    print('accuracy=', scores[1])

    # Prediction
    # make_prediction(model, sys.argv[1])
    make_prediction(model, "/opt/project/photoz/dog/001.jpg")
