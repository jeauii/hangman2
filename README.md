# hangman2
Hangman AI with TensorFlow in Python

## Version
Python 3.9, NumPy 1.24, TensorFlow 2.11

## Method
For any given word, we generate 2^n-1 data points where n is the number of distinct letters in the word. For each non-empty subset of the letters, we mask them in the original word as the input and use them as the target output. For example, the word 'apple' produces 15 data points in total: ```(.pple, {a}), (a..le, {pp}), (app.e, {l}), (appl., {e}), (...le, {app}), (.pp.e, {al}), (.ppl., {ae}), (a...e, {ppl}), (a..l., {ppe}), (app.., {le}), (....e, {appl}) (...l., {appe}), (.pp.., {ale}), (a...., {pple}), (....., {apple})```.

The input is of a fixed length where the letter in each position is represented by one-hot encoding (a blank ```.``` is treated like a special letter). The output is a 26-dimensional vector which can be interpreted as the projected portion of the blanks being each of the letter. The player makes its prediction based on the letter with the highest number that has not been guessed before. 

The model has an input (flatten) layer, a hidden dense layer, and an output layer. Since this is a classification problem, categorical cross-entropy is chosen as the loss function.

## Workflow
```bash
# Prepare the vocabulary as a txt file containing one word per line
touch vocab/words_freq.txt

# Produce a training sample from the vocabulary
# [rate]: rate of the population (default 1) randomly selected for sampling
python process.py [rate] <vocab/words_freq.txt >data/sample.txt

# Generate the training data from the sample selected
python generate.py data/sample.npz <data/sample.txt

# Train a model using the training data
# [epochs]: number of epochs for the training
python train.py models/model data/sample.npz [epochs]

# Test the fitted model
python hangman.py models/model vocab/words_freq.txt
# Type a word for the computer to guess or an empty line to select a random word from the vocabulary
```
