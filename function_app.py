import azure.functions as func
import logging
from googlesearch import search

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


# @app.function_name(name="HttpTrigger")
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    query = req.params.get("query")
    if not query:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            query = req_body.get("query")

    if query:
        results = search(query, num_results=50)
        links = []

        for link in results:
            links.append(link)

        linklist = ", ".join(links)
        return func.HttpResponse(
            linklist
            #    f"Hello. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a keyword or phrase in the query string or in the request body for a list of Google search results.",
            status_code=200,
        )
