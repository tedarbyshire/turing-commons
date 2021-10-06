# Model Documentation and Productionalization

- The limits of transparency
  - Handling sensitive information
  - Protecting against model inversion
  - Transparency is not accountability
- What needs to be documented?
  - Evaluating current tools (e.g., datasheets, factsheets, model cards, and TRIPOD)
    - Who is your audience?
    - What are you developing?

Although the previous stages are likely to create a series of artefacts while undertaking the tasks themselves, model reporting should also be handled as a separate stage to ensure that the project team reflect on the future needs of various stakeholders and end users. While this stage is likely to include information about the performance measures used for evaluating the model (e.g. decision thresholds for classifiers, accuracy metrics), it can (and should) include wider considerations, such as intended use of the model, details of the features used, training-testing distributions, and any ethical considerations that arise from these decisions (e.g. fairness constraints, use of politically sensitive demographic features).

Unless the end result of the project is the model itself, which is perhaps more common in scientific research, it is likely that the model will need to be implemented within a larger system. This process, sometimes known as 'model operationalisation', requires understanding (a) how the model is intended to function in the proximate system (e.g. within an agricultural decision support system used to predict crop yield and quality) and (b) how the model will impact—and be impacted by—the functioning of the wider sociotechnical environment that the tool is embedded within (e.g. a decision support tool used in healthcare for patient triaging that may exacerbate existing health inequalities within the wider community). Ensuring the model works within the proximate system can be a complex programming and software engineering task, especially if it is expected that the model will be updated continuously in its runtime environment. But, more importantly, understanding how to ensure the model’s sustainability given its embeddedness in complex and changing sociotechnical environments requires active and contextually-informed monitoring, situational awareness, and vigilant responsiveness.