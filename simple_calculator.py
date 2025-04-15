import streamlit

streamlit.title('calculator')

num1 = streamlit.number_input('Enter your first number:')
num2 = streamlit.number_input('Enter your second number:')
operation = streamlit.selectbox('Choose operation: ', ["+", "-", "*", "/"])

if streamlit.button("Calculate"):
    if operation == "+":
        streamlit.write("Result: ", num1 + num2)
    elif operation == "-":
        streamlit.write("Result: ", num1 - num2)
    elif operation == "*":
        streamlit.write("Result: ", num1 * num2)
    elif operation == "/":
        streamlit.write("Result: ", num1 / num2)