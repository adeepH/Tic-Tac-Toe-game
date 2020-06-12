# Deep Tic Tac Toe
Here is the implementation of a classic example of a Markov Decision Process, a Tic Tac Toe game. Here we have employed two different approaches,namely:
- Deep Neural Network
- Deep Q-learning

# Game
`game.py` has the source code for the game of tic-tac-toe in python.

## Installation

    $ git clone https://github.com/adeepH/Tic-Tac-Toe-game
    $ cd Tic-Tac-Toe-game/
    $ pip3 install -r requirements.txt

This project requires the following libraries to be installed.Please check these out if you don't have one of these (else follow the previous installation process):
- [NumPy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [tabulate](https://pypi.org/project/tabulate/)

# Abstract
 - `tictactoe.py` 
  uses a Deep Neural Network in order to predict the best move possible.Here we run a simulation of around 10000 games and learn from the outcomes of the generated games. The model then predicts the best move based on the simulation of the 10000 previous games it had seen, i.e,  from the data.The model thus learns from the data and delivers a validation accuracy of around 64% on 100 epochs.Higher accuracies can be achieved with robust models such as `Deep Q-Learning` and `Reinforcement Learning`.
- `deep_tic_tac_toe.py` uses a Deep Q-learning approach
