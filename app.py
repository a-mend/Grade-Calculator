import streamlit as st

# Set up the page title and icon
st.set_page_config(page_title="Grade Weight Calculator", page_icon="🎓")

st.title("🎓 Course Grade Weight Calculator")
st.write("Dynamically adjust your syllabus weights and calculate your final grade.")

st.markdown("---")

# 1. Dynamic Assessment Setup
st.subheader("🛠️ Step 1: Define Weights")
st.info("Ensure the total weight equals exactly 100%.")

# Create columns for inputs
col1, col2 = st.columns(2)

with col1:
    # Editable category names
    cat1 = st.text_input("Category 1 Name", "Final Exam")
    cat2 = st.text_input("Category 2 Name", "Midterm")
    cat3 = st.text_input("Category 3 Name", "Attendance")
    cat4 = st.text_input("Category 4 Name", "Homework")

with col2:
    # Editable weight percentages
    w1 = st.number_input(f"{cat1} Weight (%)", min_value=0, max_value=100, value=30)
    w2 = st.number_input(f"{cat2} Weight (%)", min_value=0, max_value=100, value=30)
    w3 = st.number_input(f"{cat3} Weight (%)", min_value=0, max_value=100, value=20)
    w4 = st.number_input(f"{cat4} Weight (%)", min_value=0, max_value=100, value=20)

total_weight = w1 + w2 + w3 + w4

# Show a warning or success message based on total weight
if total_weight == 100:
    st.success(f"Total Weight: {total_weight}% (Perfect!)")
else:
    st.error(f"Total Weight: {total_weight}%. It must equal 100% to calculate correctly.")

st.markdown("---")

# 2. Score Inputs
st.subheader("📝 Step 2: Enter Your Grades")

col3, col4 = st.columns(2)

with col3:
    g1 = st.number_input(f"Your {cat1} Score (%)", min_value=0.0, max_value=100.0, value=85.0)
    g2 = st.number_input(f"Your {cat2} Score (%)", min_value=0.0, max_value=100.0, value=78.0)

with col4:
    g3 = st.number_input(f"Your {cat3} Score (%)", min_value=0.0, max_value=100.0, value=100.0)
    g4 = st.number_input(f"Your {cat4} Score (%)", min_value=0.0, max_value=100.0, value=92.0)

st.markdown("---")

# 3. Calculation Logic
st.subheader("📊 Step 3: Final Result")

if total_weight == 100:
    # Calculate weighted grade
    final_grade = ((g1 * w1) + (g2 * w2) + (g3 * w3) + (g4 * w4)) / 100
    
    # Display final score with metric visualization
    st.metric(label="Calculated Final Grade", value=f"{final_grade:.2f}%")
    
    # Quick letter grade logic
    if final_grade >= 90:
        st.balloons()
        st.success("Letter Grade: A")
    elif final_grade >= 80:
        st.success("Letter Grade: B")
    elif final_grade >= 70:
        st.warning("Letter Grade: C")
    elif final_grade >= 60:
        st.warning("Letter Grade: D")
    else:
        st.error("Letter Grade: F")
else:
    st.warning("Please adjust your weights to sum up to 100% to see your final grade.")
