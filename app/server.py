from fastapi import Depends, FastAPI

# from app.dependencies import get_query_token


description = """
This is fast api basic template. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",    # required
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",  # if externalDocs use required
        },
    },
]

responses = {
    200: {"content": {
              "application/json": {
                  "example": {"username": "return username place"}
              }
          }},
    404: {"description": "User not Found",
          "content": {
              "application/json": {
                  "example": {"message": "User not Found"}
              }
          }},
    302: {"description": "The user was moved"},
    403: {"description": "Not enough privileges"},
    418: {"description": "this is fast exception"},
}

app = FastAPI(
              title="Fast API Template",
              description=description,
              version="0.0.1",
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": "This is contact parameters",
                  "url": "http://x-force.example.com/contact/",
                  "email": "cfd0318@gmail.com",
              },
              license_info={
                  "name": "jheok_template",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              docs_url="/docs",
              redoc_url="/redoc",
              openapi_url="/api/v1/openapi.json",
              # dependencies=[Depends(get_query_token)],
              openapi_tags=tags_metadata,
              responses=responses
              )

