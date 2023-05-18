# Observatorio Vigilancia y Seguridad Privada de Colombia. 

## Data engineering scripts

This is a private project of the **PROYECTO OBSERVATORIO SUPERVIGILANCIA.** of the Colombian Government entity **SuperIntendencia de Vigilancia y Seguridad Privadaa**. The complete datasets and complete documentation of this project is available in the intranet of the entity under access control. 

This is a Git version controlled repository to store all the scripts and code used in the proyect.

The files are stored locally, backed up by a git respository and a One-Drive account linked to the government entity intranet. This files are intended to be run from a virtual machine running ubuntu linux in the Azure cloud of the entity, automatically and on demand.

This document follows the reocmmendations listed here: https://datasciencesouth.com/blog/data-science-project-checklist/, So, please take a look in order to introduce you to the structure of the repository and documentation.

### Problem:
The particular problem of the entity is that their data is sparse and closed to the public in purpose built databases that are not totally consistent, each one serves a particular enforcement purpose and are not designed to provide ready to read data for business analytics purposes.

This project started during 2021 mapping all the data of the entity. Then we started running experiments to gather data, transform it and test if it was feasible to answer business questions with it. It was not possible in all cases. 

In order to improve efficacy, consistency and build capacity to answer even more difficult questions about the Surveillance and Private Security Sector in Colombia, it was required to have small functions that provide small datasets able to be consumed in Dashboards and analytics reports. This repository stores the result of that effort.

In the process of making this project we, a small team of 5 people have learned many useful skills necesary to make data available for a public sector entity in a professional way. This project has been in continous development and improving (sometimes in hectic ways) during most of 2021 and 2022.

## Goals

The goal of this project is to provide a way of making accessible and reproducible:
    - The ETL tasks of loading the datasets for the project 
    - The datasets (when avaliable to the general public) and the scripts for processing them
    - The result of experiments and analysis on that data
    - The reproducibility of those analysis in order to extract insights.

## Users and audience

This documentation aims to be addressed to a non technical audience who is actively in the pursuit of technical expertise in Data Science, Engineering and Analytics. This project is not totally public, so there are no public posts or web apps (Flask, Streamlit or Flask) yet. Most of the datasets are made public trhough [**Datos Abiertos**](https://datos.gov.co/) and the visualizations are made public through the [entity's website](https://supervigilancia.gov.co/) as MS-PowerBI Reports and Panels. 

The users of these scripts are personel of the entity, provided with the security clearance to access the servers and the data. It is necessary for the user to be familiarized with the documentation of the project that is stored in the entity. There are tutorials, how-to guides, examples and full blown exhaustive reference material. 

It is also expected that the user is familiarized with programing, executing and debugging Extraction, Transformation and Load rutines for datasets in Python and SQL.


## How to Set it Up

### Setup

This project requires Python 3.8.5 - setup by:
    $ pip install -r requirements.txt

Download data using:
    $ download_data.sh

### How to configure local or remote environment:

The minimal python version this project is 3.8.5. Usually it runs from a virtual environment configured using miniconda. 
The usual command to install all required libraries is:

    $ conda update conda
    $ conda create --name minimal_ds
    $ conda activate minimal_ds
    $ conda config --add channels conda-forge
    $ conda config --set channel_priority strict
    $ conda install --name minimal_ds python=3,8
    $ conda install pandas scikit-learn matplotlib notebook statsmodels openpyxl xlrd
        ? (conda install requirements.txt)
    $ Installing more libraries specifying the source:
    $ conda install -c conda-forge folium
    $ conda install -c plotly plotly_express

Details are explained hre : (https://github.com/noobiesdev/minimal_ds), and in this Medium post:  (https://medium.com/dunder-data/anaconda-is-bloated-set-up-a-lean-robust-data-science-environment-with-miniconda-and-conda-forge-b48e1ac11646)



## Use

Train a model:

    $ python3 train.py

Use a pretrained model:

    $ python3 pretrained.py


### How to Use the Project

Moving of source code out of notebooks has multiple benefits:

    - proper version control
    - reuse code in multiple notebooks
    - test code using tools like pytest


(...)

### Licence

There is no licence for this code. It is private. You have to be authorized in order to access and use it.


## Tests

Tests are another important software engineering practice that all data scientists should use. Testing code has a number of benefits:

    - tests can tell you if something breaks
    - tests make you write better code
    - tests help others understand your code

A useful form of testing are in-line assert statements. For example after splitting a dataset into test & train sets, we might want to check that our test set is smaller than our test set:

te, tr = split_dataset(data)
assert te.shape[0] < tr.shape[0]

This will fail if the something is wrong - much better than a comment that sits silently and watches the world burn.

The following is an example of the use of tests in scripts:

#### src.py
    def my_complex_function():
        return super_secret_algorithm()

#### tests.py
    from src import my_complex_function

    def test_my_complex_function():
        assert my_complex_function() == expected_result

We can then run this test suite using:

    $ pytest tests.py