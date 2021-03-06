# Baseline Primer

Establish terms so we know we are talking about the same thing when we say a word.

## Probability

* **Probability** - *P* - the likelihood that an event will occur
  * If *p* = 0, the event will not occur.
  * If *p* = 1, the event will occur.
  * The probability of *A* happening is *P(A)*
  * The probability of *A* happening, given that *B* has occurred is *P(A|B)*
    > ![conditional probability](./img/fd0d993e-43c1-4eeb-81e5-92bc3f36d1fe.png)<!--
      P(A|B) = \frac{P(A \cap B)}{P(B)}
      -->
  * Rewritten is the multiplication rule:
    > ![multiplication rule](./img/0e5a30e9-26bd-42d8-9ef1-edd694e6fe34.png)<!--
      P(A \cap B) = P(A|B) \cdot P(B)
      -->
* Example: What is the probability that you draw from a pack of cards 2 diamonds in a row?
  * Reworded: What is the probability that the second card drawn from a pack of cards is a diamond *P(D<sub>2</sub>|D<sub>1</sub>)*, given that the first card drawn was a diamond *P(D<sub>1</sub>)*?
  * If 1 card has been drawn from a pack of cards, the probability that diamond is drawn from the remaining cards is:
   * *P(D<sub>2</sub>|D<sub>1</sub>)* = 12/51
  * The probability of drawing a diamond as the first card is 1/4.
  * *P(D<sub>2</sub> &cap; D<sub>1</sub>) = *P(D<sub>2</sub>|D<sub>1</sub>)  * P(D<sub>1</sub>)* = 12/51 * 1/4 = 3/51
* **Mutually Exclusive** - two events cannot occur at the same time.
  * *A* is independent of *B* if *P(A|B) = P(A)*
* **Bayes' Theorem**
  > ![Bayes' Theorem](./img/d09541ec-5a36-4035-9cb2-192a52f5324c.png)
  * Proof (divide both sides by *P(A)*:
    *P(B|A) * P(A) = P(A &cap; B) = P(A|B) * P(B)*
  * Let *H<sub>1</sub>* be the probability that the first coin toss is heads, and let *H<sub>2</sub>* be the probability that all 3 coin tosses are heads.
    * Then *P(H<sub>1</sub>|H<sub>A</sub>)* = 1, while *P(H<sub>A</sub>|H<sub>1</sub>)* = 1/4
  * **Sally Clark**
    * What is the probability that a mother's first 2 babies dies of SIDS? Are these events dependent or independent?
    * Given that a mother's first baby died of SIDS, what is the probability that her second baby will also die of SIDS?
    * Professor Sir Roy Meadow incorrectly concluded that these were 2 independent events, and famously said it was a "1 in 73 million" chance.
    * This false statistic lead to her false conviction in November 2009.
    * She was release on January 2003, but died in March 2007 from alcohol poisoning.

## Discrete Random Variables


* **Random Variable** - a variable with a value that determined by a chance event.
* ** discrete sample space** *&Omega;* is a finite set of outcomes {*&omega;<sub>1</sub>, &omega;<sub>2</sub>...*}. The probability of an outcome *&omega;* is *P(&omega;)*.
* **Discrete Probability Distribution** - a distribution that can be represented by a table. For example, there are only 4 outcomes from flipping a coin 2 times.

<table>
    <tr>
        <th>Number of Heads, x</th>
        <th>Probability P(x)</th>
    </tr>
    <tr>
        <td>0</td>
        <td>0.25</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0.5</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0.25</td>
    </tr>
</table>

* Note that the sum of all these probabilities equals 0.
* **Probability Mass Function pmf** - the function for a discrete random variable
  * *p(a) = P(X = a)*, where 0 &le; *p(a)* &le; 1
* **Cumulative Distribution Function cdf** - the function that gives the total probabilities from minus infinity to *a*
  * *F(a) = P(X ≤ a)*
* Example: let the sample space *&Omega;* be 2 dice rolls, and let a random variable *M* be the maximum of 2 dice rolls. In other words M(1,4) = 4.

<table>
    <tr>
        <th>value</th>
        <th><em>a</em></th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
    </tr>
    <tr>
        <td>pdf</td>
        <td><em>p(a)</em></td>
        <td>1/36</td>
        <td>3/36</td>
        <td>5/36</td>
        <td>7/36</td>
        <td>9/36</td>
        <td>11/36</td>
    </tr>
    <tr>
        <td>cdf</td>
        <td><em>F(a)</em></td>
        <td>1/36</td>
        <td>4/36</td>
        <td>9/36</td>
        <td>16/36</td>
        <td>25/36</td>
        <td>36/36</td>
    </tr>
</table>


  * *F(a)* only increases. If *a &le; b*, then *F(a) &le; F(b)*
  * 0 &le; *F(a)* &le; 1
* **Bernoulli Distributions** - See page on [Bernoulli Trials](https://github.com/herereadthis/sagaxus/blob/master/docs/bernoulli-trials.md)
* **Binomial Distributions** - See above

  * **Discrete Variable** - variables that can only be certain values, within a range. For example, the number of heads from *n* coin flips is a whole number between 0 and *n*. It cannot be fractions.
    * Discrete Variables can be **finite** or **infinite**. While coin flips that result with heads can be infinite, but selecting aces from a pack of cards is finite.
  * **Continuous Variable** - variables that be any value within a range. For example the height of a person selected from a population is continuous.
* **Probability Distribution** a table or equation that can describe every outcome and its probability of occurance.


## Discrete Mean and Variance

* **Discrete Mean** - the mean of a discrete random variable X is also known as the **expected value** of X, E(X)
  > ![discrete mean](./img/991a07a6-e273-4bb0-abba-b05abf6760e4.png)<!--
    E(X) = \mu_{x} = \sum_{i=1}^n p(x_{i}){x_{i} }
    -->
  * Expected Value is the sum of every outcome times is probability.
  * For a variable *X* with mean *&mu;<sub>x</sub>* and a variable *Y* with mean *&mu;<sub>y</sub>*:
    * *&mu;<sub>x + y</sub>* = *&mu;<sub>x</sub>* + *&mu;<sub>y</sub>*
    * *&mu;<sub>x - y</sub>* = *&mu;<sub>x</sub>* - *&mu;<sub>y</sub>*
* **Discrete Variance** - a measure of how much the probability mass is spread out around the discrete mean.
  > ![Discrete variance](./img/ed1fd387-4f36-4bb8-9f75-7c06a74e64c3.png)<!--
    \text{Var}(X) = \text{E}[(X- \mu )^{2}] = \sum_{i=1}^n p({x_{i})(x_{i}- \mu )^{2} }
    -->
  * Where *X* is a random variable with a mean *E(X) = &mu;*
  * Variance is taking the weighted average of the squared distance to the mean. Squaring makes sure we are averaging non-negative values (the spread to the right doesn't cancel the spread to the left). Using expectation means we weigh the high-probability values more.
    * *&sigma;* has the same units as *X*
    * *Var(X)* has the same units as the square of *X*. If X is measured in inches, then *Var(X)* is inches squared.
* **Discrete Standard Deviation** - *&sigma;* - the square root of the variance
  > ![discrete standard deviation](./img/85abbbef-2b89-4b6a-ae68-8cb6219ae441.png)<!--
    \sigma = \sqrt{\text{Var}(X)}
    -->
  * Because *&sigma;* and *X* have the same units, the standard deviation is measure of the spread.
* **Discrete Independence** - two random variables *X* and *Y* are independent if the probably of both of them happening is the product of their probabilities
  * *P(X = a, Y = b) = P(X = a) * P(X = b)*
  * *X* and *Y* are independent if *Var(X + Y)= Var(X) + Var(Y)*
  * For constants *a* and *b*, *Var(aX + b) = a<sup>2</sup>Var(X)*.
  * *Var(X) = E(X<sup>2</sup>) − E(X)<sup>2</sup>*

## Continuous Random Variables

* A random variable X is **continuous** if there is a function *f(x)* such that for any *c &le; d*, the probability density function is:
  > ![continuous pdf](./img/6786b048-ab22-4611-a4e1-6224e33501e9.png)
  * The pdf is always non negative *f(x) &ge; 0*
  * and the pdf across all ranges will equal 1
  > ![infinity pdf](./img/9efb5908-31e8-4389-ad03-345bf5fdf7d9.png)
  * You have to integrate *f(x)* to get the probability
* **Median** - the value *x* for X where *P(X &le; x) = 0.5*
  * That is, *X* has equal probability of being above or below the median
* **Continuous Probability** - a distribution that is expressed as an equation called a **Probability Density Function**
    * a random variable *y* is a function of *x* such that *y = f(x)*
    * 0 &le; *y* &le; 1 for all values of *x*
    * The area of the curve created by the function is equal to 1
    * The probability that *y* occurs within the interval of *a* and *b* is equal to the area of the function curve from *a* to *b*
* **Cumulative Distribution Function cdf** - analogous to cmf
  * *F(x) = P(X &le; x)*
  * 0 &le; *F(x)* &le; 1
* **Uniform Distribution** - all outcomes in the range have equal probobability, aka same probability density
  * Parameters: *a, b*
  * Range: *[a, b]*
  * Notation: *U(a, b)*
  * Density: *f(x) = 1/(b - a)* for *a &le; x &le; b*
  * Density (PDF):
    > ![uniform density](./img/35bdff7e-46b5-4892-b9e5-387db1468bc1.png)<!--
      f(x) =\begin{cases}
      \frac{1}{b-a} & x \in [a, b]
      \\0 & otherwise
      \end{cases}
      -->
  * Distribution (CDF):
    > ![uniform distribution](./img/a3763022-a4a3-4d83-adde-5ab0253bd1d0.png)<!--
      F(x) =\begin{cases}
      0 & x < a
      \\\frac{x-a}{b-a} & x \in [a, b]
      \\1 & x \ge b
      \end{cases}
      -->
  * Mean:
    > ![uniform mean](./img/afbf4399-4523-4ea9-b251-a126927e3145.png)<!--
      \mu = \frac{1}{2}(a + b)
      -->
  * Variance:
    > ![uniform variance](./img/42a1b621-535d-470d-8c09-87c6e7ff96e0.png)<!--
      \sigma^2 = \frac{1}{12}(b-a)^2
      -->
  * Standard Deviation:
    > ![uniform standard deviation](./img/589ca684-1b99-4c60-a24f-97747494db3e.png)<!--
      \sigma = \frac{b-a}{\sqrt{12}}
      -->
  * an example of uniform distribution is throwing darts at a dartboard and getting the angle drawn from a vertical line to the center to the dart
* **Exponential Distribution** - the probability of and outcome gets larger as *x* increases
  * Parameter: *&lambda;*
  * Range: [0, &infin;)
  * Notation: exp(&lambda;)
  * Density: *f(x) = &lambda;e<sup>-&lambda;x</sup>* for *0 &le; x*
  * Distribution: *F(x) = 1 - e<sup>-&lambda;x</sup>* for *x &ge; 0*
  * Example: waiting for a taxi to arrive. The longer you wait, the more likely it will arrive

### Normal Distribution

* Also known as a **Gaussian** Distribution, named after Carl Friedrich Gauss
* Parameters: *&mu;, &sigma;*
* Range: (-&infin;, &infin;)
* Notation: *N(&mu;,&sigma;<sup>2</sup>)*
* Density:
  > ![normal density](./img/fb256a18-8ac2-4e0c-8e41-5d14f780e8bf.png)<!--
    f(x) = \phi(z) = \frac{1}{\sigma \sqrt{2 \pi } }e^{\frac{-(x - \mu)^2}{2\sigma^2}}
    -->
* **Standard normal distribution Z** - a normal distribution where *&mu;* = 0 and *&sigma;* = 1
* Let *X* be a random variable with *&mu;* mean and *&sigma;* standard deviation. Then:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)<!--
    Z = \frac{X -  \mu }{ \sigma }
    -->
* [The probability that a value](http://courses.atlas.illinois.edu/spring2016/STAT/ST) *z* is between the mean and *Z*
  * *f(z) = &phi;(z) - 1/2* (probability density function pdf)
  * *P(-1 &le; Z &le; 1)* &asymp; 0.6827
  * *P(-2 &le; Z &le; 2)* &asymp; 0.9545
  * *P(-3 &le; Z &le; 3)* &asymp; 0.9973
* The mean, median and mode of a normal distribution [are the same](https://www.analyticsvidhya.com/blog/2017/09/6-probability-distributions-data-science/).
* The curve of a normal distribution is a bell shaped, and it is symmetrical
  * half the area is left of mean, half is right of mean
* The area under the curve is 1
* The curve is entirely defined by its mean and variance

## Expected Value, Variance, and Standard Deviation for Continuous Random Variables

* **Expected Value** - measures central tendency
  * *&mu; = E(X)*
  > ![expected value, continuous](./img/3f1e837e-afe9-4ce5-9dd5-b69a98b1dc54.png)<!--
    \mathrm{E}[X] =  \int_a^b xf(x)dx
    -->
* Expected Value of a standard normal distribution N(0,1) where *&mu; = 0* and *&sigma; = 1*
  > ![Expected Value standard](./img/ab0b600e-9c73-4017-a99c-ed1af08099a8.png)<!--
    E(z) = \phi(z) = \frac{1}{ \sqrt{2 \pi } }e^{-z^2/2} \Big|_{-\infty}^{\infty} = 0
    -->
* Example: let *X ~ U(0,1)* - for a range [0,1] and a density *f(x) = 1*
  > ![expected value uniform continuous](./img/d235e517-bb02-430b-894f-3047ff491820.png)<!--
    E(X) = \int_{0}^{1}xdx = \frac{x^2}{2}  \Big|_0^1 = \frac{1}{2}
    -->
  * The range of Z is (-&infin;,&infin;)
* **Standard Deviation &sigma;** - measures spread or scale
* **Variance** - square of the standard deviation
  *&sigma;<sup>2</sup> = Var(X)*
  * The formula is the same as for discrete random variables *Var(X) = E((x - &mu;)<sup>2</sup>)*


## Central Limit Theorem

* **Law of Large Numbers** - the frequency of an event will converge on the probability of the event as the number of trials increase.
  * The average of many independent samples is close to the average of the population.
  > ![law of large numbers](./img/a7e65c98-a61e-4cd4-8e2c-5e6c7e8802ed.png)<!--
    \lim_{n \rightarrow \infty} P(\left |  \overline{X} - \mu  \right | < a) = 1
    -->
* **Central Limit Theorem** - as more averages of independent samples is gathered, the distribution approaches a normal distribution
* **Standardization** - For a random variable *X* that has a normal distribution, the standardization is:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)
  * *Z* has a mean of 0 and standard deviation 1
* Let *S<sub>n</sub>* the the sum of *X<sub>1</sub>, X<sub>1</sub>, ... , X<sub>n</sub>* random variables each with a mean &mu; and a standard deviation *&sigma;*. Then the weighted average of the random variables is:
  > ![clt](./img/d837515c-3d03-4737-84a5-7ba8cf4c22d6.png)<!--
    \overline{X}_{n} = \frac{S_{n}}{n} = \frac{X_{1} + \ldots + X_{n}}{n} = \left(\sum_{i=1}^nX_{i}\right)/n
    -->
* Mean
  > ![Expected Value Sum, Sample](./img/79ec9ea9-a0cf-4ae2-b199-b69678789f18.png)<!--
    E(S_{n}) = n\mu, E( \overline{X}_{n}) =\mu -->
* Variance
  > ![Variance Sum, Sample](https://user-images.githubusercontent.com/638189/48675533-fc10a000-eb27-11e8-8ed0-e67c6aa32ed2.png)<!--
    Var(S_{n}) = n\sigma^2, Var( \overline{X}_{n}) =\frac{\sigma^2}{n} -->
* Standard Deviation
  > ![Standard Deviation, sum, sample](./img/d40e14ea-3186-4877-937e-c32daac1597a.png)<!--
    \sigma_{S_{n}} =\sqrt{n}\sigma, \sigma_{\overline{X}_{n}} =\frac{\sigma}{\sqrt{n}} -->
* CLT: For large *n*,
  > ![large n](https://user-images.githubusercontent.com/638189/48675580-9e308800-eb28-11e8-9f9a-6dc3e99fe996.png)

### CLT Examples
  * See [Sampling Size page](https://github.com/herereadthis/sagaxus/blob/master/docs/sampling-size.md) for examples


## Statistics

The goal of statistics is to make inferences based on data.

1. Collect the data
2. Describe the data
3. Analyze the data

* **Statistic** - anything that can be computed from collected data
  * To be more specific, statistic is a rule for computing something, value is what is computed
  * Is a coin fair if it lands 60 heads out of 100 tosses?
* **Probability** - the likelihood that an event occurs
  * What is the likelihood of landing 60 heads out of 100 coin tosses
* **Statistics vs Probability** - for example, the average of 100 dice rolls or the number of times 5 was rolled is a statistic. The likelihood of getting 4 on a dice roll
is *probability.*
* **Pure Statistics** - a single value computed from data, such as a sample average
* **Interval Statistics** - an interval [*a, b*] computed from data.

## Sources

* Graph generator: [http://courses.atlas.illinois.edu/spring2016/STAT/STAT200/pnormal.html](http://courses.atlas.illinois.edu/spring2016/STAT/ST)
* [HTML Math Symbols, Math Entities, and ASCII Math Character Code Reference](https://www.toptal.com/designers/htmlarrows/math/)
* [Rules of Probability](https://stattrek.com/probability/probability-rules.aspx?Tutorial=AP)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Bayes' Theorem: `P(B|A) = \frac{P(A|B)*P(B)}{P(A)}`
  * continuous pdf: `P(c \leq d) = \int_c^d f(x)dx`
  * infinity pdf: `{P(-\infty \leq X \leq \infty) = \int_{-\infty}^\infty f(x) dx = 1}`
  * large n: `\overline{Xn} \approx N(\mu, \frac{\sigma^2}{n}), S_n \approx N(n\mu, n\sigma^2), Zn \approx N(0,1))`
* [Better Online equation editor](https://www.codecogs.com/latex/eqneditor.php)
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
* [Intruction to probability and statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/)
* [Variance of Discrete Random Variables](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf)
* [6 Common Probability Distributions every data science professional should know](https://www.analyticsvidhya.com/blog/2017/09/6-probability-distributions-data-science/)
