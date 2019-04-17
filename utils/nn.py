from sklearn.neural_network import MLPRegressor

def create_mlp_nn(hidden_layer_sizes=(100,), verbose=True):
    ''' Return a multi-layer neural network
        with a pre-defined number of hidden layers and
        number of perceptrons in each hidden layers.

        Argurments:
        -----------
        hidden_layer_sizes (tuple): structure of hidden
        layers used in the neural network. Default is 
        1 layers with 100 nodes.

        Returns:
        --------
        A MLPRegressor instance
    '''
    return MLPRegressor(solver='adam', 
                        alpha=.0001, 
                        hidden_layer_sizes=hidden_layer_sizes, 
                        max_iter=1000, 
                        early_stopping=True,
                        shuffle=True, 
                        verbose=verbose,
                        warm_start=False,
                        tol=0.00001,
                        random_state=13)