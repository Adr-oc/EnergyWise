import customtkinter
from PIL import ImageTk, Image
from login import *
import pandas as pd
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
from werkzeug.security import generate_password_hash, check_password_hash

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")
