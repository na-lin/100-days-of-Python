import requests
# TODO 2: step 2: create a graph
# "name": "Coding Time"
def create_graph(GRAPH_ID, NAME_OF_GRAPH,url)
    graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
    graph_params = {
        "id": GRAPH_ID,
        "name": NAME_OF_GRAPH,
        "unit": "minute",
        "type": "int",
        "color": "ajisai",
    }
    graph_authenticate = {
        "X-USER-TOKEN": USER_TOKEN,
    }
    graph_response = requests.post(url=graph_endpoint,json=graph_params, headers=graph_authenticate)
    print(graph_response.text)