from ipyfs.ipfs import IPFS


class Add(IPFS):

    def __call__(
        self,
        file = None,
        quiet: bool = None,
        quieter: bool = None,
        silent: bool = None,
        progress: bool = None,
        trickle: bool = None,
        only_hash: bool = None,
        wrap_with_directory: bool = None,
        chunker: str = None,
        pin: bool = None,
        pin_name: str = None,
        raw_leaves: bool = None,
        nocopy: bool = None,
        fscache: bool = None,
        cid_version: int = None,
        hash: str = None,
        inline: bool = None,
        inline_limit: int = None,
        to_files: str = None,
        files: dict = None,
    ) -> dict:
        """
        Add a file or directory to IPFS.

        :param file: File to add. Required: yes, unless files is passed.
        :param quiet: Write minimal output. Required: no.
        :param quieter: Write only final hash. Required: no.
        :param silent: Write no output. Required: no.
        :param progress: Stream progress data. Required: no.
        :param trickle: Use trickle-dag format for dag generation. Required: no.
        :param only_hash: Only chunk and hash - do not write to disk. Required: no.
        :param wrap_with_directory: Wrap files with a directory object. Required: no.
        :param chunker: Chunking algorithm, size-[bytes], rabin-[min]-[avg]-[max] or buzhash. Default: size-262144. Required: no.
        :param pin: Pin this object when adding. Default: true. Required: no.
        :param pin_name: Name to use for the pin.Required: no.
        :param raw_leaves: Use raw blocks for leaf nodes. Required: no.
        :param nocopy: Add the file using filestore. Implies raw-leaves. (experimental). Required: no.
        :param fscache: Check the filestore for pre-existing blocks. (experimental). Required: no.
        :param cid_version: CID version. Defaults to 0 unless an option that depends on CIDv1 is passed. Passing version 1 will cause the raw-leaves option to default to true. Required: no.
        :param hash: Hash function to use. Implies CIDv1 if not sha2-256. (experimental). Default: sha2-256. Required: no.
        :param inline: Inline small blocks into CIDs. (experimental). Required: no.
        :param inline_limit: Maximum block size to inline. (experimental). Default: 32. Required: no.
        :param to_files: Add reference to Files API (MFS) at the provided path. Required: no.
        :param files: add multiple files - see requests.request => files parameter 
        :return response: Response from IPFS.
        """
        if file is None and files is None:
            raise(TypeError(" missing one of required : first positional argument: 'file' or keyword argument: 'files'"))
        replace = {
            "only_hash": "only-hash",
            "wrap_with_directory": "wrap-with-directory",
            "raw_leaves": "raw-leaves",
            "cid_version": "cid-version",
            "inline_limit": "inline-limit",
            "to_files": "to-files",
            "pin_name": "pin-name"
        }
        return self._send(
            params=locals(),
            replace=replace,
            file=file,
            files=files
        )
