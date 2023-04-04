import click
from dhuo_stub import DHuoStub
from persistence import persistence

stub = DHuoStub(persistence.get_username(), persistence.get_password(), None)


def create_ml_project(name, description, git_repo):
    print("Criando projeto...")

    data = stub.create_ml_project(name, description, git_repo)
    
    persistence.save_workspace_id(data["data"]["workspaceId"])


def choose_ml_projects():    
    print("Escolhendo projeto...")

    data = stub.get_ml_projects()
    data = data["data"]

    project_index = select_ml_projects(data)
    if project_index:
        project = data[project_index]        
        persistence.save_project(project["id"])
        print("Projeto configurado: " + project["name"])
    else:
        print("Nenhum projeto selecionado")


def select_ml_projects(projects):    
    print("Projetos disponíveis")

    for index, item in enumerate(projects):
        print(index + 1, item["name"])

    project_index = click.prompt('Informe o Id do Projeto', type=int)
    return project_index - 1
