def detect_risk(df):
    """
    Identifies high-risk students based on low engagement and low performance
    """
    return df[(df['avg_time'] < 20) & (df['avg_score'] < 40)]

