def create_recommendations(insights):
    recommendations = []

    # Recommend focusing on weak topics
    if 'weak_topics' in insights and not insights['weak_topics'].empty:
        recommendations.append("Focus on improving your understanding of the following topics:")
        for topic in insights['weak_topics'].index:
            recommendations.append(f" - {topic}")

    # Recommend practicing more questions of specific difficulty levels
    if 'performance_gaps' in insights and not insights['performance_gaps'].empty:
        recommendations.append("\nPractice more questions of the following difficulty levels:")
        for level in insights['performance_gaps'].index:
            recommendations.append(f" - Difficulty level: {level}")

    # Recommend focusing on improving accuracy for specific topics
    if 'response_accuracy' in insights and not insights['response_accuracy'].empty:
        recommendations.append("\nWork on improving your accuracy for questions related to the following topics:")
        low_accuracy_topics = insights['response_accuracy'][insights['response_accuracy']['correct_answers'] < 0.5]
        for topic in low_accuracy_topics.index:
            recommendations.append(f" - {topic}")

    return recommendations
def extract_quiz_info(row, key):
    """
    Helper function to extract information from nested 'quiz' column.
    """
    quiz_info = row.get('quiz', {})
    return quiz_info.get(key, None) if isinstance(quiz_info, dict) else None
def analyze_student_persona(historical_quiz_df):
    persona = {}

    # Extract topic and difficulty information from the nested 'quiz' column
    historical_quiz_df['difficulty_level'] = historical_quiz_df.apply(extract_quiz_info, axis=1, key='difficulty_level')
    historical_quiz_df['topic'] = historical_quiz_df.apply(extract_quiz_info, axis=1, key='title')

    # Define thresholds for strengths and weaknesses
    strength_threshold = 80
    weakness_threshold = 50

    # Identify strengths
    strengths = historical_quiz_df[historical_quiz_df['score'] > strength_threshold]
    strengths_by_topic = strengths['topic'].value_counts().index.tolist()
    strengths_by_difficulty = strengths['difficulty_level'].value_counts().index.tolist()

    # Identify weaknesses
    weaknesses = historical_quiz_df[historical_quiz_df['score'] < weakness_threshold]
    weaknesses_by_topic = weaknesses['topic'].value_counts().index.tolist()
    weaknesses_by_difficulty = weaknesses['difficulty_level'].value_counts().index.tolist()

    # Summarize the persona
    persona['strengths'] = {
        'topics': strengths_by_topic,
        'difficulty_levels': strengths_by_difficulty
    }
    persona['weaknesses'] = {
        'topics': weaknesses_by_topic,
        'difficulty_levels': weaknesses_by_difficulty
    }

    return persona