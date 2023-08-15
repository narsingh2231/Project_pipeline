from setuptools import setup, find_packages

setup(name = "centus-income",
      version = "0.0.1",
      author ="Narsingh Maurya",
      author_email = "narsingh2231@gamil.com",
      packages= find_packages(),
      install_requires= ["pandas", "numpy", "flask"]
      )