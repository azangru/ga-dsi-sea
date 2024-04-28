---
title: Case Study in Bayesian Analysis
type: lab
duration: "1:25"
creator:
    name: Chris Esposo
    city: Atlanta, GA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

## Lab Intro

Welcome to your first lab in Bayesian Analysis. This lab is just to take a brief look over the probability and distribution tools you might have forgotten over the past few weeks.

## Exercise

Since we've spent the past few weeks working on  machine learning applications, in this lab we'll review some statistics fundamentals using Python.

|     Distribution  | Probability Mass Function (The Formula)  | Written Description
|:-:|---|---|
| Uniform  | `$\frac{1}{n}$` |  Basically, a uniform distribution is utilized when you're selecting any one member of a set is just as likely as any other  |
| Bernoulli   | `$\binom{n}{k}\cdot p^{k}(1-p)^{1-k} $`  | Like a coin flip, p represents the probability that event X occurs, and 1-p is the probability that event Y occurs  |
| Poisson | `$\frac{e^{-n}n^{x}}{x!}$` | The probability of observing x events in a certain time interval. e is the Euler number and n is a tuning parameter |
| Binomial  | `$\binom{n}{k}\cdot p^kq^{n-k} $` | Gives you the probability of getting k "success" in n iterations/trials |
| Chi-Squared  | --- | Used for goodness of fit of an observed distribution to a theoretical one i.e. how well you thought your sports team was going to do over how they actually did |
| Cauchy | --- | Describes the distributions of horizontal distances in a line segment. Similar to Normal Distribution  |

Lastly, we will introduce the Beta function, which will be a critical tool to add to our Bayesian reportoire this week.

#### Requirements
We're going to be dealing with some theoretical material, which is required to understand the foundations of statistics. Therefore, you'll need to review some of the basic counting identities.

For the small code snippet on coin-tosses, you may want to take a few minutes first to [review this video from Khan Academy](https://www.khanacademy.org/math/ab-sixth-grade-math/al-statistics-probability/al-probability/v/coin-flipping-example). It gives a great overview of the problem statement, as well as a good work-through of some potential solutions.

Next, [open the starter code](./w8-1.2-starter.ipynb) and begin to try your hand at today's exercises!

**Bonus:**
- Look up [Fisher's exact test](https://en.wikipedia.org/wiki/Fisher%27s_exact_test), which will show you a more substantive example of the link between counting and statistics. Try to derive the exact test yourself with some basic counting principles.

#### Starter code

[Starter Code](./Lab Worksheet Starter.ipynb)

#### Deliverable

Complete the lab notebook and provide the necessary solutions.

#### Additional Resources

For those of you who want to read further:

- [Math is Fun](http://www.mathsisfun.com/data/basic-counting-principle.html)
- [Khan Academy Prework](https://www.khanacademy.org/math/probability/statistics-inferential/margin-of-error/v/mean-and-variance-of-bernoulli-distribution-example)
