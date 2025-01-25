# main.py
import pandas as pd
import json
from data_analysis import analyze_quiz_data
from insights_generation import generate_insights
from recommendations import create_recommendations, analyze_student_persona
from visualize import visualize_performance  # Import the visualization function

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    # Transform data if it is a dictionary of dictionaries
    if isinstance(data, dict):
        data = list(data.values())

    return pd.DataFrame(data)

def print_insights(insights):
    print("Insights:")

    # Print weak topics
    if 'weak_topics' in insights and not insights['weak_topics'].empty:
        print("\nWeak Topics:")
        for topic, row in insights['weak_topics'].iterrows():
            print(f" - {topic}: Average Score = {row['score']:.2f}")

    # Print improving topics
    if 'improving_topics' in insights and not insights['improving_topics'].empty:
        print("\nImproving Topics:")
        for topic, row in insights['improving_topics'].iterrows():
            print(f" - {topic}: Average Score = {row['score']:.2f}")

    # Print performance gaps
    if 'performance_gaps' in insights and not insights['performance_gaps'].empty:
        print("\nPerformance Gaps:")
        for level, row in insights['performance_gaps'].iterrows():
            print(f" - Difficulty Level {level}: Average Score = {row['score']:.2f}")

    # Print response accuracy
    if 'response_accuracy' in insights and not insights['response_accuracy'].empty:
        print("\nResponse Accuracy Issues:")
        for topic, row in insights['response_accuracy'].iterrows():
            print(f" - {topic}: Correct Answers = {row['correct_answers']:.2f}")

def main():
    # Load data
    current_quiz_df = load_data("../data/current_quiz_data.json")
    quiz_submission_df = load_data("../data/quiz_submission_data.json")
    historical_quiz_df = load_data("../data/historical_quiz_data.json")

    # Print first few rows of the DataFrame to verify its structure
    print("Current Quiz Data Columns:", current_quiz_df.columns)
    print("\nQuiz Submission Data Columns:", quiz_submission_df.columns)
    print("\nHistorical Quiz Data Columns:", historical_quiz_df.columns)

    print("\nCurrent Quiz Data:")
    print(current_quiz_df.head())
    print("\nQuiz Submission Data:")
    print(quiz_submission_df.head())
    print("\nHistorical Quiz Data:")
    print(historical_quiz_df.head())

    # Analyze data
    topic_performance, difficulty_performance, response_accuracy = analyze_quiz_data(current_quiz_df, historical_quiz_df)

    # Generate insights
    insights = generate_insights(topic_performance, difficulty_performance, response_accuracy)

    # Print insights
    print_insights(insights)

    # Create recommendations
    recommendations = create_recommendations(insights)
    print("\nRecommendations:")
    for rec in recommendations:
        print(rec)

    # Analyze student persona and print it
    student_persona = analyze_student_persona(historical_quiz_df)
    print("\nStudent Persona:")
    print("Strengths by Topics:", student_persona['strengths']['topics'])
    print("Strengths by Difficulty Levels:", student_persona['strengths']['difficulty_levels'])
    print("Weaknesses by Topics:", student_persona['weaknesses']['topics'])
    print("Weaknesses by Difficulty Levels:", student_persona['weaknesses']['difficulty_levels'])

    # Visualize performance
    visualize_performance(topic_performance)

if __name__ == "__main__":
    main()