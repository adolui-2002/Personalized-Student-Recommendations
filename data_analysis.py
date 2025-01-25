import pandas as pd

def extract_quiz_info(row, key):
    """
    Helper function to extract information from nested 'quiz' column.
    """
    quiz_info = row.get('quiz', {})
    return quiz_info.get(key, None) if isinstance(quiz_info, dict) else None

def analyze_quiz_data(current_quiz_df, historical_quiz_df):
    # Extract 'difficulty_level' and 'topic' from 'quiz' column
    historical_quiz_df['difficulty_level'] = historical_quiz_df.apply(extract_quiz_info, axis=1, key='difficulty_level')
    historical_quiz_df['topic'] = historical_quiz_df.apply(extract_quiz_info, axis=1, key='title')

    # Analyze performance by topics
    topic_performance = historical_quiz_df.groupby('topic').agg({'score': 'mean'})

    # Analyze performance by difficulty levels
    difficulty_performance = historical_quiz_df.groupby('difficulty_level').agg({'score': 'mean'})

    # Analyze response accuracy
    response_accuracy = historical_quiz_df.groupby('id').agg({'correct_answers': 'mean'})  # Using 'id' as 'question_id' is not available

    return topic_performance, difficulty_performance, response_accuracy