import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="HAR System", layout="wide")

st.title("🧠 Human Activity Recognition (HAR)")
st.write("Predict human activities using trained ML models")

# -----------------------
# LOAD MODEL SAFELY
# -----------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("models/rf_model.pkl")  # adjust path if needed
        return model
    except FileNotFoundError:
        st.error("❌ Model file not found! Please check path.")
        return None

model = load_model()

# -----------------------
# LABEL MAP
# -----------------------
label_map = {
    1: "WALKING",
    2: "WALKING_UPSTAIRS",
    3: "WALKING_DOWNSTAIRS",
    4: "SITTING",
    5: "STANDING",
    6: "LAYING"
}

# -----------------------
# FILE UPLOAD
# -----------------------
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file is not None and model is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")
        st.write("Dataset Shape:", df.shape)

        st.dataframe(df.head())

        # -----------------------
        # VALIDATION
        # -----------------------
        if df.shape[1] != 561:
            st.error(f"❌ Expected 561 features, got {df.shape[1]}")
        else:

            st.subheader("🎯 Prediction Mode")
            mode = st.selectbox(
                "Choose mode",
                ["Single Row", "Random Row", "Batch Prediction"]
            )

            # -----------------------
            # SINGLE ROW
            # -----------------------
            if mode == "Single Row":
                idx = st.slider("Select Row Index", 0, len(df) - 1, 0)
                sample = df.iloc[idx].values.reshape(1, -1)

                pred = model.predict(sample)[0]
                st.success(f"Prediction: {label_map[pred]}")

                # Probabilities
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(sample)[0]
                    prob_df = pd.DataFrame({
                        "Activity": list(label_map.values()),
                        "Probability": probs
                    })

                    st.subheader("📊 Prediction Probabilities")
                    st.bar_chart(prob_df.set_index("Activity"))

            # -----------------------
            # RANDOM ROW
            # -----------------------
            elif mode == "Random Row":
                idx = np.random.randint(0, len(df))
                sample = df.iloc[idx].values.reshape(1, -1)

                st.write(f"Random Row: {idx}")

                pred = model.predict(sample)[0]
                st.success(f"Prediction: {label_map[pred]}")

            # -----------------------
            # BATCH PREDICTION
            # -----------------------
            elif mode == "Batch Prediction":
                preds = model.predict(df)

                results = pd.DataFrame({
                    "Prediction": [label_map[p] for p in preds]
                })

                st.subheader("📊 Predictions (First 10)")
                st.dataframe(results.head(10))

                # Count plot
                st.subheader("📈 Activity Distribution")
                counts = results["Prediction"].value_counts()
                st.bar_chart(counts)

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.markdown("Developed for Human Activity Recognition Project")
