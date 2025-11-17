from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(filepath: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(filepath) as fileobj:
        requirements = [line.strip() for line in fileobj if line.strip() and not line.strip().startswith('#')]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements




setup(
    name='ML project',
    version='0.0.1',
    author='Tachafine',
    author_email='otachafine@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)