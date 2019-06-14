import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import *
import sys
from AngryTops.features import *
from AngryTops.ModelTraining.custom_loss import *

n_features_input = 6
n_target_features = 6

def base_model(**kwargs):
    """
    The base model. Consists of a since LSTM layer of 30 nodes sandwiched
    between two dense layers
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    learn_rate = kwargs["learn_rate"]
    lstm_size = 30
    if 'lstm_size' in kwargs.keys():
        lstm_size = int(kwargs['lstm_size'])
    model = keras.Sequential()
    model.add(Dense(36, activation='relu', input_shape=(36,)))
    model.add(Reshape(target_shape=(6,6)))
    model.add(LSTM(lstm_size, return_sequences=True))
    model.add(Flatten())
    model.add(Dense(24))
    model.add(Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def batchnorm_model(**kwargs):
    """
    The base model. Consists of a since LSTM layer of 30 nodes sandwiched
    between two dense layers
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    learn_rate = kwargs["learn_rate"]
    lstm_size = 30
    if 'lstm_size' in kwargs.keys():
        lstm_size = int(kwargs['lstm_size'])
    model = keras.Sequential()
    model.add(Dense(36, activation='relu', input_shape=(36,)))
    model.add(BatchNormalization())
    model.add(Reshape(target_shape=(6,6)))
    model.add(LSTM(lstm_size, return_sequences=True))
    model.add(Flatten())
    model.add(Dense(24))
    model.add(Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def double_lstm(**kwargs):
    """
    Create a RNN w/ 3 regularized LSTM layers, sandwiched between Batch
    Normalizations and Dense Layers
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    learn_rate = kwargs["learn_rate"]
    lstm0, lstm1 = 50, 50
    if 'lstm0' in kwargs.keys(): lstm0 = int(kwargs['lstm0'])
    if 'lstm1' in kwargs.keys(): lstm1 = int(kwargs['lstm1'])
    reg_weight = kwargs['reg_weight']
    rec_weight = kwargs['rec_weight']
    bias_weight = kwargs["bias_weight"]
    model = keras.Sequential()
    model.add(Dense(36, activation='relu', input_shape=(36,)))
    model.add(BatchNormalization())
    model.add(Reshape(target_shape=(6,6)))
    model.add(LSTM(lstm0, return_sequences=True, kernel_regularizer=l2(reg_weight),
                    recurrent_regularizer=l2(rec_weight), bias_regularizer=l2(bias_weight)))
    model.add(LSTM(lstm1, return_sequences=True, kernel_regularizer=l2(reg_weight),
                    recurrent_regularizer=l2(rec_weight), bias_regularizer=l2(bias_weight)))
    model.add(Flatten())
    model.add(Dense(24))
    model.add(Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def triple_lstm(**kwargs):
    """
    Create a RNN w/ 3 regularized LSTM layers, sandwiched between Batch
    Normalizations and Dense Layers
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    learn_rate = kwargs["learn_rate"]
    lstm0, lstm1, lstm2 = 50, 50, 50
    if 'lstm0' in kwargs.keys(): lstm0 = int(kwargs['lstm0'])
    if 'lstm1' in kwargs.keys(): lstm1 = int(kwargs['lstm1'])
    if 'lstm2' in kwargs.keys(): lstm0 = int(kwargs['lstm2'])
    reg_weight = kwargs['reg_weight']
    rec_weight = kwargs['rec_weight']
    bias_weight = kwargs["bias_weight"]
    model = keras.Sequential()
    model.add(Dense(36, activation='relu', input_shape=(36,)))
    model.add(BatchNormalization())
    model.add(Reshape(target_shape=(6,6)))
    model.add(LSTM(lstm0, return_sequences=True, kernel_regularizer=l2(reg_weight),
                    recurrent_regularizer=l2(rec_weight), bias_regularizer=l2(bias_weight)))
    model.add(LSTM(lstm1, return_sequences=True, kernel_regularizer=l2(reg_weight),
                    recurrent_regularizer=l2(rec_weight), bias_regularizer=l2(bias_weight)))
    model.add(LSTM(lstm2, return_sequences=True, kernel_regularizer=l2(reg_weight),
                    recurrent_regularizer=l2(rec_weight), bias_regularizer=l2(bias_weight)))
    model.add(Flatten())
    model.add(Dense(24))
    model.add(Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model_multi(**kwargs):
    """Seperate the inputs for jets and leps. Idea: Apply an LSTM layer to
    correctly identify the order of the jets. Then combine with lept + met
    information to obtain the final state objects. Uses only a single LSTM layer
    in the beginning for jets."""
    learn_rate = kwargs["learn_rate"]
    lstm_size = kwargs['lstm_size']
    dense_size = kwargs['dense_size']
    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")

    # Jets
    x_jets = Reshape(target_shape=(5,4))(input_jets)
    x_jets = LSTM(lstm_size, return_sequences=True)(x_jets)
    x_jets = Reshape(target_shape=(5*lstm_size,))(x_jets)
    x_jets = Dense(dense_size, activation='linear')(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = keras.Model(inputs=input_lep, outputs=input_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(18, activation='relu')(combined)
    final = Reshape(target_shape=(6,3))(final)
    final = Dense(3, activation="linear")(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

################################################################################
# List of all models
models = {'base_model':base_model, 'batchnorm_model':batchnorm_model,
          'double_lstm':double_lstm, 'triple_lstm':triple_lstm,
          'model_multi':model_multi}
################################################################################

if __name__ == "__main__":
    print("Compiled")