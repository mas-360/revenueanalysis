# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 07:39:45 2023

@author: 27823
"""

from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import ssl
import streamlit as st 

ssl._create_default_https_context = ssl._create_unverified_context 

st.set_page_config(page_title='A Revenue Analysis', layout='centered', page_icon="📊")

st.header('📊 Annual Revenue Analysis')
st.write("---")

width=950
height=500

# initialize chart
data = Data()
df = pd.read_csv('salesbyyear.csv', dtype={'Year': str})
data.add_df(df)


story = Story(data=data)
story.set_size(width, height)

slide1 = Slide(
    Step(
        Config(
            {
                "title": "Consistent growth for most products despite production issues in 2021.",
                "channels": {
                    "x": "Year",
                    "y" : ["Revenue [$]", "Product"],
                    "color": "Product",
                    },
                "geometry" :"area",
                "align": "center",
                }
            ),
        Style(
            {
                "plot": {
                "marker": {
                    "colorPalette": "#f07167FF #fed9b7FF #fdfcdcFF #00afb9FF"
                }},
                                
            }
            ),
        )
    )
story.add_slide(slide1)

slide2 = Slide()
slide2.add_step(
    Step(
        Config(
            {
                "align": "min", "split": True,
                }),
        Style(
            {
                "plot": {
                "marker": {
                    "colorPalette": "#f07167FF #fed9b7FF #fdfcdcFF #00afb9FF"
                }
            }  # Set the color palette here
            }
        )
    ))
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Config(
            {
               "channels":{"x": ["Product", "Year"], "y": "Revenue [$]"},
               "split": False,
          
               }
            ),
        Style(
            {
                "plot": {
                "marker": {
                    "colorPalette": "#f07167FF #fed9b7FF #fdfcdcFF #00afb9FF"
                }  # Set the color palette here
            }
        }
    )
   )
)
story.add_slide(slide3)

story.set_feature('tooltip', True)

html(story._repr_html_(), width=width, height=height)

st.download_button('Download HTML export', story.to_html(), file_name=f'revenue-by-product.html', mime='text/html')

st.write("---")    
st.markdown('''
Contact: masinsight360@gmail.com
''')
  

