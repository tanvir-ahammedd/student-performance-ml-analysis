from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from requirements.txt
    """
    with open(file_path) as f:
        requirements = [line.strip() for line in f.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='student-performance-ml-analysis',
    version='0.0.1',
    author='Tanvir Ahammed',
    author_email='tanvir7535@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
