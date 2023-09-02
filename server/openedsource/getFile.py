from fastapi import FastAPI
import fastapi.responses as responses
import json, time, uvicorn

main = FastAPI()

@main.get("/favicon.ico")
async def favicon():
    return responses.FileResponse("favicon.ico")

@main.get("/getFile")
async def getFile(token: str | None = None):
    with open("/workspaces/liteWearable-ACS/server/openedsource/files/getFile/getFile.json", "r", encoding = "utf-8") as f:
        getFiles = json.load(f)
        if not token is None:
            try:
                print(token)
                if time.time() - getFiles[token]["createTime"] <= getFiles[token]["keepTime"] and not getFiles["downloadCount"] == 0:
                    getFiles[token]["downloadCount"] -= 1
                    return responses.FileResponse(getFiles[token])
                elif time.time() - getFiles[token]["createTime"] > getFiles[token]["keepTime"]:
                    return {"message": "token is overdue"}
                else:
                    return {"message": "token is no more aviliable"}
            except:
                return {"message": "token is not valid"}

if __name__ == "__main__":
    uvicorn.run(app=main, host="127.0.0.1", port=7775)

