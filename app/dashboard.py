import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Page config
st.set_page_config(
    page_title="World Cup 2026 Analysis",
    page_icon="⚽",
    layout="wide"
)

# Title
st.title("⚽ 2026 FIFA World Cup Intelligence Report")
st.markdown("Social Media, Broadcast & Sponsor Performance Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/raw/youtube_videos.csv')
    return df

# Load KPI report
@st.cache_data
def load_kpi_report():
    try:
        with open('data/processed/kpi_report.txt', 'r') as f:
            return f.read()
    except:
        return "KPI report not found"

# Load data
df = load_data()

# Calculate metrics
total_videos = len(df)
total_views = df['views'].sum()
total_engagements = df['likes'].sum() + df['comments'].sum()
social_value = total_engagements * 0.95

# Display KPI Cards
st.markdown("## Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Posts", f"{total_videos:,}")

with col2:
    st.metric("Total Views", f"{total_views:,.0f}")

with col3:
    st.metric("Total Engagements", f"{total_engagements:,.0f}")

with col4:
    st.metric("Social Value", f"${social_value:,.0f}")

st.markdown("---")

# Section 1: Social Media Performance
st.markdown("## Social Media Performance Overview")
col1, col2 = st.columns(2)

with col1:
    # Views distribution
    fig_views = px.bar(
        df.sort_values('views', ascending=False),
        x='title',
        y='views',
        title='Views by Video',
        labels={'views': 'Views', 'title': 'Video Title'},
        color='views',
        color_continuous_scale='Reds'
    )
    fig_views.update_layout(height=400, showlegend=False)
    fig_views.update_xaxes(tickangle=45)
    st.plotly_chart(fig_views, use_container_width=True)

with col2:
    # Engagement distribution
    df['total_engagement'] = df['likes'] + df['comments']
    fig_engagement = px.bar(
        df.sort_values('total_engagement', ascending=False),
        x='title',
        y='total_engagement',
        title='Engagement by Video (Likes + Comments)',
        labels={'total_engagement': 'Engagement', 'title': 'Video Title'},
        color='total_engagement',
        color_continuous_scale='Blues'
    )
    fig_engagement.update_layout(height=400, showlegend=False)
    fig_engagement.update_xaxes(tickangle=45)
    st.plotly_chart(fig_engagement, use_container_width=True)

st.markdown("---")

# Section 2: Top Videos
st.markdown("## Top Performing Videos")
top_videos = df.sort_values('views', ascending=False).head(5)
video_table = top_videos[['title', 'channel', 'views', 'likes', 'comments']].copy()
video_table['total_engagement'] = video_table['likes'] + video_table['comments']
video_table = video_table[['title', 'channel', 'views', 'likes', 'comments', 'total_engagement']]
video_table.columns = ['Title', 'Channel', 'Views', 'Likes', 'Comments', 'Total Engagement']

st.dataframe(video_table, use_container_width=True)

st.markdown("---")

# Section 3: Channel Performance
st.markdown("## Performance by Channel")
channel_stats = df.groupby('channel').agg({
    'views': 'sum',
    'likes': 'sum',
    'comments': 'sum',
    'video_id': 'count'
}).reset_index()
channel_stats.columns = ['Channel', 'Total Views', 'Total Likes', 'Total Comments', 'Video Count']
channel_stats['Engagement Rate'] = ((channel_stats['Total Likes'] + channel_stats['Total Comments']) / channel_stats['Total Views'] * 100).round(2)

fig_channel = px.bar(
    channel_stats,
    x='Channel',
    y='Total Views',
    title='Total Views by Channel',
    color='Total Views',
    color_continuous_scale='Viridis'
)
fig_channel.update_layout(height=400)
st.plotly_chart(fig_channel, use_container_width=True)

st.dataframe(channel_stats, use_container_width=True)

st.markdown("---")

# Section 4: Engagement Metrics
st.markdown("## Engagement Analysis")
col1, col2 = st.columns(2)

with col1:
    avg_engagement_rate = ((total_engagements / total_views) * 100)
    st.metric("Average Engagement Rate", f"{avg_engagement_rate:.2f}%")

with col2:
    avg_views_per_video = total_views / total_videos
    st.metric("Average Views per Video", f"{avg_views_per_video:,.0f}")

st.markdown("---")

# Section 5: Methodology
st.markdown("## Methodology & Data Sources")
st.info("""
**Data Collection:**
- Social media data sourced from official team and player accounts
- YouTube videos analyzed for views, likes, and comments
- All metrics based on publicly available data

**Analysis Methods:**
- Engagement Rate = (Likes + Comments) / Views × 100
- Social Value = Total Engagements × $0.95 (Cost Per Engagement)
- Sponsor Value = Total Views × $4 CPM / 1000

**Data Quality:**
- All figures are based on sample data for demonstration purposes
- Methodology is production-ready and scalable to real data

**Key Assumptions:**
- CPE (Cost Per Engagement): $0.95
- CPM (Cost Per Thousand Impressions): $4.00
- These are conservative estimates for sports content
""")

st.markdown("---")

# Footer
st.markdown("""
---
**World Cup 2026 Analysis Dashboard** | Built with Streamlit | Data: Sample YouTube Metrics
""")