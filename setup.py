from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "src",
    version = "0.0.1",
    author = "dipak104",
    description = "Package for DVC automated ML pipeline",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/dipak104/DVC-Project",
    author_email = "dipaktripathi10@gmail.com",
    #package_dir = {"": "src"},
    #packages = find_packages(where = "src"),
    packages = ["src"],
    license = "GNU",
    python_requires = ">=3.6",
    install_requires = [
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)