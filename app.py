import streamlit as st

# 타이틀 및 간단한 설명
st.title("Welcome to Minji's Portfolio")

# 상단 메뉴
menu = st.selectbox("Click", [ "Education", "Work Experience", "Technical Stack", "Projects","Identity"])



# Identity 섹션
if menu == "Identity":
    st.header("Identity")
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ I - Innovation")
    st.write('"I strive to discover new ideas and solutions through innovation"')
    st.write('"And I work to solve problems creatively."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ D - Diligent")
    st.write('" I work diligently, putting continuous effort"')
    st.write('"And dedication into achieving my goals."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ E - Essence")
    st.write('"I focus on the essence of things."')
    st.write('"Aiming to understand and address complex issues in a clear and concise manner."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ N - Uniqueness")
    st.write('" Leveraging a unique perspective and creativity,"')
    st.write('" I approach tasks in an individualized manner, seeking innovative solutions."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ T - Trendsetter")
    st.write('"I keep an eye on emerging trends and technologies,"')
    st.write('"Aspiring to take a leading role in setting new trends."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ I - Implementation")
    st.write('"I systematically execute plans to achieve objectives"')
    st.write('"And turn ideas into reality."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ T - Trustworthiness")
    st.write('"I am reliable and earn trust by collaborating"')
    st.write('"with others to deliver results."')
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
    st.write("■ Y - Yes")
    st.write('"I believe in future possibilities "')
    st.write('"And maintain a positive attitude towards new challenges."')

# Education 섹션
elif menu == "Education":
    st.header("Education")

    st.subheader("Highest Education_Master's Degree")
    st.write("Sookmyung Women's University - Master of Big Data Analysis Convergence")
    st.write("The Master of Big Data Analysis Convergence program at Sookmyung Women's University is a comprehensive program that focuses on advanced data analysis techniques, artificial intelligence, and data management. This program equips students with the skills to extract valuable insights from large datasets and make data-driven decisions, contributing to the rapidly growing field of data science.")
    st.write("■ VISUALIZATION FOR BIGDATA")
    st.write("■ FUNDAMENTALS OF ARTIFICIAL INTELLIGENCE")
    st.write("■ DESIGN OF BIGDATA")
    st.write("■ BIG DATA PROGRAMMING WITH PYTHON")
    st.write("■ PRIVACY LAW FOR PERSONAL PROTECTION")
    st.write("■ PBL(Project-Based Learning)")
    st.write("■ SPECIAL TOPIC FOR MEDIA WITH BIG DATA")
    st.write("■ DATABASE")
    st.write("■ BUSINESS ANALYTICS")
    st.write("■ DEEP LEARNING PROGRAMMING")

# Work Experience 섹션
elif menu == "Work Experience":
    st.header("Work Experience")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.header("Experience 3: Sookmyung Women's University Intellectual Property Human Resources Development (IP HRD)")
    st.write("■  Job Position: Data analysis, research & development")
    st.write("■  Innovative Patent Human Resource Development (IP HRD) is an AI patent education project supported by the Patent Office")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.header("Experience 2: NONGHYUB")
    st.write("■  Job Position: Credit and deposit data analysis, statistics")
    st.write("■  While working at Nonghyup, I was responsible for credit and deposit operations,")
    st.write("supporting financial data analysis and efficient decision-making.")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.header("Experience 1: Samsung Seoul Hospital")
    st.write(" ■  Job Position: Medical Billing, Customer Service")


# Technical Stack 섹션
elif menu == "Technical Stack":  # <-- Adjusted the indentation here
    st.header("Technical Stack")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("■ LANGUAGES")
    st.write("Python")
    st.write("HTML")
    st.write("Markdown")
    st.write("SQL")

    st.write("■ ALGORITHMS & TECHNIQUES")
    st.write("Supervised Learning")
    st.write("Random Forest Classifier")

    st.write("■ UNSUPERVISED LEARNING")
    st.write("Latent Dirichlet Allocation")
    st.write("K-Means Clustering")

    st.write("■ NATURAL LANGUAGE PROCESSING")
    st.write("BERT")
    st.write("GPT")

    st.write("■ VISAULIZATION")
    st.write("pandas")
    st.write("matplotlib")
    st.write("seaborn")

    st.write("■ MACHINE LEARNING & NLP")
    st.write("Scikit-learn")
    st.write("transformers")
    st.write("PyTorch")
    st.write("Korpora")
    st.write("gensim")

    st.write("■ TEXT PREPROCESSING & WEB SCRAPING")
    st.write("tokenizers")
    st.write("re")
    st.write("Web Crawling")

    st.write("■ DATA PROCESSING & DISTRIBUTED STORAGE")
    st.write("Hadoop")

    st.write("■ WEB APPLICATIONS & DASHBOARDING")
    st.write("Streamlit")

    st.write("■ DATA RETRIEVAL & INTEGRATION")
    st.write("API Integration")

    st.write("■ DATA EXCHANGE FORMATS")
    st.write("JSON")

    st.write("■ DEVELOPMENT ENVIRONMENTS & TOOLS")
    st.write("Google Colab")
    st.write("Jupyter")
    st.write("PyCharm")

########## CSS를 사용하여 배경 이미지 변경하기 ##########

# CSS를 사용하여 배경 이미지 변경하기
st.markdown(
    """
    <style>
    body {
        background-image: url('BACKGROUND.jpg'); /* 배경 이미지 경로를 설정합니다. */
        background-size: cover; /* 이미지를 창에 맞게 확장합니다. */
        background-repeat: no-repeat; /* 이미지 반복 없음 */
        color: white; /* 글자 색상 */
        font-size: 15px; /* 글자 크기 */
        font-family: Pacifico, sans-serif; /* 글꼴 설정 */
        text-align: left; /* 텍스트 정렬 (왼쪽) */
    }
    </style>
    """,
    unsafe_allow_html=True
)