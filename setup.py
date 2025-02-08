from setuptools import find_packages,setup
from typing import List
''' this setup.py file is used to define config of requirements'''
def get_requirements() -> List[str]:
    '''
    It will return a list of requiremnts
    '''                                                     
    req_list:List[str] = []
    try: 
        with open('requirements.txt','r') as file:
            #read the lines form req file
            lines = file.readlines()
            # process each line
            for line in lines:
                req = line.strip()
                # ignore empty lines and -e.
                if req and req!= '-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("req.txt file not found")
     
    print(req_list)


setup(
    name ='Network Security',
    version='0.0.1',
    author='JyothiKumar',
    author_email='jyothikumargoud6@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)


            

