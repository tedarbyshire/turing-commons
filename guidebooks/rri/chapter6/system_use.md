# System Use, Monitoring, and Updating

- Model drift and concept creep
- Responsibility though sustainability: monitoring and updating

Depending on the context of deployment, it is likely that the performance of the model could degrade over time. This process of *model drift* is typically caused by increasing variation between how representative the training dataset was at the time of development and how representative it is at later stages, perhaps due to changing social norms (e.g. changing patterns of consumer spending, evolving linguistic norms that affect word embeddings). As such, mechanisms for monitoring the model's performance should be instantiated within the system's runtime protocols to track model drift, and key thresholds should be determined at early stages of a project (e.g. during project planning or in initial impact assessment) and revised as necessary based on monitoring of the system's use.

## Model Updating or De-provisioning

- De-provisioning is not really an option in research

As noted previously, model updating can occur continuously if the architecture of the system and context of its use allows for it. Otherwise, updating the model may require either revisiting previous stages to make planned adjustments (e.g. model selection and training), or if more significant alterations are required the extant model may need to be entirely de-provisioned, necessitating a return to a new round of project planning.

[^aversion]: Algorithmic aversion refers to the reluctance of human agents to incorporate algorithmic tools as part of their decision-making processes due to misaligned expectations of the algorithm's performance (see {cite:p}`burton2020`).

This overview and summary of the project lifecycle is by necessity an abstraction. However, it provides a useful anchor for subsequent discussion, and serves to motivate the following question: how do you provide assurance for the diversity of tasks included throughout the process? For instance, there may be a plurality of ethical goals relevant to the assurance of <span style="font-variant:small-caps;">(model) development</span> or <span style="font-variant:small-caps;">system use and monitoring</span>, including demonstrating that the system being deployed is safe, secure, fair, trustworthy, explainable, sustainable, or respectful of human agency and autonomy. How do you provide assurance that the interconnected project processes and activities individually and collectively support the relevant goal? This is why we need a unifying framework and methodology that makes space for the operationalisation of end-to-end, normative considerations and complements existing regulatory culture, as opposed to merely a miscellany of practical mechanisms.
