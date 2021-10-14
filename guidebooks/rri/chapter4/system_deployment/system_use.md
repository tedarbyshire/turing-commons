# System Use, Monitoring, and Updating

- Model drift and concept creep
- Responsibility though sustainability: monitoring and updating

Depending on the context of deployment, it is likely that the performance of the model could degrade over time. This process of *model drift* is typically caused by increasing variation between how representative the training dataset was at the time of development and how representative it is at later stages, perhaps due to changing social norms (e.g. changing patterns of consumer spending, evolving linguistic norms that affect word embeddings). As such, mechanisms for monitoring the model's performance should be instantiated within the system's runtime protocols to track model drift, and key thresholds should be determined at early stages of a project (e.g. during project planning or in initial impact assessment) and revised as necessary based on monitoring of the system's use.
