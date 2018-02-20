# Data Analysis: Intercalation of *X*=(Li, Na, Mg, Ca, Al) into (F/OH)-substituted anatase TiO<sub>2</sub>

Authors:
- B. J. Morgan ORCID: 0000-0002-3056-8233

[![CircleCI](https://circleci.com/gh/bjmorgan/data_F-TiO2_intercalation_anions.svg?style=shield&circle-token=62e9c3a0cf6c788761c1ab66018dced0a0a4fd60)](https://circleci.com/gh/bjmorgan/data_F-TiO2_intercalation_anions)

TODO:
- Add to Zenodo, and link doi here.

## Summary

This repository contains data analysis for a series of DFT calculations of metal intercalation into (F/OH)-substituted anatase TiO<sub>2</sub>.

The analysis contained here supports the findings reported in 
J. Ma *et al.*, &ldquo;Lithium Intercalation in Anatase Titanium Vacancies and the Role of Local Anionic Environment&rdquo; \[1\], and includes code for plotting the figures in this paper that report DFT data.

The repository consists of
1. A series of .yaml files, containing data extracted from VASP calculations. The inputs and outputs for the source VASP calculations, along with the scripts to extract the raw data used here, are available at the [University of Bath Data Archive](TODO).
2. Jupyter notebooks containing code for data analysis and figure plotting:
    - Comparison of the relative energies for groups of F_O or OH_O defects as a function of their positions relative to the V_Ti defect. TODO: add nbviewer link.
    - Calculation of intercalation energies for *X*=(Li, Na, Mg, Ca, Al) into (F/OH)-substituted anatase TiO<sub>2</sub>. TODO: add nbviewer link.

## Overview

This top level directory contains four sub-directories: `data`, `analysis`, `figures`, and `tests`.

* **`data/`**: This folder contains a series of `.yaml` filed, containing data extracted from VASP calculations. The inputs and outputs for the source VASP calculations, along with scripts for extracting the relevant data and generating these files, are available at the [University of Bath Data Archive]TODO.

* **`analysis/`**: This folder contains Jupyter notebooks that perform the analysis of the DFT data, using the input data in the `data` folder. These notebooks also generate relevant figures for publication.

* **`figures/`**: This folder contains figures for publication, produced by the analysis scripts.

* **`tests/`**: This folder contains tests to check that the notebooks in the `analysis` folder runwithout errors.

## Dependencies

Python dependencies are listed in the [`requirements.txt`](requirements.txt) file.

## Tests

Notebook execution can be tested by running:
```
python3 -m unittest discover
```

Automated testing that all notebooks execute without errors happens [here](https://circleci.com/gh/bjmorgan/data_F-TiO2_intercalation_anions).

## References

1. J. Ma *et al.*, In Submission.
2. B. J. Morgan &ldquo;DFT Dataset: Intercalation of *X*=(Li, Na, Mg, Ca, Al) into (F/OH)-substituted anatase TiO<sub>2</sub>&rdquo; [University of Bath Research Data Archive]TODO

