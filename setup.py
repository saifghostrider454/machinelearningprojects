from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."
def get_requirements(path: str) -> list[str]:
    """
    This function will return the list of requirements
    """

    requirements = []

    with open(path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    

setup(
    name="Machine Learning Project",
    version="0.0.1",
    author="Saif",
    author_email="ansarimdsaif742@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)