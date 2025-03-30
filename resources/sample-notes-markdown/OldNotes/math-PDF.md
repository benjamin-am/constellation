## Probability Density Functions

Probability density function. We have seen many examples of discrete random
variables, including some of the most important ones: Bernoulli, binomial and
geometric. The next definition introduces another major class of random variables.
This class is studied with the tools of calculus.
Definition 3.1. Let X be a random variable. If a function f satisfies
(3.3) P (X ≤ b) = ∫f(x)dx
for all real values b, then f is the probability density function (p.d.f.) of X.
In plain English the definition requires that the probability that the value of X
lies in the interval (−∞, b] equals the area under the graph of f from −∞ to b. An
important (and somewhat surprising) technical fact is that if f satisfies Definition
3.1 then
(3.4) P (X ∈ B) = ∫f(x) dx
for any subset B of the real line for which integration makes sense. We prefer (3.3)
for the definition because this ties in with the cumulative distribution function (to
be introduce