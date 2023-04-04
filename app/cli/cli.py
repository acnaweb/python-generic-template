from typing import Optional
from persistence import persistence
from commands.login import login
from commands.project import create_ml_project, choose_ml_projects
from commands.experiment import create_ml_experiment
from commands.execution import create_ml_execution



# login
# list projects
# create project

if __name__ == "__main__":

    # dh login    
    login("antonioclj.ac@gmail.com", "Pwd@9051")

    # dh create
    create_ml_project("projeto xpto", "Projeto do CLI", "gitlab.com")
    # salvar o projeto criado 
    
    choose_ml_projects()

    create_ml_experiment(persistence.get_project(), "Experimento 1", "Descrição do experimento 1")


    create_ml_execution




