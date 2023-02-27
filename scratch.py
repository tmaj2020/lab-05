import platform
import time
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import re

fig = px.bar()

fig.show()
fig.write_image("testing.png", format="png", engine = "kaleido")