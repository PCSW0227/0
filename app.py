
import streamlit as st
from PIL import Image  # 이 줄을 추가
from Project_Module import project1, project2

# 나머지 코드는 그대로 두면 됩니다.


# 타이틀 및 간단한 설명
st.title("Welcome to Minji's Portfolio")
# 상단 메뉴
menu = st.selectbox("Click", ["Projects", "Technical Stack", "Education", "Work Experience", "Identity"])


projects = [project1, project2]


# Projects 섹션
if menu == "Projects":
    st.header("Projects")
    selected_project_name = st.selectbox("Select a project", [p.name for p in projects])
    selected_project = next((p for p in projects if p.name == selected_project_name), None)

    if selected_project is not None:
        for img_path in selected_project.images:
            img = Image.open(img_path)  # 이미지 파일 열기
            st.image(img, caption=selected_project_name, use_column_width=True)

        st.write(selected_project.description)

# Identity 섹션
elif menu == "Identity":
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
    st.write("The Master of Big Data Analysis Convergence program")
    st.write("at Sookmyung Women's University is a comprehensive program")
    st.write("that focuses on advanced data analysis techniques, artificial intelligence, and data management.")
    st.write("This program equips students with the skills")
    st.write("to extract valuable insights from large datasets and make data-driven decisions,")
    st.write("contributing to the rapidly growing field of data science.")
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
    st.write("■  Innovative Patent Human Resource Development (IP HRD)")
    st.write("is an AI patent education project supported by the Patent Office")
    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.header("Experience 2: NONGHYUB")
    st.write("■  Job Position: Credit and deposit data analysis, statistics")
    st.write("■  While working at Nonghyup, I was responsible for credit and deposit operations,")
    st.write("supporting financial data analysis and efficient decision-making.")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.header("Experience 1: Samsung Seoul Hospital")
    st.write(" ■  Job Position: Medical Billing, Customer Service")


# Technical Stack 섹션
elif menu == "Technical Stack":
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


# 배경 이미지 파일 경로 설정
background_image_path = "C:/Users/wkdal/Desktop/2023/02. 프로젝트/06. 쿠폰/BACKGROUND/BACKGROUND IMAGE.png"


# 배경 이미지 적용을 위한 스트림릿 코드
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('{background_image_path}') no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True)
