# DS11 GROUP4 DATA SCIENCE PROJECT VISUALIZATION

# 1.Uploading the required libraries
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plot
import seaborn as sns

# 2.Project outline
intro = st.container()
dataset = st.container()
conclusion = st.container()

# 3.Introduction
with intro:
   st.title('DS11 Group 4 Data Science Project')
   st.header('Analysis to Find the Distribution of Healthcare Services and Workforce in Kenya and Its Correlation to Economic Growth')
   st.subheader('Background Information')
   st.text('This research explores the distribution of health care services in Kenya to identify gaps\nand give recommendations to government on future policy implications as well as the private\nsector on where to channel their resources because building on this and prior research,\nit is evident that the good health of citizens indeed results in an overall better economy')
   st.subheader('Problem Statement')
   st.text('How do we improve the healthcare infrastructure to ensure no matter your location in Kenya\nyou have access to proper healthcare by ensuring money allocated to healthcare across the\ncountry is fair and sufficient to cater to its persons.')
   
# 4.Dataset Visualisation
with dataset:
   st.subheader('Datasets Used')
   st.text('In order to fulfill the objectives of our project, we will derive our datasets from\nthe National Census and most of the surveys done by the Kenya National bureau of\nstatistics. More from open data, WHO and UNICEF.')
   
   st.markdown('Dataset 1: Child Mortality Rate')
   cmr = pd.read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/export_dataframe_child_mortality.csv")  
   'Child Mortality Rate',cmr

   fig = plot.figure()
   ax = fig.add_subplot(1,1,1)

   ax.bar(
      cmr["m"],
      cmr["Indicator"],
   )

   ax.set_xlabel("Mortality")
   ax.set_ylabel("Indicator")

   st.write(fig)


   st.markdown('Dataset 2: Percentage of GDP allocated to Health')
   GDPvHealth = pd.read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/percentage_of_gdp_alocated_to_healt.csv",sep=',')  
   'GDPvHealth',GDPvHealth
   
   st.markdown('Dataset 3: Number of Hospital beds in Kenya')
   HBedsKe = pd.read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/Number%20of%20hospital%20beds%20in%20Kenya%2C%202020.csv")  
   'HBedsKe',HBedsKe

   fig1 = plot.figure()
   ax = fig1.add_subplot(1,1,1)

   ax.bar(
      HBedsKe["Geography"],
      HBedsKe["Number of hospital beds"],
   )

   ax.set_xlabel("Number of hospital beds")
   ax.set_ylabel("Geography")

   st.write(fig1)

   st.markdown('Dataset 4: Community Health Units')
   CoHealthUnits = pd.read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/List%20of%20community%20health%20units.csv")  
   'CoHealthUnits', CoHealthUnits
  
# 5.Conclusion
with conclusion:
   st.subheader('Proposed Solution')
   st.text('To come up with a clear analysis of distribution of the different aspects of healthcare\nin our country and the impact to economic growth and propose recommendations for the\ngovernment and private sector on how to better distribute health care services across\nthe country.')
   