
import streamlit as st
import requests
import os
api_key = os.environ.get("OPENROUTER_API_KEY", "your_openrouter_api_key_here")

st.set_page_config(page_title="Job Search AI Toolkit", page_icon="💼")
st.title("💼 Job Search AI Toolkit")
st.subheader("Built for real job seekers")

tab1, tab2, tab3 = st.tabs(["📄 Resume Analyzer", "✉️ Cover Letter Generator", "🏥 Healthcare IT Checker"])

with tab1:
    st.header("Resume Analyzer")
    job_description = st.text_area("Paste Job Description", height=200, key="jd1")
    resume = st.text_area("Paste Your Resume", height=200, key="cv1")
    if st.button("Analyze My Resume"):
        if job_description and resume:
            with st.spinner("Analyzing..."):
                prompt = f"""
You are an expert resume coach and recruiter.
Analyze this resume against the job description and provide:
1. Match Score out of 100
2. Top 3 matching strengths
3. Top 3 missing keywords or skills
4. 3 specific suggestions to improve the resume for this job
Job Description:
{job_description}
Resume:
{resume}
Be specific, direct and helpful.
"""
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://streamlit.io",
                    },
                    json={
                        "model": "openrouter/auto",
                        "messages": [{"role": "user", "content": prompt}]
                    }
                )
                st.markdown(response.json()["choices"][0]["message"]["content"])
        else:
            st.warning("Please paste both the job description and your resume.")

with tab2:
    st.header("Cover Letter Generator")
    job_description2 = st.text_area("Paste Job Description", height=200, key="jd2")
    resume2 = st.text_area("Paste Your Resume", height=200, key="cv2")
    tone = st.selectbox("Select Tone", ["Professional", "Enthusiastic", "Concise"])
    if st.button("Generate Cover Letter"):
        if job_description2 and resume2:
            with st.spinner("Writing your cover letter..."):
                prompt = f"""
You are an expert cover letter writer.
Write a compelling {tone.lower()} cover letter based on this resume and job description.
- Keep it under 300 words
- Do not use generic phrases like "I am writing to express my interest"
- Be specific, human and direct
- Highlight the most relevant experience from the resume
- End with a confident closing
Job Description:
{job_description2}
Resume:
{resume2}
"""
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://streamlit.io",
                    },
                    json={
                        "model": "openrouter/auto",
                        "messages": [{"role": "user", "content": prompt}]
                    }
                )
                st.markdown(response.json()["choices"][0]["message"]["content"])
        else:
            st.warning("Please paste both the job description and your resume.")

with tab3:
    st.header("🏥 Healthcare IT Application Checker")
    st.write("Specifically designed for PHSA, VCH, and BC health authority applications.")
    job_description3 = st.text_area("Paste Healthcare Job Description", height=200, key="jd3")
    resume3 = st.text_area("Paste Your Resume", height=200, key="cv3")
    cover_letter3 = st.text_area("Paste Your Cover Letter (optional)", height=150, key="cl3")
    if st.button("Check Healthcare Application"):
        if job_description3 and resume3:
            with st.spinner("Checking your healthcare application..."):
                prompt = f"""
You are an expert in BC healthcare authority hiring, specifically PHSA and VCH.

Analyze this application and provide:

1. Indigenous Cultural Safety Score (0-10): Does the application acknowledge Indigenous Cultural Safety, Truth and Reconciliation, and anti-racism commitments? This is mandatory for all BC health authority positions.

2. Healthcare IT Keywords Score (0-10): Does the application include relevant terms like EMR, clinical systems, IMITS, ServiceNow, change control, incident management?

3. Missing Critical Elements: What mandatory elements are missing that will cause automatic rejection at PHSA/VCH?

4. Specific Improvements: 3 specific lines to add to the cover letter or resume to pass PHSA screening.

Job Description:
{job_description3}

Resume:
{resume3}

Cover Letter:
{cover_letter3}

Be direct and specific. This person needs to pass automated screening at a BC health authority.
"""
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://streamlit.io",
                    },
                    json={
                        "model": "openrouter/auto",
                        "messages": [{"role": "user", "content": prompt}]
                    }
                )
                st.markdown(response.json()["choices"][0]["message"]["content"])
        else:
            st.warning("Please paste the job description and resume.")
