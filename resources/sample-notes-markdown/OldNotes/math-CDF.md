## Cumulative Distribution Functions

Probability mass functions are defined only for discrete random variables and den-
sity functions only for continuous random variables. By contrast, the cumulative
distribution function gives a way to describe the probability distribution of any
random variable, including those that do not fall into the discrete or continuous
categories.
Definition 3.10. The cumulative distribution function (c.d.f.) of a random
variable X is defined by
(3.12) F (s) = P (X ≤ s) for all s ∈ R.
It is very important to be mindful of the convention that the inequality is
≤ in definition (3.12). The cumulative distribution function gives probabilities of
left-open right-closed intervals of the form (a, b]:
P (a < X ≤ b) = P (X ≤ b) − P (X ≤ a) = F (b) − F (a).
Knowing these probabilities is enough to determine the distribution of X com-
pletely. But proving this fact is beyond the scope of this book