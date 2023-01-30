import openai
import pandas as pd

# you need to own api key
openai.api_key = "your_api_key"

# open ai model list
# just for check
openai.Model.list()

# I tried this with much larger data and texts.+
# Due to privacy, I cannot share hole text or data.
# But you can try it with your own raw text data

data = "Sol Ventrikül	Ölçüm	Referans		" \
       "Sol ve Sağ Atriyum	Ölçüm	Referans Aort Kökü (cm)	2,1	2.2-3.6		" \
       "Sol Atriyum Boyutu (cm)	3,3	2.7 - 3.8 (K) 3.0-4.0 (E)"

# prompt for generation
prompt = (f"Convert the following data into a dataframe:\n"
          f"{data}\n"
          f"Language: Python")

# OpenAI API to generate
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1000, n=10)

for choice in response.choices:
print(choice.text)


#A lot of options were generated below, let's use one of them.

# Results

"""
import pandas as pd 
  
# intialise data of lists. 
data = {'Sol Ventrikül':[2.1, 3.3], 'Ölçüm':[2.2, 3.8], 'Referans':[3.6, 4.0]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 

# Print the output. 
df
df = pd.DataFrame({
    'Sol Ventrikül': ['Ölçüm', 'Referans'],
    'Sol ve Sağ Atriyum': ['Ölçüm', 'Referans'],
    'Aort Kökü (cm)': [2.1, 2.2-3.6],
    'Sol Atriyum Boyutu (cm)': [3.3, 2.7 - 3.8 (K) 3.0-4.0 (E)]
})

import pandas as pd
data_dict = {"Sol Ventrikül": ["Ölçüm", "Referans"],
             "Sol ve Sağ Atriyum": ["Ölçüm", "Referans"],
             "Aort Kökü (cm)": ["2,1", "2.2-3.6"],
             "Sol Atriyum Boyutu (cm)": ["3,3", "2.7 - 3.8 (K) 3.0-4.0 (E)"]}
df = pd.DataFrame(data_dict)


import pandas as pd
data = {'Sol Ventrikül': ['Ölçüm', 'Referans'], 
        'Sol ve Sağ Atriyum': ['Ölçüm', 'Referans'], 
        'Aort Kökü (cm)': 2.1, 2.2-3.6,
        'Sol Atriyum Boyutu (cm)': 3.3, 2.7 - 3.8 (K) 3.0-4.0 (E)}
df = pd.DataFrame(data)
print(df)


import pandas as pd
data = {'Sol Ventrikül': ['2.1', '3.3'],
        'Ölçüm': ['2.2-3.6', '2.7-3.8 (K) 3.0-4.0 (E)'],
        'Referans': ['Aort Kökü (cm)', 'Sol Atriyum Boyutu (cm)'],
        'Sol ve Sağ Atriyum': ['', '']}
df = pd.DataFrame(data)
print(df)


import pandas as pd
data = {'Sol Ventrikül': ['2.1', '3.3'], 
        'Ölçüm': ['2.2-3.6', '2.7-3.8 (K) 3.0-4.0 (E)'],
        'Referans': ['Aort Kökü (cm)', 'Sol Atriyum Boyutu (cm)']}
df = pd.DataFrame(data)
print(df)


import pandas as pd
data = {'Sol Ventrikül': ['2.1', '3.3'], 'Ölçüm': ['2.2-3.6', '2.7 - 3.8 (K) 3.0-4.0 (E)'], 'Referans': ['Sol ve Sağ Atriyum', 'Aort Kökü (cm)']}
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = {'Sol Ventrikül' : ['Ölçüm', 'Referans'],
        'Sol ve Sağ Atriyum' : ['Ölçüm', 'Referans'],
        'Aort Kökü (cm)' : ['2,1', '2.2-3.6'],
        'Sol Atriyum Boyutu (cm)' : ['3,3', '2.7 - 3.8 (K) 3.0-4.0 (E)']}
df = pd.DataFrame(data)
print(df)


import pandas as pd
data = {'Sol Ventrikül': ['Ölçüm', 'Referans'],
        'Sol ve Sağ Atriyum': ['Ölçüm', 'Referans'],
        'Aort Kökü (cm)': [2.1, 2.2-3.6],
        'Sol Atriyum Boyutu (cm)': [3.3, 2.7-3.8]}
df = pd.DataFrame(data)
print(df)


import pandas as pd 
data = [['Sol Ventrikül', 'Ölçüm', 'Referans', 'Sol ve Sağ Atriyum', 'Ölçüm', 'Referans Aort Kökü (cm)', '2,1', '2.2-3.6', 'Sol Atriyum Boyutu (cm)', '3,3', '2.7 - 3.8 (K) 3.0-4.0 (E)'], ['', '', '', '', '', '', '', '', '', '', '']]
df = pd.DataFrame(data, columns=['Sol Ventrikül', 'Ölçüm', 'Referans', 'Sol ve Sağ Atriyum', 'Ölçüm', 'Referans Aort Kökü (cm)', '2,1', '2.2-3.6', 'Sol Atriyum Boyutu (cm)', '3,3', '2.7 - 3.8 (K) 3.0-4.0 (E)'])

import pandas as pd 
data = ({'Sol Ventrikül': ['2.1', '3.3'],
                   'Referans': ['2.2-3.6', '2.7 - 3.8 (K) 3.0-4.0 (E)'],
                   'Aort Kökü (cm)': ['2,1', 'Sol Atriyum Boyutu (cm)'],
                   'Referans Aort Kökü (cm)': ['2.2-3.6', '2.7 - 3.8 (K) 3.0-4.0 (E)']})
                   
df = pd.DataFrame(data)

import pandas as pd
data = {'Sol Ventrikül': ['Ölçüm', 'Referans'],
        'Sol ve Sağ Atriyum': ['Ölçüm', 'Referans'],
        'Aort Kökü (cm)': ['2,1', '2.2-3.6'],
        'Sol Atriyum Boyutu (cm)': ['3,3', '2.7 - 3.8 (K) 3.0-4.0 (E)']}
df = pd.DataFrame(data)
print(df)

"""

data = {'Sol Ventrikül': ['Ölçüm', 'Referans'],
        'Sol ve Sağ Atriyum': ['Ölçüm', 'Referans'],
        'Aort Kökü (cm)': ['2,1', '2.2-3.6'],
        'Sol Atriyum Boyutu (cm)': ['3,3', '2.7 - 3.8 (K) 3.0-4.0 (E)']}
df = pd.DataFrame(data)

print(df)

