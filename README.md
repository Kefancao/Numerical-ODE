# Ordinary Differential Equation
This repo is intended for me to introduce a common technique called the Euler's method to solve derivatives. The Euler's method is one that has been taught to most people during high school as the fundamental theorem of calculus. It looks similar to this, 

$$f(x+h) - f(x) \approx f(x) \cdot h$$
Rearranging we have, 
$$f(x+h) \approx f(x)\cdot h + f(x)$$

Turns out, if we're given an initial value, we can apply a similar technique to get the derivative! 
If we're given the initial value problem, 
$${dy\over dt} = f(t, y(t)) \text{ with }y(t_0) = y_0$$
We can then pick a set of discrete points and uses them to compute the slope as a form of approximation to the derivative, developing a recursive scheme for determining an **approximated**
$y_n$ values. Applying the formula for the slope, 

$${y(t_{n+1}) - y(t_n) \over t_{n+1} - t_n} = y'(t_n) = f(t_n, y(t_n))$$

Rearranging,
$$y_{t_{n+1}} = y(t_n) + f(t_n, y(t_n))(t_{n+1} - t_n)$$
with the initial value $y_0 = y(t_0)$. This is called the forward Euler method.

## Modified Euler's Method 
The Modified Euler's method builds on the forward euler's method and is a second order method. 
It essentially hinges on the following equations, 

$$y_{n+1}^* = y_n + hf(t_n, y_n)$$
and 
$$y_{n+1} = y_n + {h\over 2}(f(t_n, y_n) + f(t_{n+1}, y_{n+1}^*))$$
It essentially takes the midpoint between the projected $y_{n+1}^*$ using the forward euler's method
and the current projection. The attached python script in this repo demonstrates the modified euler's method and is of a higher order accuracy compared to the forward euler's method. For the initial value problem of a simple projectile, the graph below is the output
