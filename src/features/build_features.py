def build_features(df):
    df['avg_time'] = df.groupby('student_id')['time_spent'].transform('mean')
    df['avg_score'] = df.groupby('student_id')['score'].transform('mean')
    return df[['avg_time', 'avg_score', 'completed']]

