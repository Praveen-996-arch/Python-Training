TOKEN = "a234nmkjkjhsf987"
import requests
from datetime import datetime


parameters = {
    "token": TOKEN,
    "username":"manasapola",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url="https://pixe.la/v1/users",json = parameters)
# response.raise_for_status()
# print(response.text)
# graph_parameters = {
#     "id": "Health-Tracking1",
#     "name": "Health Tracking Graph",
#     "unit": "calories",
#     "type": "int",
#     "color": "ajisai"
# }


# graph_response = requests.post(url="https://pixe.la/v1/users/manasapola/graphs", json=graph_parameters,headers = {"X-USER-TOKEN": TOKEN})
# graph_response.raise_for_status()
# print(graph_response.text)

# post_value_parameters={
#     "date":datetime.now().date().strftime("%Y%m%d"),
#     "quantity":"300"
# }

# post_value_response = requests.post(url="https://pixe.la/v1/users/manasapola/graphs/health-tracking1", json=post_value_parameters, headers={"X-USER-TOKEN": TOKEN})
# post_value_response.raise_for_status()
# print(post_value_response.text)



# put_value_parameters={
#     "quantity":"400"
# }

# put_value_response = requests.put(url="https://pixe.la/v1/users/manasapola/graphs/health-tracking1/20260403", json=put_value_parameters, headers={"X-USER-TOKEN": TOKEN})
# put_value_response.raise_for_status()
# print(put_value_response.text)



delete_value_response = requests.delete(url="https://pixe.la/v1/users/manasapola/graphs/health-tracking1/20260403",  headers={"X-USER-TOKEN": TOKEN})
delete_value_response.raise_for_status()
print(delete_value_response.text)
