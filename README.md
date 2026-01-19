# Fire Weather Index Prediction Service

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-production-orange?style=flat-square)
![Inference](https://img.shields.io/badge/Inference-0.36ms-success?style=flat-square)

Production-grade ML inference service for forest fire risk assessment.

This project implements a **deterministic, low-latency machine learning service** for predicting the Fire Weather Index (FWI) from environmental signals.  
The system is engineered for **correctness, reproducibility, and operational safety**, not model novelty.

The production model is a **single serialized scikit-learn pipeline** (StandardScaler → Ridge Regression), ensuring identical outputs for identical inputs across deployments and eliminating training–serving skew.

---

## System Goals

- Provide fast and reliable FWI predictions for real-time decision support  
- Guarantee deterministic inference with bounded inputs and safe failure modes  
- Enable future lifecycle extensions (drift detection, retraining, rollback)  

This is **not** a research or Kaggle-style project.  
It is an ML service designed to be **operated**, not demoed.

---

## Key Properties

- **Deterministic inference:** end-to-end pipeline serialized as a single artifact  
- **Stateless REST API:** suitable for containerized and cloud environments  
- **Strict input validation:** rejects out-of-range environmental parameters  
- **Low-latency serving:** optimized for sub-millisecond inference  

---

## Technical Stack

| Layer | Technology |
|-----|-----------|
| Language | Python 3.9+ |
| Machine Learning | scikit-learn (Ridge Regression, StandardScaler) |
| Serialization | Joblib |
| Serving | Flask (REST API) |
| Interface | Minimal HTML/CSS (manual testing only) |

---

## Model Performance

Measured on held-out test data.

- **R²:** 0.987  
- **MSE:** 0.38  
- **Average inference latency:** 0.36 ms (1000-run benchmark, single instance)

These metrics reflect a deliberate tradeoff favoring **latency, stability, and interpretability** over marginal accuracy gains from heavier models.

---

## Repository Structure

```text
├── src/fwi/
│   ├── api.py          # HTTP interface (Flask)
│   ├── model.py        # Model loading & inference
│   └── validate.py     # Input validation & invariants
│
├── models/
│   └── model.pkl       # Serialized ML pipeline
│
├── data/
│   └── cleaned_forest_fires.csv
│
├── scripts/
│   ├── evaluate.py     # Offline model evaluation
│   └── benchmark.py   # Inference latency benchmarking
│
├── templates/          # Minimal UI for manual testing
├── requirements.txt
└── README.md