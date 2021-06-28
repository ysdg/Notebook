# Week 2

## Environment setup instructions

For Octave and Matlab



## Multivariate linear regression

### Multiple Features

The hypothesis function:
$$
h_\theta(x)
=\theta_0 + \theta_1x_1 + \theta_2x_2 + ... + \theta_nx_n
=[\theta_0\quad\theta_1 ... \theta_n]\left[ \begin{matrix}x_0\\x_1\\...\\x_n \end{matrix}\right]
=\theta^Tx
$$
In the function:
- $x^{(i)}_j$=values of feature $j$ in the $i^{th}$ training example
- $x^{(i)}$=the input (features) of the $i^{th}$ training example
- $m$=the number of training examples
- n=the number of features

### Gradient Descent for Multiple Variables

Repeat until convergence:{
$$
\theta_j:=\theta_j-\alpha\frac{1}{m}\sum^m_{i=1}(h_\theta(x^{(i)})-y^{(i)}x_j^{(i)}) \quad for j:=0...n
$$
}

### Gradient Descent in Practice I - Feature Scaling

**Feature scaling and mean normalization**

We can speed up gradient descent by having each of our input values in roughly the same range. This is bacause θ will descend quickly on small ranges and slowly on large ranges, and so will oscillate inefficiently down to the optimum when the variables are very even
$$
x_i:=\frac{x_i-\mu_i}{s_i}
$$
Where $\mu_i$ is the average of all values for feature(i) and $s_i$ is the range of values(max-min), or $s_i$ is the standard deviation.

### Gradient Descent in Practice II - Learning Rate

**Debugging gradient descent**: Make a plot with *number of iterations* on the x-axis. Now plot the cost function, J(θ) over the number of iterations of gradient descent. If $J(\theta)$  ever increases, then you probably need to decrease α.

**Automatic convergence test**: Declare convergence if $J(\theta)$ decreases by less than E in one iteration, where E is some small value such as $10^{−3}$. However in practice it's difficult to choose this threshold value

**To summarize**:

 If $\alpha$ is too small: slow convergence. 

 If $\alpha$ is too large: ￼may not decrease on every iteration and thus may not converge.

### Features and Polynomial Regression

**Polynomial Regression**

**change the behavior or curve** of our hypothesis function by making it a quadratic, cubic or square root function (or any other form). For example:
$$
h_\theta(x)=\theta_0 + \theta_1x_1
$$
to:
$$
h_\theta(x)=\theta_0 + \theta_1x_1 + \theta_2x_1^2
$$
One important thing to keep in mind is, if you choose your features this way then feature scaling becomes very important.



## Computing parameters analytically

### Normal Equation

normal equation formula:
$$
\theta=(X^TX)^{-1}X^Ty
$$
There is **no need** to do feature scaling with the normal equation.

The following is comparison of gradient descent and the normal equation:

| Gradient Descent           | Normal Equation                               |
| -------------------------- | --------------------------------------------- |
| Need to choose alpha       | No need to choose alpha                       |
| Needs many iterations      | No need to iterate                            |
| $O(kn^2)$                  | $O(n^3)$, need to calculate inverse of $X^TX$ |
| Works well when n is large | Slow if n is very large                       |

### Normal Equation Nonimvertibility

If $X^T$ is **noninvertible,** the common causes might be having:

- Redundant features, where two features are very closely related
- Too many features. In this case, delete some feature or use "regularization"

## Submitting programming assignments

### Programming tips from Mentors