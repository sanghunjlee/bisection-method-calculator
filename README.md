# Bisection Method Calculator
The Bisection Method Calculator (BMC) approximates a zero (a root) of a given function by iterating through a number of values determined through the bisection method.

## Description
This program will read user typed function and will attempt to find a zero using the bisection method. The method is based on the following mathematical statement:
```
Given a differential function *f* that stisfies *f(a) \* f(b) < 0*,
there must exists *x_0* such that *f(x_0) = 0*
```
The bisection process uses the following equation to pinpoint the next *x_c* to test the condition *f(x_a) \* f(x_c) < 0* (or *f(x_c) \* f(x_b) < 0*):
```
*x_c = (x_a + x_b) / 2* 
where *x_a < x_c < x_b*
```
