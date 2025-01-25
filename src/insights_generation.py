def generate_insights(topic_performance, difficulty_performance, response_accuracy):
    insights = {}

    # Identify weak areas (score < 50)
    weak_topics = topic_performance[topic_performance['score'] < 50]

    # Identify improvement trends (positive percentage change in score)
    improving_topics = topic_performance[topic_performance['score'].pct_change() > 0]

    # Identify performance gaps (score < 50)
    performance_gaps = difficulty_performance[difficulty_performance['score'] < 50]

    # Identify low accuracy (correct_answers < 0.5)
    low_accuracy = response_accuracy[response_accuracy['correct_answers'] < 0.5]

    insights['weak_topics'] = weak_topics
    insights['improving_topics'] = improving_topics
    insights['performance_gaps'] = performance_gaps
    insights['response_accuracy'] = low_accuracy

    return insights