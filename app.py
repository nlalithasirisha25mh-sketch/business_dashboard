import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Business & Operations Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Mock Data Generator / Loader
@st.cache_data(ttl=3600)
def load_data():
    """Generates synthetic data representing operational, rental, and sales metrics."""
    np.random.seed(42)
    dates = pd.date_range(start="2025-01-01", periods=180, freq="D")
    
    categories = ["Commercial", "Residential", "Retail", "Industrial"]
    regions = ["North", "South", "East", "West"]
    
    data = {
        "Date": np.random.choice(dates, size=500),
        "Category": np.random.choice(categories, size=500),
        "Region": np.random.choice(regions, size=500),
        "Rent_Revenue": np.random.uniform(1500, 8500, size=500),
        "Operating_Cost": np.random.uniform(500, 3000, size=500),
        "Occupancy_Rate": np.random.uniform(0.65, 0.99, size=500),
    }
    df = pd.DataFrame(data)
    df["Net_Income"] = df["Rent_Revenue"] - df["Operating_Cost"]
    df["Date"] = pd.to_datetime(df["Date"])
    return df.sort_values("Date")

df_raw = load_data()

# 3. Sidebar Navigation & Filtering Pipeline
st.sidebar.title("Navigation & Filters")

view_mode = st.sidebar.radio(
    "Select Dashboard View:",
    options=["Executive Overview", "Rent & Property Analytics", "Operations & Cost Breakdown"],
    index=1  # Default to Rent Analytics based on your anchor
)

st.sidebar.markdown("---")
st.sidebar.subheader("Filter Pipeline")

selected_regions = st.sidebar.multiselect(
    "Filter by Region:",
    options=df_raw["Region"].unique(),
    default=df_raw["Region"].unique(),
)

selected_categories = st.sidebar.multiselect(
    "Filter by Category:",
    options=df_raw["Category"].unique(),
    default=df_raw["Category"].unique(),
)

# Apply dynamic query filtering
df_filtered = df_raw[
    (df_raw["Region"].isin(selected_regions)) &
    (df_raw["Category"].isin(selected_categories))
]

# 4. Main Content Rendering

if view_mode == "Executive Overview":
    st.title("Executive Performance Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    total_rev = df_filtered["Rent_Revenue"].sum()
    total_cost = df_filtered["Operating_Cost"].sum()
    net_income = df_filtered["Net_Income"].sum()
    avg_occ = df_filtered["Occupancy_Rate"].mean() * 100

    col1.metric("Total Revenue", f"${total_rev:,.2f}", "+8.4%")
    col2.metric("Operating Cost", f"${total_cost:,.2f}", "-2.1%")
    col3.metric("Net Income", f"${net_income:,.2f}", "+11.2%")
    col4.metric("Avg Occupancy", f"{avg_occ:.1f}%", "+1.5%")

    st.markdown("---")
    
    fig_overview = px.line(
        df_filtered.groupby("Date")[["Rent_Revenue", "Net_Income"]].sum().reset_index(),
        x="Date",
        y=["Rent_Revenue", "Net_Income"],
        title="Revenue vs. Net Income Trends",
        labels={"value": "Amount ($)", "variable": "Metric"},
        template="plotly_white"
    )
    st.plotly_chart(fig_overview, use_container_width=True)

elif view_mode == "Rent & Property Analytics":
    st.title("🏠 Rent & Leasing Analytics")
    st.caption("Deep-dive tracking of rental yield, occupancy rates, and segment breakdowns.")

    # High-level Rent KPIs
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Gross Rental Revenue", f"${df_filtered['Rent_Revenue'].sum():,.2f}")
    kpi2.metric("Median Rent per Asset", f"${df_filtered['Rent_Revenue'].median():,.2f}")
    kpi3.metric("Portfolio Occupancy", f"{(df_filtered['Occupancy_Rate'].mean() * 100):.2f}%")

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        fig_cat = px.bar(
            df_filtered.groupby("Category")["Rent_Revenue"].sum().reset_index(),
            x="Category",
            y="Rent_Revenue",
            color="Category",
            title="Revenue Distribution by Category",
            template="plotly_white"
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    with col_chart2:
        fig_scatter = px.scatter(
            df_filtered,
            x="Occupancy_Rate",
            y="Rent_Revenue",
            color="Region",
            size="Net_Income",
            hover_data=["Category"],
            title="Occupancy vs. Rent Realization",
            template="plotly_white"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Raw Asset Records")
    st.dataframe(
        df_filtered[["Date", "Region", "Category", "Rent_Revenue", "Operating_Cost", "Occupancy_Rate"]],
        use_container_width=True
    )

elif view_mode == "Operations & Cost Breakdown":
    st.title("Operational & Expense Breakdown")
    
    fig_cost = px.box(
        df_filtered,
        x="Category",
        y="Operating_Cost",
        color="Region",
        title="Operating Cost Distribution across Verticals",
        template="plotly_white"
    )
    st.plotly_chart(fig_cost, use_container_width=True)
