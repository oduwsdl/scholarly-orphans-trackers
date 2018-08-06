# Scholarly Oprhans Trackers

# AS2 Models

The AS2 models for various portals are available in the [models folder](./models).
Each portal in the models folder is split into three directories: `tracker`, `capture`, and `archiver`.
Each of these directories contain models for the `tracker`, `capture`, and `archiver` components of the pod.
Under each of these directories, there are AS2 message models for the most common event types for a portal.

All the models are serialized in valid JSON-LD.
They are passed around and are consumed directly by the various components in the pod.
In all the models across various portals, the researcher the pod is tracking is named `Alice`, and only the artifacts `Alice` creates and interacts with is of interest for the pod.
Hence, artifacts created by other researchers, even when they may be in a portal that `Alice` is involved in, is not of concern for the pod.
For example, if a researcher named `Bob` commits a contribution to a repository owned by `Alice`, `Alice's` pod will not track this event.
Also, for simplicity, the models assume that `Alice` only interacts with artifacts created by `Bob`.

The AS2 messages generated by the tracker and the archiver must be based on these models.
To add a new model or to edit an existing model, the following steps must be taken to make sure the models are compatible:

* The JSON must be converted to RDF/XML using [http://www.easyrdf.org/converter](http://www.easyrdf.org/converter).
* The RDF/XML output from the previous step is validated and visualized using:
[https://www.w3.org/RDF/Validator/](https://www.w3.org/RDF/Validator/).

The RDF conversion and visualization helps keep the model and the graph simple as things can become very
complex very fast when working with JSON alone.
All of the existing models have been validated by performing the steps above, so any existing model can be used for comparison when creating any new model.

# Collaborators

Scholarly Orphans Trackers is a collaboration between the Prototyping Team of the Research Library of the Los Alamos National Laboratory and the Computer Science Department of Old Dominion University.

The Scholary Orphans tracker models are based on the analysis and design of:

- Harihar Shankar (@hariharshankar)
- Martin Klein (@martinklein0815)
- Herbert Van de Sompel (@hvdsomp)

# License

This repository is licensed under the Apache 2.0 license.
