from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#No, the correct syntax for defining the return type in the function signature is using -> The -> arrow indicates the return type of the function.
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    #we creat the empty list []
    requirements=[]
    
    #This opens the file specified by file_path in a context manager. It ensures that the file is properly closed after reading its contents.
    with open(file_path) as file_obj:
        
 #This reads all the lines from the file and stores them as a list of strings in the requirements variable. 
#Each line in the file becomes an item in the list.       
        requirements=file_obj.readlines()
#        
        requirements=[req.replace("\n","") for req in requirements]
        
#This conditional statement checks if the string stored in HYPEN_E_DOT exists in the requirements list. 
# If it does, the remove() method is called to remove the occurrence of HYPEN_E_DOT from the list.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
#Finally, the function returns the requirements list, which contains the parsed requirements from the file.    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Ketan Salian',
author_email='ketan.salian3@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)