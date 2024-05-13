import requests

class AuthService:
    __host = None
    __port = None

    def __init__(self, host, port=8001):
        self.__host = host
        self.__port = port

    def check_permissions(self, permissions, endpoint):
        url = f"http://{self.__host}:{self.__port}/rbac-service/check-permissions/"
        print("this is the url", url)
        headers = {"Content-Type": "application/json"}
        data = {
            "permissions": permissions,
            "endpoint": endpoint
        }

        try:
            print("this is from the auth service")
            response = requests.post(url, json=data, headers=headers)
            print("this is the response from te other project", response)
            return response.json()
        except requests.HTTPError as e:
            print("Error:", e)
            return {"error": "Failed to check permissions"}
