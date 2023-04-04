import requests
from openid import OpenId

class DHuoStub():

    def __init__(self, username, password, workspace_id: None) -> None:
        self.host = "https://backend-dhuo-data-stg.br.engineering"
        self.openid = OpenId(username, password)

        self.workspace_id = workspace_id


    def get_ml_projects(self):  # noqa: E501
        """Get MLProjects with pagination  # noqa: E501

        :return: HandlersResponseGetMLProjects
        """   
        self.openid.refresh_user_info()

        endpoint = f"/v1/workspaces/{self.openid.workspace}/ml/projects"
        url = self.host + endpoint

        headers = {}        
        headers = self.openid.fill_auth_header(headers)     

        response = requests.get(url, headers=headers)
    
        return response.json()
    

    def create_ml_project(self, name, description, git_repo): 
        """Create a MLProject  # noqa: E501
        """
        self.openid.refresh_user_info()

        endpoint = f"/v1/workspaces/{self.openid.workspace}/ml/projects"
        url = self.host + endpoint

        headers = {}        
        headers = self.openid.fill_auth_header(headers)     

        payload = {}
        payload["id"] = "id"
        payload["workspaceId"] = self.openid.workspace
        payload["name"] = name
        payload["description"] = description
        payload["gitRepo"] = git_repo

        response = requests.request("POST", url, headers=headers, json=payload)        

        return response.json()
    

    def create_ml_experiment(self, project_id, experiment_name, description): 
        """Create a MLExperiment  # noqa: E501 """
        self.openid.refresh_user_info()

        endpoint = f"/v1/workspaces/{self.workspace_id}/ml/projects/{project_id}/experiments"
        url = self.host + endpoint

        headers = {}        
        headers = self.openid.fill_auth_header(headers)  

        payload = {}
        payload["experimentName"] = experiment_name
        payload["description"] = description
        payload["projectId"] = project_id

        response = requests.request("POST", url, headers=headers, json=payload)        

        return response.json()
    

    def create_ml_execution(self, params): 
        """Update a MLExecution  # noqa: E501 """
        self.openid.refresh_user_info()
        
        endpoint = f"/v1/workspaces/{self.workspace_id}/ml/projects/{params['project_id']}/experiments/{params['experiment_id']}/executions"
        url = self.host + endpoint

        headers = {}        
        headers = self.openid.fill_auth_header(headers)  

        payload = {}
        payload["executionName"] = params['execution_name']
        payload["experimentId"] = params['experiment_id']
        payload["model"] = params['model']
        payload["source"] = params['source']
        payload["user"] = params['user']
        payload["version"] = params['version']

        response = requests.request("POST", url, headers=headers, json=payload)         
        data = response.json()
        execution_id = data["data"]["id"]

        endpoint = f"/v1/workspaces/{self.workspace_id}/ml/projects/{params['project_id']}/experiments/{params['experiment_id']}/executions/{execution_id}"
        url = self.host + endpoint

        #payload["id"] = execution_id

        #response = requests.request("PUT", url, headers=headers, json=payload)         

        #data = response.json()
        #print(url)
        #print(payload)
        #print(data)

        return response.json()


if __name__ == "__main__":
    from persistence import persistence
    stub = DHuoStub(persistence.get_username(), persistence.get_password(), persistence.get_workspace_id())
    
    stub.create_ml_project("Projeto Novo", "Descrição de Projeto", "git@github.com")
    print(stub.get_ml_projects())

    data = stub.create_ml_experiment(persistence.get_project(), "Novo experimento", "Uma breve descrição")
    experiment_id = data["data"]["id"]
    
    params = {}
    params["execution_name"] = "training lr"
    params["experiment_id"]  = "dfffa769-024d-4bc2-8266-416a9be93100"
    params["source"] = "script.py"
    params["user"] = "AC"
    params["model"] = None        
    params["version"] = None
    params["project_id"] = persistence.get_project()

    stub.create_ml_execution(params)
