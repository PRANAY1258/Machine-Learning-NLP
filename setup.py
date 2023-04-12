from setuptools import find_packages,setup
from typing import List


Hypen_e_dot ='-e .'
def get_requirements(file_path:str)->List[str]:
    
    

#this  function will return the list of reguriments

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        [req.replace('\n','')for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
        
setup(
name = 'NLP project',
version='0.0.1',
author= 'Pranay',
author_email= 'pranaykumar915915@gamil.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)