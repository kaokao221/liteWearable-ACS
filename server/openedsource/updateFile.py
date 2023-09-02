from fastapi import FastAPI, File, UploadFile
import fastapi.responses as responses
import json, time, uvicorn

main = FastAPI()

@main.get("/favicon.ico")
async def favicon():
    return responses.FileResponse("favicon.ico")

@main.post("/uploadFile")
async def uploadFile(file: UploadFile, keepTime: int = 7200, dowmloadCount: int = -1):
    with open("")

@main.get("/")
async def app():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadFile" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return responses.HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run(app=main, host="127.0.0.1", port=7774)
