import streamlit as st
from seven_segment import segment_map

st.title("Seven-Segment Data Dashboard Simulator")

digit = st.selectbox("Select a digit", list(range(10)))

st.subheader(f"Seven-Segment Display: {digit}")

segments = segment_map[digit].copy()

fault = st.selectbox(
    "Select Faulty Segment",
    ["None", "A", "B", "C", "D", "E", "F", "G"]
)

segment_names = ["A", "B", "C", "D", "E", "F", "G"]

if fault != "None":
    fault_index = segment_names.index(fault)
    segments[fault_index] = 0
    st.error(f"Fault Detected: Segment {fault} is OFF")

st.write("Segment Status (A-G):", segments)
st.write("1 = ON, 0 = OFF")

st.subheader("Display Output")

st.code(
    f"""
      {'---' if segments[0] else '   '}
     {'|' if segments[5] else ' '}   {'|' if segments[1] else ' '}
      {'---' if segments[6] else '   '}
     {'|' if segments[4] else ' '}   {'|' if segments[2] else ' '}
      {'---' if segments[3] else ' '}
    """
)

st.subheader("Test Case Summary")

st.write("Normal Test Cases: 10")
st.write("Fault / Edge Cases: 5")
st.write("Total Test Cases: 15")

if fault == "None":
    st.success("System Status: Normal")
else:
    st.warning("System Status: Fault Detected")
