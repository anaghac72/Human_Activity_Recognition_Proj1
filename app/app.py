import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="HAR System",
    page_icon="🧠",
    layout="wide"
)

# -----------------------
# LOAD MODEL
# -----------------------
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "rf_model.pkl")
model = joblib.load(MODEL_PATH)  # or svm_model.pkl

# -----------------------
# LABEL MAP
# -----------------------
label_map = {
    1: "🚶 WALKING",
    2: "⬆️ WALKING_UPSTAIRS",
    3: "⬇️ WALKING_DOWNSTAIRS",
    4: "🪑 SITTING",
    5: "🧍 STANDING",
    6: "🛌 LAYING"
}

# -----------------------
# HEADER
# -----------------------
st.title("🧠 Human Activity Recognition System")
st.markdown("### Predict human activities using sensor data (UCI HAR Dataset)")

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.header("⚙️ Settings")

mode = st.sidebar.radio(
    "Select Prediction Mode",
    ["Manual Row", "Random Row", "Batch Prediction"]
)

uploaded_file = st.sidebar.file_uploader("📂 Upload CSV File", type=["csv"])

# -----------------------
# MAIN CONTENT
# -----------------------
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Overview")
    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    with st.expander("🔍 Preview Data"):
        st.dataframe(df.head())

    # -----------------------
    # MANUAL ROW
    # -----------------------
    if mode == "Manual Row":

        st.subheader("🎯 Manual Prediction")

        row_index = st.slider("Select Row Index", 0, len(df)-1, 0)

        if st.button("Predict"):

            sample = df.iloc[row_index].values

            if len(sample) != 561:
                st.error(f"❌ Expected 561 features, got {len(sample)}")
            else:
                pred = model.predict(sample.reshape(1, -1))[0]

                st.success("Prediction Result:")
                st.markdown(f"## {label_map[pred]}")

    # -----------------------
    # RANDOM ROW
    # -----------------------
    elif mode == "Random Row":

        st.subheader("🎲 Random Prediction")

        if st.button("Generate Random Prediction"):

            row_index = np.random.randint(0, len(df))
            sample = df.iloc[row_index].values

            st.write(f"Selected Row: {row_index}")

            if len(sample) == 561:
                pred = model.predict(sample.reshape(1, -1))[0]

                st.success("Prediction Result:")
                st.markdown(f"## {label_map[pred]}")

    # -----------------------
    # BATCH PREDICTION
    # -----------------------
    elif mode == "Batch Prediction":

        st.subheader("📊 Batch Predictions (First 10 Rows)")

        if st.button("Run Batch Prediction"):

            results = []

            for i in range(min(10, len(df))):
                sample = df.iloc[i].values

                if len(sample) == 561:
                    pred = model.predict(sample.reshape(1, -1))[0]
                    results.append([i, label_map[pred]])

            result_df = pd.DataFrame(results, columns=["Row", "Prediction"])

            st.dataframe(result_df)

# -----------------------
# NO FILE
# -----------------------
else:
    st.info("👈 Upload a CSV file from the sidebar to begin")

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.markdown("Developed for Human Activity Recognition Project 🚀")
