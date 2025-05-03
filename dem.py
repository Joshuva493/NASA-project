import streamlit as st 


st.title("NASA PROJECT")


st.write("Hello, this is my project 1")


st.selectbox("select an option", ["Count how many times each asteroid has approached Earth",
                                   "Average velocity of each asteroid over multiple approaches",
                                    "List top 10 fastest asteroids",
                                    "Find potentially hazardous asteroids that have approached Earth more than 3 times",
                                    "find the month with the most asteroid approaches",
                                     "Get the asteroid with the fastest ever approach speed",
                                     "sort asteroids by maximum estimated diameter (descending)",
                                     "Asteroids whose closest approach is getting nearer over time(Hint: Use ORDER BY close_approach_date and look at miss_distance)",
                                     "Display the name of each asteroid along with the date and miss distance of its closest approach to Earth.",
                                     "List names of asteroids that approached Earth with velocity > 50,000 km/h",
                                     "Count how many approaches happened per month",
                                     "Find asteroid with the highest brightness (lowest magnitude value)",
                                     "Get number of hazardous vs non-hazardous asteroids",
                                     "Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.",
                                     "Find asteroids that came within 0.05 AU(astronomical distance)",
                                     "Find asteroids that have approached Earth within a certain distance in the last 10 years",
                                     "Calculate the average miss distance for asteroids grouped by estimated diameter ranges",
                                     "Analyze the trend of asteroid approaches over the past few years, grouped by month and estimated diameter range",
                                     "List the top 10 largest asteroids by estimated diameter and their closest approach distance",
                                     "Count the number of asteroids discovered by each program, grouped by year"])


button = st.button("Submit")


if button:
    st.success("Done")


if st.checkbox('Accepted'):
    st.write('Thank you.')









