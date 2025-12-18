def chapter_difficulty(df):
    """
    Identifies difficult chapters using completion rate, time spent, and scores
    """
    return df.groupby('chapter').agg({
        'time_spent': 'mean',
        'score': 'mean',
        'completed': 'mean'
    })

