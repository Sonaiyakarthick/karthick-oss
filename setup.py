
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='karthick-oss',  
     version='0.2',
     scripts=['karthick-oss'] ,
     author="karthick",
     author_email="kpskarthick1@gmail.com",
     description="karthick's open source",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Sonaiyakarthick/karthick-oss",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
