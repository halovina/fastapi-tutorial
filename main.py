
from fastapi import FastAPI, Request
from routers import users, items
from routers.controllers import ItemException
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)


@app.exception_handler(ItemException)
async def item_exception_handler(request: Request, exc: ItemException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.item_id} did something. There goes a rainbow..."},
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}


