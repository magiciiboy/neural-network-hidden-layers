# Determining the Number of Hidden Layers

Experiment of Determining the Number of Hidden Layers

I was inspired by the post by Jeff Heaton at https://www.heatonresearch.com/2017/06/01/hidden-layers.html to test what is the best size of hidden layers in a neural network.

I conducted some experiment to extract the insight of performance corresponding with 
variable sizes.

## What is recommended? ##

As recommended by Jeff Heaton, there are some rules to determine the number of hidden layers and number of nodes in each layers as follows:

Number of Layers

| Num Hidden Layers	| Result |
|-------------------|--------|
|none | Only capable of representing linear separable functions or decisions. |
| 1	  | Can approximate any function that contains a continuous mapping from one finite space to another. |
| 2   | Can represent an arbitrary decision boundary to arbitrary accuracy with rational activation functions and can approximate any smooth mapping to any accuracy. |
| >2  | Additional layers can learn complex representations (sort of automatic feature engineering) for layer layers. |

Number of nodes in each layer:

- The number of hidden neurons should be between the size of the input layer and the size of the output layer.
- The number of hidden neurons should be 2/3 the size of the input layer, plus the size of the output layer.
- The number of hidden neurons should be less than twice the size of the input layer.

However, some of others suggest to use other calculation such as at https://www.researchgate.net/post/How_to_decide_the_number_of_hidden_layers_and_nodes_in_a_hidden_layer :

- Number of hidden node = (2 * input size) + 1 (by **Irfan Majid**)
- Number of hidden node = (4 * n^2) + 3 / (n^2-8) (by **Gnana Sheela and Deepa**)

## What to test or purpose of this test ? ##

- Whether keeping number of perception in each layers as suggested is as good as increase to a greater number of perceptrons.
- Determine which calcualtion performs better on a semi-complicated dataset.

Detail of experiments is presented in Jupyter note `NeuralNetworkModel`

## Dataset ##

To run the experiments, I used a dataset of Bike-Sharing. This dataset has more than 17.000 observations with 19 extracted features.

This dataset has been preprocessed:

- Use One-Hot encoding for Categorical data

## Try-and-Error result ##

After trying some random choice of hidden layers. I come up with the best selection of (160, 80, 40).
This structure generates following results:

- `R-squared`: 0.9106457314393288
- `R-squared (Pred)`: 0.9002130472935612
- `MSE`: 3336.8798909376187

In fact, for this dataset, the performance peak when using `Random Forest`:

- `R-squared`: 0.9916119677601978
- `R-squared (Pred)`: 0.9403197838814934

## Experiment with variable number of nodes in each hidden layer ##

I was trying to looking for a simpler version of structure which can generate the same as the acceptable result as above by using some rule-of-thumb methods suggested by Jeff Heaton. I tried to reduce the number of layers.

### Experiment #1: ###

Use: 2 hidden layers, prior layer varies in range(output, 2 * input), later one has 2/3 size of input + output

Result:

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp1.png?raw=true)

### Experiment #2: ###

Use: 2 hidden layers, prior layer has 2/3 size of input + output, later one varies in range (output, 2 * input)

Result:

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp2.png?raw=true)

On the same scale

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp2b.png?raw=true)

### Experiment #3: ###

Use: 2 hidden layers, all layers have more number of nodes than recommended

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp3.png?raw=true)


### Experiment #4: ###

Use: 2 hidden layers, all layers have more number of nodes than recommended

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp4.png?raw=true)

### Experiment #5: ###

Use: 2 hidden layers, suggested by **Irfan Majid**

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp5.png?raw=true)


### Experiment #6: ###

Use: 2 hidden layers, suggested by **Gnana Sheela and Deepa**

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp6.png?raw=true)

### Experiment #7: ###

Use: N = 2 * n + 1, however increase number of hidden layers to 3, 4, 5, 6, 7

![Experiment of Determining the Number of Hidden Layers](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp7F.png?raw=true)


## Conclusion ##

- `N = 2 * n + 1` works with 8 hidden layers. It achieves R-squared score at **0.9012** (target is **0.9002**). `MSE` is **3302.2312** (target is **3336.8798**).
- From 8 layers, the performance does not increase.
- Although, the result is acceptable, it still needs more inverstigation to calibrate to pass the result of `Random Forest` (R-squared score **0.9403**).