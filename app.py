import streamlit as st,requests,pandas as pd,os

st.set_page_config(page_title="EV Charging ML Intelligence",page_icon="⚡",layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #101b2d 0%, #0b1220 35%, #050b14 100%);
        color: #e2e8f0;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #f8fafc !important;
        font-weight: 800;
        letter-spacing: 0.04em;
        text-shadow: 0 2px 8px rgba(56, 189, 248, 0.18);
    }
    h2, h3 {
        color: #7dd3fc !important;
        font-weight: 700;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.88));
        border-right: 1px solid rgba(148, 163, 184, 0.18);
    }
    .stMetric > div {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: 0 14px 32px rgba(14, 116, 144, 0.18);
    }
    [data-testid="stMetricLabel"] { color: #cbd5e1 !important; }
    [data-testid="stMetricValue"] { color: #f8fafc !important; font-weight: 700; }
    .stDataFrame, .stTable {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 14px 30px rgba(14, 165, 233, 0.18);
    }
    .stAlert, .stSuccess, .stInfo, .stWarning {
        border-radius: 14px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(96, 165, 250, 0.18);
        color: #e2e8f0;
    }
    .stApp a, .stApp p, .stApp li, .stApp div {
        color: #e2e8f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

API=os.getenv("EV_API_URL","http://localhost:5000/api"); st.title("⚡ EV Charging ML Intelligence Platform"); st.caption("Regression • Live Inference • Training • Dataset Explorer • Model Governance")
try: requests.get(API+"/health",timeout=3).raise_for_status()
except Exception: st.error("Start backend first: cd backend && npm install && npm start"); st.stop()
try:
    d=requests.get(API+"/analytics",timeout=60)
    d.raise_for_status()
    payload=d.json()
except Exception as exc:
    st.error(f"The backend is unavailable or responded with an error: {exc}"); st.stop()
r=payload.get("registry",{})
m=pd.DataFrame(r.get("models",[]))
a,b,c,e=st.columns(4)
a.metric("Sessions",payload.get("shape", [0,0])[0])
b.metric("Columns",payload.get("shape", [0,0])[1])
c.metric("Models",len(m))
e.metric("Target","Energy (kWh)")
st.subheader("Model Benchmark")
if m.empty:
    st.warning("No trained model metrics are available yet. Train a model from the Live Inference page.")
else:
    st.dataframe(m,width="stretch",hide_index=True)
    st.bar_chart(m.set_index("model")[["mae","rmse"]])
st.info("Use the sidebar pages for detailed analytics, live testing/training, data exploration and governance.")