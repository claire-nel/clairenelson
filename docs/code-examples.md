*I'm currently using the following [dataset](https://huggingface.co/datasets/lukebarousse/data_jobs) from data analyst and content creator Luke Barousse to analyze job market trends for data professionals. For now, I have only uploaded my first steps, but I will upload the full code once I have finished debugging the projet.*

###1. Importing libraries.

```py
# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

###2. Loading Data.

```py
from datasets import load_dataset
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()
```

###3. Cleaning Data.

```py
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
```