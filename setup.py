from setuptools import find_namespace_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    HYPEN_E_DOT='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name="DiamondPricePredictor", 
    version="0.0.1",
    author="Aviral Tripathi",
    author_email="bDgB8@example.com",                                       
    install_requires=get_requirements('requirements.txt'), 
    packages=find_namespace_packages(),)