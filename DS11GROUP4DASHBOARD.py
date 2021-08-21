# DS11 GROUP4 DATA SCIENCE PROJECT VISUALIZATION

# 1.Uploading the required libraries
from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import altair as alt
import matplotlib.pyplot as plot
import seaborn as sns

# 2.Project outline
intro = st.container()
dataset = st.container()
analytics=st.container()
conclusion = st.container()

# 3.Introduction
with intro:
   st.title('DS11 Group 4 Data Science Project')
   st.header('Analysis to Find the Distribution of Healthcare Services and Workforce in Kenya and Its Correlation to Economic Growth')
   st.subheader('Background Information')
   st.text('This research explores the distribution of health care services in Kenya to identify gaps\nand give recommendations to government on future policy implications as well as the private\nsector on where to channel their resources because building on this and prior research,\nit is evident that the good health of citizens indeed results in an overall better economy')
   # st.subheader('Problem Statement')
   # st.text('How do we improve the healthcare infrastructure to ensure no matter your location in Kenya\nyou have access to proper healthcare by ensuring money allocated to healthcare across the\ncountry is fair and sufficient to cater to its persons.')
   
# 4.Datasets
with dataset:
   st.subheader('Datasets Used')
   # st.text('In order to fulfill the objectives of our project, we will derive our datasets from\nthe National Census and most of the surveys done by the Kenya National bureau of\nstatistics. More from open data, WHO and UNICEF.')
   
   st.markdown('Dataset 1: Annual GDP Kenya')
   AnnGDP= pd.read_csv("https://raw.githubusercontent.com/franciskingk/Healthcare-dataset/main/Annual%20GDP.csv")  
   # AnnGDP
   
   st.markdown('Dataset 2: Health Spending per Capita by County')
   HealthperCapita = pd.read_csv("https://raw.githubusercontent.com/franciskingk/Healthcare-dataset/main/Health_Spending_Per_Capita_By_County.csv")  
   # HealthperCapita
      
   st.markdown('Dataset 3: List of hospitals and number of beds - Kenya 2020')
   HbedsKe = pd.read_csv("https://raw.githubusercontent.com/franciskingk/Healthcare-dataset/main/List%20of%20hospitals%20and%20number%20of%20beds%20-%20Kenya%202020.csv")  
   # HbedsKe

   st.markdown('Dataset 4: Kenyan Allocation to Health per year')
   AnnHealthAllocationKe =pd.read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/kenyan_allocation_to_health_per_year1.csv")  
   # AnnHealthAllocationKe

   st.markdown('Dataset 5: Allocation to Health per year Worldwide')
   D6 = read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/percentage_of_gdp_alocated_to_healt1.csv")  
   D6.sort_values(D6.columns[23], axis=0, inplace=True)
   # D6

   st.markdown('Dataset 6: Health Staff')
   D7 = read_csv("https://raw.githubusercontent.com/joywangai/DS11-GROUP4-DATA-SCIENCE-PROJECT-VIS/main/healthstaff11.csv") 
   D7.sort_values(D7.columns[1], axis=0, inplace=True) 
   # D7

# 5.Data Analytics
with analytics:
   st.subheader('Data Analysis')
   # st.text('These are the results of our data analysis.')

   HbedsKe1=plot.figure(figsize=(5,3))
   HbedsKe['Owner type'].value_counts().plot(kind= 'pie', autopct='%.1f%%')
   # st.write(HbedsKe1)

   HbedsKe2=plot.figure(figsize=(10,3))
   HbedsKe['Keph level'].value_counts().plot(kind= 'bar')
   # st.write(HbedsKe2)
   
   D61=plot.figure(figsize=(16,12))
   sns.barplot(x='2018yr', y='Country Name', data=D6)
   # st.write(D61) 
   
   D71= plot.figure(figsize=(16,12))
   sns.barplot(x='Core health workforce per 10,000\rpopulation', y='County', data=D7)
   # st.write(D71)
   
   AnnHealthAllocationKe1=plot.figure(figsize=(16,12))
   sns.barplot(x='Year', y='Current health expenditure (% of GDP)', data=AnnHealthAllocationKe)
   # st.write(AnnHealthAllocationKe1)

   AnnGDP1=plot.figure(figsize=(16,12))
   sns.barplot(x='Year', y='Annual GDP growth (%)', data=AnnGDP)
   # st.write(AnnGDP1)

   percapita1=plot.figure(figsize=(16,12))
   sns.barplot(y='County', x='Heath_Spending_Per_Person_', data=HealthperCapita)
   # st.write(percapita1)


# 5.1 Print the Data Visualisations
   option = st.selectbox("Choose Dataset", ('Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4', 'Dataset 5', 'Dataset 6'))
   st.header(option)

   if option == 'Dataset 1':
      'A. GDP', AnnGDP
      st.markdown('B. Distribution of GDP growth from the year 2000 to the year 2018')
      st.write(AnnGDP1)

   if option == 'Dataset 2':
      'A. Health Spending per Capita by County', HealthperCapita
      st.markdown('B. Distribution of Health Spending per Capita by County')
      st.write(percapita1)

   if option == 'Dataset 3':
      'A. List of hospitals and number of beds - Kenya 2020', HbedsKe
      st.markdown('B. The ownership of Hospitals in Kenya')
      st.write(HbedsKe1)
      st.markdown('C. Distribution of Hospital levels in Kenya')
      st.write(HbedsKe2)
   
   if option == 'Dataset 4':
      'A. Kenyan Allocation to Health per year', AnnHealthAllocationKe
      st.markdown('B. Distribution of Healthcare expenditure as a % of the GDP from the year 2000 to the year 2018')
      st.write(AnnHealthAllocationKe1)

   if option == 'Dataset 5':
      'A. Allocation to Health per year Worldwide', D6
      st.markdown('B. Amount spent on healthcare in Kenya vs the world')
      st.write(D61)

   if option == 'Dataset 6':
      'A. Health Staff', D7
      st.markdown('B. Distribution per county of healthcare workers per 10,000 people')
      st.write(D71)   
   
# 6.Conclusion
with conclusion:
   st.subheader('Recommendations')
   st.text('1.The Government of Kenya can create policies and a conducive environment for NGOs\n and Faith Based Organizations to set more healthcare facilities in the country.\n2.Nairobi County has the highest number of beds at 1005 while Lamu has the lowest at 56.\nThe government of Kenya should focus on better equipping the hospitals in Lamu, West\nPokot and Tana River both for the beds and cots in order to reduce the\nchild mortality rates for these counties.\n3. Majority of the hospitals in the country are of Keph Level 2 while Level 4 is the least.\n4.The counties with the highest populations such as Kiambu and Nairobi should\nfocus their efforts in increasing the number of healthcare workers.\n5.The government of Kenya should world with the private sector to train more doctors and\nmake training affordable so that we as a country can start making steps towards closing\nthis huge gap.\n6.The National Treasury should channel more funds towards healthcare during the budgetary\nallocation process especially since in our research it is evident that the amount has\nsince been reducing gradually despite the high rates of inflation annually.\n7.The Kenyan government should increase the amount of spending of the GDP to health\ncare upto at least 8% to match a country like South Africa.')
