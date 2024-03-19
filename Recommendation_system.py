import pandas as pd

df = pd.read_csv("/content/carrier path2.csv")

def build_recommendation_system(dataframe):
    course_interest = dataframe.groupby(["CourseName", "Interest"]).size().reset_index(name='count')
    sorted_counts = course_interest.sort_values(by="count", ascending=False)
    recommendations = {}

    for course in sorted_counts["CourseName"].unique():
        top_interest = sorted_counts[sorted_counts["CourseName"] == course]["Interest"].values[0]
        recommendations[course] = top_interest

    return recommendations

def get_course_for_interest(interest, recommendations):
    # Check if the interest is present in recommendations
    if interest in recommendations.values():
        course = [key for key, value in recommendations.items() if value == interest][0]
        return course
    else:
        return "No recommendations for this interest."

# Build recommendations
recommendations = build_recommendation_system(df)

# Get input from the user
user_interest = input("Enter your interest: ")

# Get the corresponding course recommendation
course_recommendation = get_course_for_interest(user_interest, recommendations)
print(f"Recommended course for interest '{user_interest}': {course_recommendation}")
