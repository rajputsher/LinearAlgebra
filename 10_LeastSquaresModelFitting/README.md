# Least-squares for model-fitting in statistics

Model fitting: 

Complex models simplified to simple understandle models

<img src='images/1.png' width=500 height=400>

One of the methods of model fitting is using least squares method.

Steps involved in model fitting: 

<img src='images/2.png' width=500 height=150>

Step-1: 

Let us consider the example of a model to compute height of a person.

Here the wights $\beta_{n}$ indicates which of the following has more influence on height.

<img src='images/3.png' width=500 height=250>

Step-2: Mapping the data into the model equations.

Data

<img src='images/4.png' width=500 height=200>

Model equations


<img src='images/4a.png' width=500 height=200>



Step-3: Matrix represenation

<img src='images/5.png' width=500 height=150>

Step-4:  Compute the parameters

<img src='images/6.png' width=250 height=75>

Step-5: Statistical evaluation of the model

<img src='images/7.png' width=500 height=50>


Statistics terminology

<img src='images/8.png' width=500 height=250>

---

## Linear least squares via left inverse

Finding $\beta$ or free parameters

<img src='images/9.png' width=500 height=250>

Conditions for X to have a left inverse

<img src='images/10.png' width=500 height=250>


<img src='images/11.png' width=500 height=250>

**Is y in the column space of X ?**

<img src='images/12.png' width=500 height=250>

The solution is exact when y belongs to column space of X. 
Otherwise that is the closest to y that is in the column space.

<img src='images/13.png' width=500 height=250>

Here $\epsilon$ is nothing but the projection of y on X

<img src='images/14.png' width=500 height=200>

## Least square via orthogonal projections 

Here in this example lets us consider we get data from a large pharmaceuticals about patient studies, we need to study this data.

<img src='images/15.png' width=500 height=200>


<img src='images/16.png' width=500 height=250>

Projections in $R^2$

<img src='images/17.png' width=500 height=250>

Projections in $R^N$

<img src='images/18.png' width=500 height=250>


using statistical equation this is represented as:

<img src='images/19.png' width=500 height=250>


Now the complete geometrical representation of this can be seen as : 

<img src='images/20.png' width=500 height=250>

---
## Least-squares via row reduced echelon form (RREF)

Computing inverse by RREF 

<img src='images/21.png' width=250 height=100>

Using the augmenting X y will not work because the resulted will not be a Identity matrix but as shown in the figure.

<img src='images/22.png' width=500 height=200>


The solution is : 
LS and normal equations

<img src='images/23.png' width=500 height=200>

now this is how the augmented matix and the result looks like : 

<img src='images/24.png' width=500 height=200>

Why this procedure works ? 

<img src='images/25.png' width=500 height=250>


## Model predicted values and residuals

$\epsilon$ and $y\hat{}$ are orthogonal

<img src='images/26.png' width=500 height=250>

There for $\epsilon=y\hat{} - y$

<img src='images/27.png' width=200 height=75>

Some times $\epsilon$ is also know as residual matrix

We can re-write the above equatio as : $||\epsilon||^2 = ||X\beta - y ||^2$. i.e magnitude of $\epsilon$  is equal to  magnitude of the difference of the predicted data($X\beta$) and the observed data($y$).

The goal of this now is to find $\beta$ (other terms cannot be changed) which minimizes this equation. Hence it is called Least squares equation:

<img src='images/28.png' width=300 height=125>

## Least squares application

Application 1:

### The average of a set of numbers can be formulated as a least squares problem

We know following are the steps involved in model fitting

<img src='images/2.png' width=400 height=150>


Step1: 

<img src='images/29.png' width=100 height=50>

Step2: 

<img src='images/30.png' width=400 height=125>

Step3:

<img src='images/31.png' width=300 height=125>

Step4: 

```python
# design matrix
X = np.concatenate( [np.ones([N,1]),np.array([np.arange(0,N)]).T],axis=1) ## Adding intercept term to the design matrix
# fit the model
b = np.linalg.solve(X.T@X,X.T@data)

# compute the model-predicted values
yHat = X@b

# plot data and model prediction
plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1),yHat,'ro--',label='Model pred.')

plt.legend()
plt.show()
```

Application 2:

### Least squares in real data from a neuroscience experiment

<img src='images/32.png' width=400 height=300>

<img src='images/33.png' width=400 height=300>

in the below experiment the candidate was asked to click the mouse button when a signal was given. Below shows the response data of the candidate for around 100 iterations.

<img src='images/34.png' width=400 height=300>

EEG contains singals. The components of these signals are extracted using fourier transform. 

<img src='images/35.png' width=400 height=300>

In our application we need to find if there is any corelation between the response times to the data extracted from the EEG signals.

Modeling Steps:

Step1: Equation of the underlying model

<img src='images/36.png' width=300 height=200>

Step2: Model equations 

Formalize in head.

Step3 : Convert equations in to a matrix-vector equation 

It is important to look the size of the matrices. In this case not all data points have a previous trail response for the first trail.
Hence the matrix is made 98 rows instead of 99 trails.


<img src='images/37.png' width=300 height=200>

Step4 : Compute the parameters 

code: 3_LSApplication2.py

Input data: 

Responses :

<img src='images/38.png' width=300 height=200>

EEG Data:

<img src='images/39.png' width=300 height=200>

Output : 

Spectrum of beta coefficients  and scatter plots for 2 frequencies 8 and 20 Hz

<img src='images/40.png' width=500 height=400>


---

## Least Square via QR decomposition

<img src='images/41.png' width=250 height=350>

