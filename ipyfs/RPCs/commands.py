from ipyfs.ipfs import IPFS


class Commands(IPFS):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.completion = self.Completion(**kwargs)

    def __call__(
        self,
        flags: bool = None
    ) -> dict:
        """
        List all available commands.

        :param flags: Show command flags. Required: no.
        :return response: Response from IPFS.
        """
        return self._send(locals())

    class Completion(IPFS):

        def __init__(self,**kwargs):
            super().__init__(**kwargs)

        def bash(self) -> dict:
            """
            Generate bash shell completions.

            :return response: Response from IPFS.
            """
            return self._send(locals())
