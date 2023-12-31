from tests.utils.patches import PatchedResponses, PRKey, PRValue


class CommonPatchedResponses(PatchedResponses):
    mappings = {
        PRKey(
            url="https://www.python.org",
            method="get"
        ): PRValue(
            status_code=200,
            content=b"python_org_content"
        ),
        PRKey(
            url="",
            method=""
        ): PRValue(
            status_code=200,
            content=b""
        ),
    }
