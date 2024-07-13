from setuptools import find_packages,setup

setup(
    name='qna',
    version='0.0.1',
    author='Rittik Raj',
    author_email='rittikrajchauhan123@gmail.com',
    install_requires=["google-generativeai","langchain","streamlit",
                      "python-dotenv","PyPDF2","langchain_google_genai","pinecone-client","tiktoken"],
    packages=find_packages()
)