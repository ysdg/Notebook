# Week 1

## Welcome and Introduction

### Machine Learning

The field of study that gives computes the ability to learn without being explicitly programmed.
A computer program is saed to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

### Supervised learning

We are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
**Regression problem**: predict results within a coutinuous output.
**Classification problem**: predict results in a discrete output.

### Unsupervised learning

Allows us to approach problems with little or no idea what our results should look like.
Clustering, Non-clustering



## Model and Cost Function

### Model reprresentation

![image-20210628142225178](1th%20week.assets/image-20210628142225178-1624890066332.png)

### Cost function

Squared error function or mean squared error
$$
J(\theta_0, \theta_1)=\frac{1}{2m} \sum_{i=i}^{m}(\hat{y}_i - y_i)=\frac{1}{2m} \sum_{i=i}^{m} (h_\theta(x_i) - y_i)
$$


## Parameter Learning

### Gradient descent

![img](1th%20week.assets/bn9SyaDIEeav5QpTGIv-Pg_0d06dca3d225f3de8b5a4a7e92254153_Screenshot-2016-11-01-23.48.26-1624890053009.png)

repeat until convergence
$$
\theta_j:=\theta_j-\alpha\frac{\partial}{\partial\theta_j}J(\theta_0, \theta_1)
$$
**Batch gradient decent**: each step of gradient descent uses all the training example



## Linear Algebra Review

1. Matrices and Vectors
2. Addition and Scalar Multiplication
3. Matrix-Vector Multiplication
4. Matrix-Matrix Multiplication
5. Matrix Multiplication Properties
6. Inverse and Transpose
