import streamlit as st
import boto3
import uuid
from textblob import TextBlob
import time
import json
import requests

st.title("📞 Speech Analytics Dashboard")

uploaded_file = st.file_uploader("Upload call recording (.mp3)", type="mp3")

if uploaded_file:
    session_id = str(uuid.uuid4())
    filename = f"{session_id}.mp3"
    
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(filename)
    st.info("Uploading file to S3...")

    s3 = boto3.client('s3')
    bucket_name = 'speech-recon-app'
    s3.upload_file(filename, bucket_name, filename)

    st.success("Uploaded to S3!")

    transcribe = boto3.client('transcribe')
    job_name = f"job-{session_id}"
    media_uri = f"s3://{bucket_name}/{filename}"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': media_uri},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )

    st.info("Transcribing... This may take up to 1 minute.")

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(5)

    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        transcript_json = requests.get(transcript_uri).json()
        text = transcript_json['results']['transcripts'][0]['transcript']

        st.subheader("📄 Transcription")
        st.write(text)

        st.subheader("📊 Sentiment Analysis")
        sentiment = TextBlob(text).sentiment
        st.write(f"Polarity: {sentiment.polarity}")
        st.write(f"Subjectivity: {sentiment.subjectivity}")
    else:
        st.error("Transcription failed.")
