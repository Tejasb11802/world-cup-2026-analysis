import pandas as pd
import os
from pathlib import Path

def load_youtube_data():
    """Load YouTube data from CSV"""
    file_path = 'data/raw/youtube_videos.csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return None
    
    df = pd.read_csv(file_path)
    return df

def calculate_kpis(df):
    """Calculate Key Performance Indicators"""
    if df is None or len(df) == 0:
        return None
    
    kpis = {
        'Total Videos': len(df),
        'Total Views': df['views'].sum(),
        'Total Likes': df['likes'].sum(),
        'Total Comments': df['comments'].sum(),
        'Average Views per Video': df['views'].mean(),
        'Average Likes per Video': df['likes'].mean(),
        'Average Comments per Video': df['comments'].mean(),
        'Total Engagements': df['likes'].sum() + df['comments'].sum(),
    }
    
    return kpis

def calculate_social_value(df, cpe=0.95):
    """Calculate social value based on engagements"""
    total_engagements = df['likes'].sum() + df['comments'].sum()
    social_value = total_engagements * cpe
    return social_value

def calculate_sponsor_value(df, cpm=4.0):
    """Calculate estimated sponsor brand value"""
    total_views = df['views'].sum()
    sponsor_value = (total_views * cpm) / 1000
    return sponsor_value

def analyze_content_performance(df):
    """Analyze which videos performed best"""
    df_sorted = df.sort_values('views', ascending=False)
    top_videos = df_sorted.head(3)[['title', 'views', 'likes', 'comments']]
    return top_videos

def save_kpi_report(kpis, social_value, sponsor_value):
    """Save KPIs to a report file"""
    os.makedirs('data/processed', exist_ok=True)
    
    report_file = 'data/processed/kpi_report.txt'
    with open(report_file, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("WORLD CUP 2026 ANALYSIS - KPI REPORT\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("ENGAGEMENT METRICS\n")
        f.write("-" * 60 + "\n")
        for key, value in kpis.items():
            if isinstance(value, float):
                f.write(f"{key}: {value:,.0f}\n")
            else:
                f.write(f"{key}: {value:,}\n")
        
        f.write("\nVALUE METRICS\n")
        f.write("-" * 60 + "\n")
        f.write(f"Total Social Value (CPE=$0.95): ${social_value:,.2f}\n")
        f.write(f"Total Sponsor Value (CPM=$4): ${sponsor_value:,.2f}\n")
        
    print(f"KPI report saved to {report_file}")

def run_analysis():
    """Run complete analysis"""
    print("Loading YouTube data...")
    df = load_youtube_data()
    
    if df is None:
        return
    
    print("Calculating KPIs...")
    kpis = calculate_kpis(df)
    
    print("Calculating social value...")
    social_value = calculate_social_value(df)
    
    print("Calculating sponsor value...")
    sponsor_value = calculate_sponsor_value(df)
    
    print("Analyzing content performance...")
    top_videos = analyze_content_performance(df)
    
    print("Saving report...")
    save_kpi_report(kpis, social_value, sponsor_value)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"\nTotal Videos: {kpis['Total Videos']}")
    print(f"Total Views: {kpis['Total Views']:,}")
    print(f"Total Engagements: {kpis['Total Engagements']:,}")
    print(f"Social Value: ${social_value:,.2f}")
    print(f"Sponsor Value: ${sponsor_value:,.2f}")
    print(f"\nTop 3 Videos:")
    print(top_videos.to_string(index=False))

if __name__ == '__main__':
    run_analysis()