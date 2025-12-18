def generate_summary(risk_df, chapter_df):
    """
    Generates human-readable insights for admins and mentors
    """
    summary = {}

    summary['high_risk_students_count'] = len(risk_df)
    summary['most_difficult_chapter'] = chapter_df.sort_values('completed').head(1).index.tolist()

    return summary

