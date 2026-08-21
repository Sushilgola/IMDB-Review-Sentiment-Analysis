import streamlit as st 
import joblib

model = joblib.load("lr_model.pkl")
tfidf = joblib.load("Tfidf.pkl")

# page configuration 

st.set_page_config( 
    page_title="Sentiment Analyzer Model",
    page_icon="😊"
)

st.title("😊 Movie Sentiment Analysis")
st.write("Enter the review and find the sentiment responces! ")

movie_name = st.text_input("Enter the Movie Name: ")

text = st.text_area( 
    'Enter the Review of Movies Here ', 
    placeholder="Text like, This Movie was absulate amazing! "
)

if st.button("🔍 Predict Sentiments", use_container_width=True):
    if movie_name =="" and text =="":
            st.error("Please fill the Movie Name, And Some Text!")

    if movie_name =="":
        st.error("Please fill the Movie Name!")

    elif text =="":
        st.error("Please Enter Some text!")
    else:
        # convert the text with Tfidf 
        tfidf_text = tfidf.transform([text])

        prediction = model.predict(tfidf_text)[0]
        pred_prob = model.predict_proba(tfidf_text)[0][1]

        st.subheader("Prediction")

        if prediction==1:
            st.write("Movie Name: ", f"{movie_name}")
            st.success("😊 Positive")
            st.write("Accuracy : ")
            st.success(f"{pred_prob:.2%}")
        else:
            st.write("Movie Name: ", f"{movie_name}")
            st.error("🥺 Negative")
            st.write("Accuracy :")
            st.success(f"{pred_prob:.2%}")
