from dhuo_stub import DHuoStub
from persistence import persistence


def create_ml_execution(params): 
    print("Criando execução...")

    stub = DHuoStub(persistence.get_username(), persistence.get_password(), persistence.get_workspace_id())
    stub.create_ml_execution(params)
