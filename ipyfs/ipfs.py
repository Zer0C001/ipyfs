import sys
import requests
import json
from collections import defaultdict


class IPFS:
    def __init__(
        self,
        host: str = "http://localhost",
        port: int = 5001,
        version: int = 0,
        response_return_status_code: bool = True,
        init_self_attr_RPCs: bool or list  = False,
    ):
        self.host = host
        self.port = port
        self.version = version
        self.uri = (
            f"{self.host}:{self.port}"
            f"/api/v{self.version}"
            f"/{self.__class__.__module__.split('.')[-1].lower()}"
        )
        class_name = self.__class__.__name__.lower()
        self.response_return_status_code=response_return_status_code
        if class_name not in self.uri:
            self.uri += f"/{class_name}"
        if self.__class__.__name__=='IPFS' and init_self_attr_RPCs:
            from . import RPCs
            if type(init_self_attr_RPCs) is list:
                rpc_objects=[ obj.capitalize() for obj in init_self_attr_RPCs if obj.capitalize() in dir(RPCs) and type(getattr(RPCs,obj.capitalize())) is type ]
                rpc_objects+=[ obj.upper() for obj in init_self_attr_RPCs if obj.upper() in dir(RPCs) and type(getattr(RPCs,obj.upper())) is type ]
            else:
              rpc_objects=[ obj for obj in dir(RPCs) if type(getattr(RPCs,obj)) is type ]
            for rpc_object in rpc_objects:
                setattr(self,rpc_object.lower(),getattr(RPCs,rpc_object)(host=host,port=port,version=version,response_return_status_code=response_return_status_code))



    @staticmethod
    def _response(response: requests.Response,response_return_status_code=True) -> dict:
        try:
            result = response.json()
        except:
            result = response.text
            if result == '':
                result = None
            else:
                try:
                    result=[ json.loads(r) for r in result.splitlines() ]
                except:
                    pass
        if response.status_code != 200:
            raise Exception(result)
        if response_return_status_code:
            return {
                "status_code": response.status_code,
                "result": result
            }
        else:
            return(result)

    def _send(
        self,
        params: dict,
        replace: dict = None,
        file=None,
        files: dict = None
    ) -> dict:
        """
        Request to IPFS.
        """
        # Generate URI
        method = sys._getframe(1).f_code.co_name
        uri = self.uri
        if method != '__call__':
            uri += f"/{method}"

        # Generate Params
        data = defaultdict(list)
        for key, value in params.items():
            if not value or key in ('self', 'replace', 'file'):
                continue
            if replace and key in replace:
                data[replace[key]].append(value)
            else:
                data[key].append(value)
        for key, value in data.items():
            if len(value) == 1:
                data[key] = value[0]

        # Send Request
        return self._response(
            requests.post(
                url=uri,
                params=data,
                files={'file': file} if files is None else {'file': file , **files}
            ),self.response_return_status_code
        )
