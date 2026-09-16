# EV ML Dashboard
Python Streamlit frontend + Node.js/Express backend + Python ML engine.

Features: six regression models, model comparison, live inference, live retraining, what-if multi-model testing, dataset explorer, model registry, governance controls, leakage prevention, dataset fingerprinting and audit logs.

## Run
1. `pip install -r requirements.txt`
2. `cd backend && npm install && npm start`
3. In another terminal: `streamlit run frontend/app.py`

Replace the included demo CSV with your actual `EV_Charging_Station_Usage_2.csv` before submission.
