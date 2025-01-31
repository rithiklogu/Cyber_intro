from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            print("Raw lines from file:", lines)  # Debugging line

            for requirement in lines:
                requirement = requirement.strip()  # Remove spaces & newlines
                print("Processing requirement:", requirement)  # Debugging line
                
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("Could not find requirements.txt")

    return requirements_lst

print("Final requirements list:", get_requirements())
