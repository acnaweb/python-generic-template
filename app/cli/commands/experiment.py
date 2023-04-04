from dhuo_stub import DHuoStub
from persistence import persistence


def create_ml_experiment(project_id, experiment_name, description):
    print("Criando experimento...")

    stub = DHuoStub(persistence.get_username(), persistence.get_password(), persistence.get_workspace_id())

    stub.create_ml_experiment(project_id, experiment_name, description)
