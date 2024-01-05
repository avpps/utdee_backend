from tests.utils.patches import PatchedResponses, PRKey, PRValue


class CommonPatchedResponses(PatchedResponses):
    url = "https://www.python.org"
    url_failing = "https://www.fail.org"
    mappings = {
        PRKey(
            url=url,
            method="get"
        ): PRValue(
            status_code=200,
            content=b"python_org_content"
        ),
        PRKey(
            url=url_failing,
            method="get"
        ): PRValue(
            status_code=404,
            content=b"bad request"
        ),
    }
