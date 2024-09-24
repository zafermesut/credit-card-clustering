import streamlit as st
from joblib import load
import plotly.graph_objects as go
import numpy as np
import pandas as pd

kmeans = load("model.joblib")
df = pd.read_csv("data/credit_card_segments.csv")

st.title("Credit Card Clustering App")

balance = st.number_input("Enter Balance:", min_value=0.0)
purchases = st.number_input("Enter Purchases:", min_value=0.0)
credit_limit = st.number_input("Enter Credit Limit:", min_value=0.0)

new_data = np.array([[balance, purchases, credit_limit]])

if st.button("Find Cluster"):
    cluster = kmeans.predict(new_data)
    st.write(f"The data belongs to cluster: Cluster {cluster[0] + 1}")

    PLOT = go.Figure()

    for i in list(df["CREDIT_CARD_SEGMENTS"].unique()):
        PLOT.add_trace(go.Scatter3d(
            x = df[df["CREDIT_CARD_SEGMENTS"] == i]['BALANCE'],
            y = df[df["CREDIT_CARD_SEGMENTS"] == i]['PURCHASES'],
            z = df[df["CREDIT_CARD_SEGMENTS"] == i]['CREDIT_LIMIT'],
            mode = 'markers',
            marker=dict(size=6, line=dict(width=1)),
            name = f'Cluster {i}'
        ))

    PLOT.add_trace(go.Scatter3d(
        x=[balance],
        y=[purchases],
        z=[credit_limit],
        mode='markers',
        marker=dict(size=10, color='yellow', line=dict(width=2)),
        name='New Data'
    ))

    PLOT.update_traces(hovertemplate='BALANCE: %{x} <br>PURCHASES %{y} <br>CREDIT_LIMIT: %{z}')
    PLOT.update_layout(
        width=800, height=800, autosize=True, showlegend=True,
        scene=dict(
            xaxis=dict(title='BALANCE', titlefont_color='black'),
            yaxis=dict(title='PURCHASES', titlefont_color='black'),
            zaxis=dict(title='CREDIT_LIMIT', titlefont_color='black')
        ),
        font=dict(family="Gilroy", color='black', size=12)
    )

    st.plotly_chart(PLOT)