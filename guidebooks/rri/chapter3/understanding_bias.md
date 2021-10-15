# Understanding Bias

Before we start exploring the [project lifecycle](../chapter4/index.md) and its associated activiyies there is a final topic that we need to explore.
You will likely have some prior familiarity of the term 'bias', but your understanding of the concept may emphasise specific properties that reflect a specific focus of your research background.
This section will present three common ways that 'bias' can be understood as it applies to and affects the research and innovation lifecycle. 
The three perspectives that we will look at are: social, statistical, and cognitive bias.

## Social Bias

Outside of research and development communities, the term 'bias' is often associated with some form of prejudice or discrimination.
For example, an inclination or disposition to treat an individual or organisation in a way that is considered to be unfair.
This understanding of bias is necessary to draw attention to pre-existing or historical patterns of discrimination and social injustice that can be perpetuated, reinforced, or exacerbated through the development and deployment of data-driven technologies.
There are numerous examples that illustrate this point.

````{panels}
[Amazon's recruitment tool](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G) that perpetuated bias in hiring against women.
^^^
This algorithmic system learned to perpetuate a bias to prefer male candidates to female candidates because this reflected past hiring decisions.
+++
---

[Predictive policing](https://www.technologyreview.com/2020/07/17/1005396/predictive-policing-algorithms-racist-dismantled-machine-learning-bias-criminal-justice/) that use geospatial data to try to learn associations between places, events, and historical crime rates.
^^^
The attempt to predict where and when crimes are more likely to happen can create a positive feedback loop, which results in over-policing that may exacerbate tensions between communities and police.
+++
---

[Clinical decision support systems](https://www.nature.com/articles/d41586-019-03228-6) can contribute to existing forms of racial bias in access to healthcare.
^^^
A study conducted in the US found that an algorithm that used health costs as a proxy for health needs was ''less likely to refer black people than white people who were equally sick to programmes that aim to improve care for patients with complex medical needs''. {cite:p}`obermeyer2019`
+++
---
````

A commonly heard response to such examples is the claim that the underlying problem is that the training data used to develop the algorithms or models were insufficiently representative.
In other words,''*it was the data that were biased*''.
The assumption behind this claim is that better data collection would solve the problem.
Unfortunately, *at best* this response is only partially true, but *at worst* it belies a commitment to a form of 'technological solutionism'[^solutionism] that often ignores how technology affects social practices and norms.

It is important to remember that most decisions that drive the project lifecycle are made by the project team.
A choice to design a study in a particular way, or to deploy a system in a context that is characterised by patterns of historical discrimination, cannot simply be blamed on poor data.

[^solutionism]: The term 'technological solutionism' is often used to refer to the belief (or, "faith") that technology can be used to solve a problem that was likely caused by technology in the first place. {cite}`morozov2013`

## Statistical Bias

If you are a data scientist, or use techniques from data science in your research or development, then it is likely that your understanding of bias is influenced by statistical concepts.

Jeff Aronson explores the etymology of the term 'bias' in a series of interesting blog articles, which emphasise the statistical understanding of bias {cite}`aronson2018`.
He begins by tracing it back to the game of bowls, where the curved trajectory of the bowl as it ran along the green reflected the asymmetric shape of the bowl (i.e., its bias).
However, according to Aronson, the term was not used in statistics until around the start of the 20th Century where it was used to refer to a systematic deviation from an expected statistical result that arises due to the influence of some additional factor.
This understanding is common in observational studies where bias can arise in the process of sampling or measurement.

On the basis of his historical review, Aronson identifies six features of definitions of bias that adopt a statistical perspective:

* Systematicity: bias arises from a *systematic* process, rather than a random or chance process.
* Truth: a realist assumption that the deviation is from a *true state* of the world
* Error: the bias reflects an error, perhaps due to *sampling or measurement*
* Deviation (or Distortion): a quantity in which the observed result is taken to differ from the actual result were there no bias.
* Affected elements: the study elements that may be affected by the bias include the conception, design, and conduct of the study, as well as the collection, analysis, interpretation, and representation of the data
* Direction: the deviation is directional, as it can be caused by both an under- or over-estimation

Some of these features are specific to a statistical framing of 'bias', but some also apply to the other two perspectives
For instance, 'systematicity' is arguably a necessary property for social biases (i.e., a bias that *systematically* leads to discriminatory outcomes).
And, 'error' is sometimes a property of our next perspective: cognitive biases.

## Cognitive Bias

Our modern understanding of cognitive biases has been most heavily influenced by research conducted by Daniel Kahneman and Amos Tversky.
A lot of their work exposed a wide variety of psychological vulnerabilities, which impact our judgement and decision-making capabilities.
In short, their experiments showed how individuals rely on an assortment of heuristics or biases, which speed up judgement and decision-making but also lead us astray.

For example, consider the following example.

````{admonition} The Linda Problem
:class: tip
Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations.

Which is more probable?

1) Linda is a bank teller.
2) Linda is a bank teller and is active in the feminist movement.

Try to answer this question yourself, before you reveal the answer.

```{dropdown} Reveal
The correct answer is (1). Did you get it right?

If you got it wrong, you have just committed what is known as the 'conjunction fallacy'. But don't worry you're in very good company!

The probability of two events occurring in conjunction, such as Linda being both a 'bank teller' and 'active in the feminist movement' must be less than or equal to the probability of either event occuring on its own. 

Formally, for two events A and B, $Pr(A \wedge B) ≤ Pr(A) and Pr(A \wedge B) ≤ Pr(B)$.
```
````

When Kahneman and Tvserky posed this question to a group of 88 undergraduate students, only $15%$ got the correct answer. They attributed this to failure to what is known as the *representativeness heuristic*.

A critical perspective on this view would see it as an attempt to catalogue a variety of *cognitive failures* or *irrationalitiees*, which stem from an individual’s inability to perform rational calculations. However, such a perspective fails to take into consideration the plurality of permissible outcomes that may be rational in certain decision tasks when additional constraints are recognised (e.g. environmental factors that place temporal constraints on choice behaviour).

An alternative to the heuristics-and-biases program is a view known as ecological rationality, made famous by Herbert Simon, and later developed by Gerd Gigerenzer. In a variety of studies, advocates of ecological rationality have shown that some observed choice behaviour, which violates traditional normative standards of rationality, should nevertheless be treated as rational when additional details about environmental structure are considered.  This alternative approach reframes a lot of human judgement and decision-making as underpinned by “fast and frugal” heuristics, which are highly adaptive and support decision-making in complex and uncertain environments. 
