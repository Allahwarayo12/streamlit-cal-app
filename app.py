import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

# User input
st.write("Enter two numbers and select an operation:")
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate result
result = None
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Division by zero is not allowed!")

# Display result
if result is not None:
    st.success(f"✅ Result: {result}")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
