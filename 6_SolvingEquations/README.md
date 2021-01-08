# Systems of equations

## Geometric perspective


<img src="images/1.png" width=500 height=250>


Solution of two equations in this case is the point of intersection of the two lines

<img src='images/2.png' width=500 height=250>

In a system of couples equation, when we add or subtract equations the solution will not change.

for example:

(equation 1) - (equation 2) = (new equation 1)

(equation 2) + 2*(equation 1)=  (new equation 2)

Though we have new equation, the solution of the new equations are still the same as seen below.

<img src="images/3.png" width=500 height=250>

## Converting system of equations to matrix equations

<img src="images/4.png" width=500 height=200>

<img src="images/5.png" width=500 height=200>

<img src="images/6.png" width=500 height=200>


## Guassian elimination method of solving equations

Steps in guassian elimination method:

<img src="images/7.png" width=500 height=250>

Example: 

Step1: 

<img src="images/8.png" width=500 height=200>

Step2:

<img src="images/9.png" width=500 height=200>

Step3:

This is also known as Echelon form of a matrix

<img src="images/10.png" width=500 height=200>

<img src="images/11.png" width=500 height=250>

Step4:

<img src="images/12.png" width=500 height=250>

here we have already solved for y. y =19/17

Step5:

<img src="images/13.png" width=500 height=250>

Step6:

<img src="images/14.png" width=500 height=250>

## Other possibilities

### 0 = 0

<img src="images/15.png" width=500 height=200>

We might work through a problem and end up with a form that looks like this after Gaussian elimination where we get an entire row of zeros at the bottom.

This basically means that the last equation completely dropped out and we end up with zero equals zero. Now when this happens it means that one at least one row in the matrix is a multiple of at least one other row.

In other words the system and the matrix that represents that system is reduced rank or rank deficient.


### 0 = 1

<img src="images/16.png" width=500 height=200>

Now this is not a valid mathematical statement at least not in our universe that we are living in; zero does not equal 1 and zero cannot equal anything other than zero.

So the conclusion if we end up with something like this the conclusion is that the system of equations is inconsistent. It does not have a single solution.Now geometrically this would mean that the lines described by these equations never meet at a single point.

There is no one point where all of these lines are touching each other.

---
# Echelon form and pivots

The most noticeable feature of the Echelon form  is that there are zeros below and to the left of the Matrix the leading nonzero terms in the each row are called **pivots**.

In the below image a,f and j are pivots.

<img src="images/17.png" width=400 height=200>


The ones in the below image are not in echelon form and hence they are not pivots. We can ge to echelon form here my moving some rows.

<img src="images/18.png" width=400 height=200>

## Converting to echelon form : example

- Usually it's useful to use the first row as best as possible use the first row to knock out subsequent rows because we want the first row to have its pivot value here in the leftmost position of the first column.

- The second tip is it's generally useful to try to eliminate the bottom row first so apply elimination first to the bottom row and then work your way up so that we get zeros below the first pivot and then we keep working down from the second pivot. The third pivot and so on.

<img src="images/19.png" width=500 height=200>

here we get 2 pivots : 1 and 5. 
As there are 2 pivots, the rank of this matrix is 2.

>  The number of pivots is equal to the rank of that matrix.

---

## Reduced row echelon form(RREF)

RREF is similar to the Echelon form in the sense that the pivots have all zeros below them and to the left of them, but with RREF, **there needs to be all zeros above the pivot's and all the pivots need to have a value of one**.

Examples:

1. This is in the echelon form as it satisfied the conditions mentioned above 

<img src="images/20.png" width=250 height=200>

2. Not in echelon form

<img src="images/21.png" width=500 height=200>


3. Not in echelon form

<img src="images/22.png" width=500 height=200>

## Conversion example
1. 
<img src="images/23.png" width=500 height=350>

2. 
<img src="images/24.png" width=500 height=350>

---
##  Row space after row reduction

Rank and row space doesnot change

<img src="images/25.png" width=500 height=350>

##  Column space after row reduction

After row reduction column space might change not necessarily.

Example where this changes:

<img src="images/26.png" width=350 height=200>


Example where this does not change:

<img src="images/27.png" width=350 height=150>