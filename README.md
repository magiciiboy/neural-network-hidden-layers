# Determining the Number of Hidden Layers

Experiment of Determining the Number of Hidden Layers

I was inspired by the post by Jeff Heaton at https://www.heatonresearch.com/2017/06/01/hidden-layers.html to test what is the best size of hidden layers in a neural network.

I conducted some experiment to extract the insight of performance corresponding with 
variable sizes.

## Dataset ##

To run the experiments, I used a dataset of Bike-Sharing which has been preprocessed:

- Use One-Hot encoding for Categorical data

## Try-and-Error result ##

After trying some random choice of hidden layers. I come up with the best selection of (160, 80, 40).
This structure generates following results:

- R-squared::0.9106457314393288
- Pred R-squared::0.9002130472935612
- MSE::3336.8798909376187

## Experiment with variable number of nodes in each hidden layer ##

I was trying to looking for a simpler version of structure which can generate the same as the acceptable result as above by using some rule-of-thumb methods suggested by Jeff Heaton. I tried to reduce the number of layers.

### Experiment #1: ###

Use: 2 hidden layers, prior layer varies, later one has 2/3 size of input + output

Result:

![alt text](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp1.png?raw=true)

### Experiment #2: ###

Use: 2 hidden layers, prior layer has 2/3 size of input + output, later one varies

Result:

![alt text](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp2.png?raw=true)

On the same scale

![alt text](https://github.com/magiciiboy/neural-network-hidden-layers/blob/master/output/exp2b.png?raw=true)