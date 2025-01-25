import pandas as pd
from data_analysis import analyze_quiz_data
from insights_generation import generate_insights
from recommendations import create_recommendations, analyze_student_persona

def load_data(filename):
    return pd.read_json(filename)

def main():
    # Load data
    current_quiz_df = load_data("../data/current_quiz_data.json")
    quiz_submission_df = load_data("../data/quiz_submission_data.json")
    historical_quiz_df = load_data("../data/historical_quiz_data.json")

    # Analyze data
    topic_performance, difficulty_performance, response_accuracy = analyze_quiz_data(current_quiz_df, historical_quiz_df)

    # Generate insights
    insights = generate_insights(topic_performance, difficulty_performance, response_accuracy)

    # Create recommendations
    recommendations = create_recommendations(insights)
    for rec in recommendations:
        print(rec)

    # Analyze student persona
    student_persona = analyze_student_persona(historical_quiz_df)
    print("Strengths:", student_persona['strengths'])
    print("Weaknesses:", student_persona['weaknesses'])

if __name__ == "__main__":
    main()