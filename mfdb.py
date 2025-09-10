import pandas as pd
import streamlit as st
import plotly.express as px

# Streamlit dashboard start
st.set_page_config(page_title='Machine Failure Prediction', layout='wide')

# load data
@st.cache_data
def load_data():
    return pd.read_csv("maintenance_schedule.csv")

df = load_data()

# ---- Custom CSS for styling ----
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    .section {
        background-color: #ffffff;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⚙️ Machine Failure Prediction Dashboard")

# ================= KPI Metrics =================
st.markdown("<div class='section'>", unsafe_allow_html=True)

# First row
col1, col2, col3, col4 = st.columns(4)
with col1: st.markdown(f"<div class='metric-card'><h4>Total Scheduled Maintenances</h4><h2>{len(df)}</h2></div>", unsafe_allow_html=True)
with col2: st.markdown(f"<div class='metric-card'><h4>Avg Failure Risk</h4><h2>{df['failure_risk'].mean():.2%}</h2></div>", unsafe_allow_html=True)
with col3: st.markdown(f"<div class='metric-card'><h4>Max Failure Risk</h4><h2>{df['failure_risk'].max():.2%}</h2></div>", unsafe_allow_html=True)

# Second row
# col4, col5 = st.columns(2)
high_risk = df[df['failure_risk'] > 0.8]
# avg_health_score = (1 - df['failure_risk']).mean() * 100
with col4: st.markdown(f"<div class='metric-card'><h4>High-Risk Machines (>0.8)</h4><h2>{len(high_risk)}</h2></div>", unsafe_allow_html=True)
# with col5: st.markdown(f"<div class='metric-card'><h4>Avg Machine Health Score</h4><h2>{avg_health_score:.1f}%</h2></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= Failure Risk Distribution =================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("📊 Failure Risk Distribution")
fig1 = px.histogram(df, x="failure_risk", nbins=10,
                   title='Failure Risk Distribution',
                   labels={"failure_risk": "Failure Risk"},
                   color_discrete_sequence=['red'])
fig1.update_traces(marker_line_color='black', marker_line_width=1)
st.plotly_chart(fig1, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= Risk Categories =================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("📌 Risk Categories")
bins = [0,0.6,0.8,1.0]
labels = ["Low (0-0.6)","Medium (0.6-0.8)", "High (>0.8)"]
df["Risk_Level"] = pd.cut(df['failure_risk'], bins=bins, labels=labels, include_lowest=True)
risk_counts = df['Risk_Level'].value_counts().reset_index()
risk_counts.columns = ['Risk_Level', 'Count']
fig2 = px.bar(risk_counts, x='Risk_Level', y='Count',
              title='Failure Risk Categories',
              text='Count', color='Risk_Level',
              color_discrete_sequence=px.colors.qualitative.Set2)
fig2.update_traces(textposition='outside')
st.plotly_chart(fig2, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= Top Machines =================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🔥 Top 5 Risky Machines")
st.dataframe(df.nlargest(5, 'failure_risk')[['Product_ID', 'failure_risk']].reset_index(drop=True), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= Maintenance Schedule =================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🛠️ Scheduled Maintenance")
st.dataframe(df, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= High Risk Filter =================
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("🔎 High Risk Filter")
high_risk_slider = st.slider("Show machines with risk >=", 0.6, 1.0, 0.8)
filtered = df[df['failure_risk'] >= high_risk_slider][['Product_ID', 'failure_risk', 'scheduled_at']].reset_index(drop=True)
st.write(f"Machines with risk >= {high_risk_slider:.2f}: {len(filtered)}")
st.dataframe(filtered, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ================= End Note =================
st.markdown("<div class='section' style='text-align:center; font-weight:bold;'>✅ THE END — Dashboard Completed</div>", unsafe_allow_html=True)
