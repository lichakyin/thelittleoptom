import streamlit as st
import random
from datetime import datetime
import plotly
import plotly.graph_objects as go
import pandas as pd
import re

st.set_page_config(page_title='Binocular Vision', page_icon=':bar_chart:', layout='centered')

# Define the sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Go to', ('Home Page', 'Myopia Control Calculator: Axial Length', 'W4dot', 'Hart Chart', 'Accommodation Facility Training', 'Red Blue Circular Pong', 'Red Blue Space Asteroids', 'Visual Discrimination Training'))

# Render the selected page
if page == 'Home Page':
    st.title('Welcome to thelittleoptom Optometry website!!	:sparkles:')
    st.markdown('---')
    st.write('This website offers a complimentary repository for optometrists.:clap::clap::clap::clap:')
    st.write('Using the sidebar as a convenient navigation tool!:angel:')
    st.caption('Created by Charles Li, FAAO')
    st.image('littleoptom.png')

if page== 'Myopia Control Calculator: Axial Length':
    st.subheader("Myopia Control Calculator: Axial Length")

# Create two columns for inputs
    col1, col2 = st.columns(2)
    st.markdown('')
    st.markdown('')
    with col1:
        st.text('Before Myopia Control')
        st.markdown('')
        date_1 = st.date_input("Date of 1st Visit:")
        axial_length_1 = st.number_input("1st Axial Length (in mm):", min_value=0.0)

        st.markdown('')
        date_2 = st.date_input("Date of 2nd Visit (Myopia Control Start):")
        axial_length_2 = st.number_input("2nd Axial Length (in mm):", min_value=0.0)

    with col2:
        st.text('After Myopia Control')
        st.markdown('')
        date_3 = st.date_input("Date of 3rd Visit:")
        axial_length_3 = st.number_input("3rd Axial Length (in mm):", min_value=0.0)

    if date_1 and date_2 and date_3:
        days_1_to_2 = (date_2 - date_1).days
        days_2_to_3 = (date_3 - date_2).days

# Calculate the rate of change if all lengths are provided
    if axial_length_1 and axial_length_2 and axial_length_3:
    # Calculate the change before and after myopia control
        change_before = (axial_length_2 - axial_length_1)/ days_1_to_2
        change_after = (axial_length_3 - axial_length_2)/ days_2_to_3
    
    # Calculate control rate as a percentage change
        control_rate = ((change_before - change_after) / change_before) * 100 if change_before != 0 else 0
    
    st.markdown(control_rate)

    #st.write(f"Change in Axial Length Before Myopia Control: {change_before} mm, in {days_1_to_2} days ")
    #st.write(f"Change in Axial Length After Myopia Control: {change_after} mm, in {days_2_to_3} days")
    

    

if page == 'W4dot':
    st.title('Worth 4 dot')
    st.write('Sensory fusion testing')
    # Add content specific to the Home page

    st.markdown('---')

    st.caption('Please wear your red-green goggles')
    col1, col2 = st.columns(2)
    
    with col1:
        red_picker = st.slider('Adjust the red color so that you can only see the red dot with your left eye',
                       100, 255, 200, 1)
        red_color = (red_picker, 0.0, 0.0)
        st.write('Selected red color:', red_color)
    with col2:
        blue_picker = st.slider('Adjust the blue color so that you can only see the blue dot with your right eye',
                       0, 255, 0, 1)
        blue_color = (0, blue_picker,150)
        st.write('Selected blue color:', blue_color)
# Define the CSS style for the circles
    circle_style = f"""
    <style>
    .container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 400px;
    }}

    .line {{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 50px;
    }}

    .circle {{
        width: 100px;
    height: 100px;
    border-radius: 50%;
    margin: 0px 80px;
}}

.red-circle {{
    background-color: rgb{red_color};
}}

.blue-circle {{
    background-color: rgb{blue_color};
}}

.white-circle {{
    background-color: white;
}}
</style>
"""

# Display the circles using HTML and CSS
    st.markdown(circle_style, unsafe_allow_html=True)
    st.markdown('<div class="container">'
           '<div class="line">'
            '<div class="circle red-circle"></div>'
            '</div>'
            '<div class="line">'
            '<div class="circle blue-circle"></div>'
            '<div class="circle blue-circle"></div>'
            '</div>'
            '<div class="line">'
            '<div class="circle white-circle"></div>'
            '</div>'
            '</div>', unsafe_allow_html=True)

if page == 'Hart Chart':
    st.empty()  # Clear the existing content
    st.title('Welcome to the Hart Chart')
    st.subheader('Antisuppression Hart Chart')
    import random


    def random_letter():
        return chr(random.randint(65, 90))

# Adjust the red color using a slider
    col1, col2 = st.columns(2)
    
    with col1:
        red_picker = st.slider('Adjust the red color so that you can only see the red dot with your left eye',
                       100, 255, 200, 1)
        red_color = (red_picker, 0.0, 0.0)
        st.write('Selected red color:', red_color)
    with col2:
        blue_picker = st.slider('Adjust the blue color so that you can only see the blue dot with your right eye',
                       0, 255, 0, 1)
        blue_color = (0, blue_picker,150)
        st.write('Selected blue color:', blue_color)    


    words = [random_letter() for _ in range(20)]
    font_size = 50
    colored_words = []
    for word in words:
        color_choice = random.choice(["red", "blue"])
        if color_choice == "red":
            colored_words.append("<span style='color: rgb{};font-size: {}px;'>{}</span>".format(red_color,font_size, word))
        else:
            colored_words.append("<span style='color: rgb{};font-size: {}px;'>{}</span>".format(blue_color, font_size, word))

    line_1 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(colored_words[:5])
    line_2 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(colored_words[15:20])
    line_3 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(colored_words[6:11])
    line_4 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(colored_words[11:16])

    line_1 = line_1.format(red_color=red_color)
    line_2 = line_2.format(blue_color=blue_color)
    line_3 = line_3.format(red_color=red_color)
    line_4 = line_4.format(blue_color=blue_color)

    st.markdown(line_1, unsafe_allow_html=True)
    st.markdown(line_2, unsafe_allow_html=True)
    st.markdown(line_3, unsafe_allow_html=True)
    st.markdown(line_4, unsafe_allow_html=True)
    st.button('Randomise it!!')

#new  accommodation facility training
if page == 'Accommodation Facility Training':
    st.title('Acommodation Facility Training')
    st.write('Wear the red-green goggle and put the HTS flipper in front of your goggles')
    # Add content specific to the Home page

    st.markdown('---')

    st.caption('Please wear your red-green goggles')
    col1, col2 = st.columns(2)
    
    with col1:
        red_picker = st.slider('Adjust the red color so that you can only see the red dot with your left eye',
                       100, 255, 200, 1)
        red_color = (red_picker, 0.0, 0.0)
        st.write('Selected red color:', red_color)
    with col2:
        blue_picker = st.slider('Adjust the blue color so that you can only see the blue dot with your right eye',
                       0, 255, 0, 1)
        blue_color = (0, blue_picker,150)
        st.write('Selected blue color:', blue_color)

    if 'boolean' not in st.session_state:
        st.session_state.boolean = False
    #st.write(st.session_state)

    def random_letter():
        return chr(random.randint(65,90))

    words = [random_letter() for _ in range(20)]
    font_size = 20
    colored_words = []
    for word in words:
        if st.session_state.boolean ==False:
            colored_words.append("<span style='color: rgb{};font-size: {}px;'>{}</span>".format(red_color,font_size, word))
        if st.session_state.boolean ==True:
            colored_words.append("<span style='color: rgb{};font-size: {}px;'>{}</span>".format(blue_color, font_size, word))

    line_1 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(colored_words[:5])

    #line_1 = line_1.format(red_color=red_color)

    st.markdown('---')
    st.markdown(line_1, unsafe_allow_html=True)


    button=st.button('Switch!')
    if button:
        st.session_state.boolean= not st.session_state.boolean

if page == 'Red Blue Circular Pong':
    st.title('Red Blue Circular Pong')
    st.write('Antisuppression Pursuit Training')
    # Add content specific to the Home page

    st.markdown('---')

    st.caption('Please wear your red-green goggles. You may adjust the red/blue color saturation so that you can only see one color by one eye')
    st.caption('https://gd.games/games/cb9c2cfb-5116-440e-b27d-afbbac7d1c34')
    st.image('Circularpong.png')

if page == 'Red Blue Space Asteroids':
    st.title('Red Blue Space Asteroids')
    st.write('Antisuppression Training')
    # Add content specific to the Home page

    st.markdown('---')

    st.caption('Please wear your red-green goggles. You may adjust the red/blue color saturation so that you can only see one color by one eye')
    st.caption('https://gd.games/games/f5c08170-30d1-4018-813d-d4ad6960eac4')
    st.image('Spaceasteroids.png')

if page == 'Visual Discrimination Training':
    st.title('Visual Discrimination Training')
    st.write('This exercise aims at improving the visuo-spatial and visual discrimination skills')
    # Add content specific to the Home page

    st.markdown('---')

    st.caption('Click the link to play. There are 3 levels')
    st.caption('https://gd.games/games/2be9c5f5-3a00-4ae3-b38e-6763a9db8925')
    st.image('DISCOVER.png')
    st.image('easy.png')
    st.image('medium.png')
    st.image('hard.png')
