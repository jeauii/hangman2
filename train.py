import sys
import numpy as np
import tensorflow as tf

from generate import WORD_LEN

def main():
    data = np.load(sys.argv[2])
    x = data['x']
    y = data['y']

    try:
        model = tf.keras.models.load_model(sys.argv[1])
    except:
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(WORD_LEN, 27)),
            tf.keras.layers.Dense(128, activation='relu'),
            #tf.keras.layers.Dense(26, activation='sigmoid')
            tf.keras.layers.Dense(26, activation='softmax')
        ])

    #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    model.fit(x, y, batch_size=256, epochs=int(sys.argv[3]))

    model.save(sys.argv[1])

if __name__ == '__main__':
    main()
