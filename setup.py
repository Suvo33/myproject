from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
        This is a function that will return list ogf requirements  
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n','') for req in requirements ]
        if "-e ." in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='mlproject',
    author='Subhajit Manna',
    version='0.0.1',
    email='subhajitmanna2122@gmail.com',
    packages=find_packages(),
    install_requitres=get_requirements('requirements.txt')


)