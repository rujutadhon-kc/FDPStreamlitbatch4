import streamlit as st
import pandas as pd

st.title("Student Marks and Grade App")

# Number of subjects
subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=10, value=3)

marks = []

# Taking marks input
for i in range(subjects):
    mark = st.number_input(f"Enter marks for subject {i+1} (out of 100):", 
                           min_value=0, max_value=100, value=0, key=f"mark_{i}")
    marks.append(mark)

# Calculate button (OUTSIDE the loop)
if st.button("Calculate Grade"):
    total_marks = sum(marks)
    per_marks = total_marks / (subjects * 100) * 100

    st.write(f"### Total Marks: {total_marks}")
    st.write(f"### Percentage: {per_marks:.2f}%")

    # Grade logic
    if per_marks >= 90:
        st.success("Grade: A+")
    elif per_marks >= 80:
        st.success("Grade: A")
    elif per_marks >= 70:
        st.success("Grade: B+")
    elif per_marks >= 60:
        st.success("Grade: B")
    elif per_marks >= 50:
        st.success("Grade: C")
    else:
        st.error("Grade: F")
