from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return a list of packages from requirements.txt
    """
    requirements=[]
    with opne(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    name="Tech-Job-Recommendation",
    version="0.1",
    author="MoRaouf",
    author_email="m.raouf.ai@outlook.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=get_requirements()
)
