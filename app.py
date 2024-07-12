import streamlit as st

st.header('define Number type apps', divider='red')
st.write('ini adalah aplikasi untuk menentukan bilangan genap atau bilangan ganjil')

number = st.number_input("insert a number")
st.write("The current number is", number)

import streamlit as st

st.header('Define Number Type Apps', divider='red')
st.write('Ini adalah aplikasi untuk menentukan bilangan genap atau bilangan ganjil')

number = st.number_input("Insert a number", value=0)
st.write("The current number is", number)

if number % 2 == 0:
    st.write("The number is bilangan genap.")
else:
    st.write("The number is bilangan ganjil.")

import streamlit as st

st.header('Number Type and Multiplication App', divider='red')
st.write('Ini adalah aplikasi untuk menentukan bilangan genap atau bilangan ganjil dan melakukan perkalian dua angka.')

# Input for first number
number1 = st.number_input("Insert the first number", value=0)
st.write("The first number is", number1)

# Input for second number
number2 = st.number_input("Insert the second number", value=0)
st.write("The second number is", number2)

# Determine if the first number is bilangan genap or bilangan ganjil
if number1 % 2 == 0:
    st.write("The first number is bilangan genap.")
else:
    st.write("The first number is bilangan ganjil.")

# Determine if the second number is bilangan genap or bilangan ganjil
if number2 % 2 == 0:
    st.write("The second number is bilangan genap.")
else:
    st.write("The second number is bilangan ganji.")

# Perform multiplication
result = number1 * number2
st.write("The result of multiplication is", result)

# Determine if the result is bilangan genap or bilangan ganji
if result % 2 == 0:
    st.write("The result is bilangan genap.")
else:
    st.write("The result is bilangan ganji.")