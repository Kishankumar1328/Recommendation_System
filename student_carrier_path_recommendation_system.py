import pandas as pd
import streamlit as st

# Read the CSV file
data = [
    ('Aeronautical Engineering', 'Aerospace Technology'),
    ('Aeronautical Engineering', 'Aircraft Design'),
    ('Aeronautical Engineering', 'Aerodynamics'),
    ('Aerospace Engineering', 'Aircraft Systems'),
    ('Aerospace Engineering', 'Spacecraft Design'),
    ('Aerospace Engineering', 'Propulsion Systems'),
    ('Architecture Engineering', 'Building Design'),
    ('Architecture Engineering', 'Construction Management'),
    ('Architecture Engineering', 'Sustainable Architecture'),
    ('Automobile Engineering', 'Automotive Design'),
    ('Automobile Engineering', 'Vehicle Dynamics'),
    ('Automobile Engineering', 'Emission Control'),
    ('Automation & Robotics Engg.', 'Robotic Systems'),
    ('Automation & Robotics Engg.', 'Automation Technology'),
    ('Automation & Robotics Engg.', 'Industrial Automation'),
    ('Avionics Engineering', 'Avionic Systems'),
    ('Avionics Engineering', 'Embedded Systems'),
    ('Avionics Engineering', 'Navigation Systems'),
    ('Bio Medical Engineering', 'Medical Devices'),
    ('Bio Medical Engineering', 'Biosensors'),
    ('Bio Medical Engineering', 'Biomaterials'),
    ('Bio Technology Engineering', 'Genetic Engineering'),
    ('Bio Technology Engineering', 'Bioprocess Technology'),
    ('Bio Technology Engineering', 'Bioinformatics'),
    ('Civil Engineering', 'Structural Design'),
    ('Civil Engineering', 'Construction Materials'),
    ('Civil Engineering', 'Transportation Engineering'),
    ('Chemical Engineering', 'Process Design'),
    ('Chemical Engineering', 'Reaction Engineering'),
    ('Chemical Engineering', 'Environmental Engineering'),
    ('Ceramic Engineering', 'Ceramic Materials'),
    ('Ceramic Engineering', 'Ceramic Processing'),
    ('Ceramic Engineering', 'Ceramic Applications'),
    ('Computer Science Engineering', 'Programming'),
    ('Computer Science Engineering', 'Algorithms'),
    ('Computer Science Engineering', 'Computer Networks'),
    ('Construction Mgmt & Tech Engg.', 'Project Management'),
    ('Construction Mgmt & Tech Engg.', 'Construction Technology'),
    ('Construction Mgmt & Tech Engg.', 'Building Information Modeling'),
    ('Electronics & Comm. Engg.', 'Communication Systems'),
    ('Electronics & Comm. Engg.', 'Signal Processing'),
    ('Electronics & Comm. Engg.', 'Microelectronics'),
    ('Electrical & Electronics Engg.', 'Power Systems'),
    ('Electrical & Electronics Engg.', 'Control Systems'),
    ('Electrical & Electronics Engg.', 'Renewable Energy'),
    ('Environmental Science Engg.', 'Waste Management'),
    ('Environmental Science Engg.', 'Air Pollution Control'),
    ('Environmental Science Engg.', 'Water Treatment'),
    ('Information Science Engg.', 'Data Analytics'),
    ('Information Science Engg.', 'Information Systems'),
    ('Information Science Engg.', 'Cybersecurity'),
    ('Industrial Engineering', 'Operations Research'),
    ('Industrial Engineering', 'Quality Control'),
    ('Industrial Engineering', 'Lean Manufacturing'),
    ('Industrial Production Engg.', 'Manufacturing Processes'),
    ('Industrial Production Engg.', 'Production Planning'),
    ('Industrial Production Engg.', 'Supply Chain Management'),
    ('Instrumentation Technology', 'Process Control'),
    ('Instrumentation Technology', 'Measurement Systems'),
    ('Instrumentation Technology', 'Industrial Automation'),
    ('Marine Engineering', 'Ship Design'),
    ('Marine Engineering', 'Marine Machinery'),
    ('Marine Engineering', 'Offshore Engineering'),
    ('Medical Electronics Engg.', 'Biomedical Instrumentation'),
    ('Medical Electronics Engg.', 'Medical Imaging'),
    ('Medical Electronics Engg.', 'Telemedicine'),
    ('Mechanical Engineering', 'Machine Design'),
    ('Mechanical Engineering', 'Thermal Engineering'),
    ('Mechanical Engineering', 'Mechatronics'),
    ('Mining Engineering', 'Mine Planning'),
    ('Mining Engineering', 'Rock Mechanics'),
    ('Mining Engineering', 'Mineral Processing'),
    ('Manufacturing Science Engg.', 'Advanced Manufacturing'),
    ('Manufacturing Science Engg.', 'Computer-Aided Manufacturing'),
    ('Manufacturing Science Engg.', 'Additive Manufacturing'),
    ('Naval Architecture', 'Ship Design'),
    ('Naval Architecture', 'Shipbuilding'),
    ('Naval Architecture', 'Offshore Structures'),
    ('Polymer Technology', 'Polymer Synthesis'),
    ('Polymer Technology', 'Polymer Processing'),
    ('Polymer Technology', 'Polymer Characterization'),
    ('Silk Technology Engineering', 'Silk Production'),
    ('Silk Technology Engineering', 'Silk Processing'),
    ('Silk Technology Engineering', 'Silk Product Development'),
    ('Carpet Technology Engineering', 'Carpet Design'),
    ('Carpet Technology Engineering', 'Carpet Manufacturing'),
    ('Carpet Technology Engineering', 'Carpet Testing'),
    ('Textile Engineering', 'Fiber Science'),
    ('Textile Engineering', 'Textile Processing'),
    ('Textile Engineering', 'Textile Product Development'),
    ('AI Engineering', 'Artificial Intelligence'),
    ('ML Engineering', 'Machine Learning'),
    ('Data Science Engineering', 'Data Science'),
    ('Data Science Engineering', 'Data Analysis'),
    ('Data Engineer', 'Big Data Processing'),
    ('Data Engineer', 'Data Warehousing'),
    ('Data Engineer', 'Database Management'),
    ('Data Science', 'Machine Learning'),
    ('Data Science', 'Statistical Analysis'),
    ('Data Science', 'Predictive Modeling'),
    ('Data Analysis', 'Data Interpretation'),
    ('Data Analysis', 'Statistical Analysis'),
    ('Data Analysis', 'Visualization')
]
df = pd.DataFrame(data, columns=['CourseName', 'Interest'])


# Function to build the recommendation system
def build_recommendation_system(dataframe):
    course_interest = dataframe.groupby(["CourseName", "Interest"]).size().reset_index(name='count')
    sorted_counts = course_interest.sort_values(by="count", ascending=False)
    recommendations = {}

    for course in sorted_counts["CourseName"].unique():
        top_interest = sorted_counts[sorted_counts["CourseName"] == course]["Interest"].values[0]
        recommendations[course] = top_interest

    return recommendations


# Function to get course recommendation for a given interest
def get_course_for_interest(interest, recommendations):
    if interest in recommendations.values():
        course = [key for key, value in recommendations.items() if value == interest][0]
        return course
    else:
        return "No recommendations for this interest."


# Build recommendations
recommendations = build_recommendation_system(df)

# Streamlit web application
st.title("Course Recommendation System")

# User input for interest using a text_input widget
user_interest = st.text_input("Enter your interest:")

# Button to trigger the recommendation
if st.button("Get Recommendation"):
    # Get the corresponding course recommendation
    course_recommendation = get_course_for_interest(user_interest, recommendations)

    # Display the recommendation dynamically
    st.write(f"Recommended course for interest '{user_interest}': {course_recommendation}")
