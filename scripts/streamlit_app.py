import streamlit as st
from JobPrediction import JobPrediction

MLFLOW_TRACKING_URI = '../models/mlruns'
MLFLOW_RUN_ID = "31ae402b0ee14d82934009728f2c3caf"
CLUSTERS_YAML_PATH = "../data/processed/features_skills_clusters_description.yaml"


#Create model
model = JobPrediction(MLFLOW_TRACKING_URI, MLFLOW_RUN_ID, CLUSTERS_YAML_PATH)

st.title("Technical Job Recommendation App")
st.caption("App developed by: Mohammed Raouf")

#Select Skills
st.markdown("""---""")
st.subheader("Skills Selection")
skills = st.multiselect("Select the skills you currently have:", model.get_all_skills(), ["NumPy"])

############## Jobs Recommendation ##############
st.markdown("""---""")
st.subheader("Job Recommendation")
st.warning("Select skills from above before getting recommendations")

st.write("Find technical jobs based on your current skills")
jobs_state = st.button("Get Jobs Recommendtion")
df = model.predict_jobs_probabilities(skills).to_frame().rename(columns={0: "Job Probability"}).sort_values("Job Probability" ,ascending=False)

if jobs_state:
    st.write("Your matched Jobs probabilities in descending order:")
    st.dataframe(df.style.highlight_max(axis=0))
    st.write("The most suitable job to your current skillset is: ", df.index[0])

############## Skills Recommendation ##############
st.markdown("""---""")
st.subheader("New Skills Recommendation")
# st.warning("Find your most suitable job before getting new skills recommendations")

job = st.selectbox("Select a preferable job",model.get_all_jobs())
skills_state = st.button("Find new skills to learn")

if skills_state:
    st.write("Recommended new skills to learn related to your selected job:")
    st.write(model.recommend_new_skills(skills, job, threshold=0.2))    

