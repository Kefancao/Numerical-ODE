# Ordinary Differential Equation
This repo is intended for me to introduce a common technique called the Euler's method to solve derivatives. The Euler's method is one that has been taught to most people during high school as the fundamental theorem of calculus. It looks similar to this, 

<img src="https://latex.codecogs.com/svg.image?f(x&plus;h)&space;-&space;f(x)&space;\approx&space;f(x)&space;\cdot&space;h">
Rearranging we have, 
<img src="https://latex.codecogs.com/svg.image?f(x&plus;h)&space;\approx&space;f(x)\cdot&space;h&space;&plus;&space;f(x)">

Turns out, if we're given an initial value, we can apply a similar technique to get the derivative! 
If we're given the initial value problem, 
<img src="https://latex.codecogs.com/svg.image?{dy\over&space;dt}&space;=&space;f(t,&space;y(t))&space;\text{&space;with&space;}y(t_0)&space;=&space;y_0">
We can then pick a set of discrete points and uses them to compute the slope as a form of approximation to the derivative, developing a recursive scheme for determining an **approximated**
$y_n$ values. Applying the formula for the slope, 

<img src="https://latex.codecogs.com/svg.image?{y(t_{n&plus;1})&space;-&space;y(t_n)&space;\over&space;t_{n&plus;1}&space;-&space;t_n}&space;=&space;y'(t_n)&space;=&space;f(t_n,&space;y(t_n))">

Rearranging,
<img src="https://latex.codecogs.com/svg.image?y_{t_{n&plus;1}}&space;=&space;y(t_n)&space;&plus;&space;f(t_n,&space;y(t_n))(t_{n&plus;1}&space;-&space;t_n)">
with the initial value $y_0 = y(t_0)$. This is called the forward Euler method.

## Modified Euler's Method 
The Modified Euler's method builds on the forward euler's method and is a second order method. 
It essentially hinges on the following equations, 

<img src="https://latex.codecogs.com/svg.image?y_{n&plus;1}^*&space;=&space;y_n&space;&plus;&space;hf(t_n,&space;y_n)">
and 
<img src="https://latex.codecogs.com/svg.image?y_{n&plus;1}&space;=&space;y_n&space;&plus;&space;{h\over&space;2}(f(t_n,&space;y_n)&space;&plus;&space;f(t_{n&plus;1},&space;y_{n&plus;1}^*))">
It essentially takes the midpoint between the projected $y_{n+1}^*$ using the forward euler's method
and the current projection. The attached python script in this repo demonstrates the modified euler's method and is of a higher order accuracy compared to the forward euler's method. For the initial value problem of a simple projectile, the graph below is the output

<img width="586" alt="Screen Shot 2022-03-30 at 2 45 48 PM" src="https://user-images.githubusercontent.com/76069770/160908545-d9940be5-08b3-4ab2-9816-cff73a6e7d7b.png">
