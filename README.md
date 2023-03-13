# Tech-Job-Recommendation

Problem Statement
---
New developers & students struggle to know which technical jobs they can pursue given their current skills, in addition to which skills to add to their arsenal in order to be able to pursue a technical job of their choice. Therefore, this project aims to help developers have better understaning of their status quo & guide them by highlighting required skills for different technical jobs that are used in the market.

Demo
---


Dataset
---
Stackoverflow makes an annual survey to their users where they accumulate data about to the current state of the technical sector. The dataset we worked on is of 2022 survey, & it can be downloaded [here](https://insights.stackoverflow.com/survey). 
> A downloaded version is included in the files, so in order to work with the dataset, first unzip the file under /data/raw & use the csv file named "survey_results_public_2022.csv"

Installation
---
* Clone this repository:
```
git clone https://github.com/MoRaouf/Tech-Job-Recommendation.git
```
* Set up the virtual environment and all required dependencies by:
  * Setting up a `python=3.8` virtual environment
  * run: `pip install -r requirements.txt`
    
* Run the Streamlit App
```
cd scripts
streamlit run streamlit_app.py
```
* The api will be automatically serving at localhost.

Requirements
---
This project used the following libraries:
```
numpy
pandas
matplotlib
plotly
sklearn
pickle
yaml
pathlib
mlflow
streamlit
```

Model Deployment
---
The tool is deployed as an app to Streamlit, & it can be accessed through [link].
```
```





