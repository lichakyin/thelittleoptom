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
page = st.sidebar.selectbox('Go to', ('Home Page', 'W4dot', 'Hart Chart', 'Accommodation Facility Training', 'Red Blue Circular Pong', 'Red Blue Space Asteroids'))

# Render the selected page
if page == 'Home Page':
    st.title('Welcome to thelittleoptom Binocular Vision website!!	:sparkles:')
    st.markdown('---')
    st.write('This website offers a complimentary repository for binocular vision. By utilizing simple tools, optometrists can provide the optimal binocular vision trainings to their patients, ensuring the utmost level of care.:clap::clap::clap::clap:')
    st.write('Using the sidebar as a convenient navigation tool, you can explore "Binocular Testing" and "Binocular Training"! The website will provide updates in the future. Enjoy your journey!:angel:')
    st.caption('Created by Charles Li')
    st.image('littleoptom.png')


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
