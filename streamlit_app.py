import streamlit as st
from multiapp import MultiApp
from app import main as app_main
from page2 import main as page2_main

app = MultiApp()

# Add all your application here
app.add_app("Business Card Recognition", app_main)
app.add_app("Business Card History", page2_main)

# The main app
app.run()
