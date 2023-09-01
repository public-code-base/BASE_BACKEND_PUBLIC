import __init__
import asyncio
import uvicorn
import kthread
import time
import threading
import settings.settings as settings
import helper.json_func as json_func
from decouple import config
from logs.logger import logs_sys, logs_dev, lprint
from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Create routers
router_root = APIRouter()
router_telegram = APIRouter()

@router_root.get("/")
@limiter.limit("500/minute")
async def home(request: Request):
    return f"Version: {settings.VERSION} ::: Environment: {settings.ENVIRONMENT}"

@router_root.post("/ping")
@limiter.limit("500/minute")
async def ping(request: Request):
    """
    Route: /v1/ping
    """
    return "success"

@router_telegram.post("/send_any")
@limiter.limit("500/minute")
async def send_any(request: Request, item: dict):
    def internal_send_any(json_payload):
        logs_sys.info("An Incoming Payload...")
        message = json_payload.get("message")
        bot_name = json_payload.get("bot_name")
        result = True # Replace this line
        if result != None:
            logs_sys.info("Successfully Processed Incoming Payload")
        else:
            logs_sys.error("Unable to Process Incoming Payload")
            
    # result, error_msg = payload_check_valid.CheckValidPayload(item).check_if_valid_key()
    # print(f"result: {result}, error_msg: {error_msg}")
    # if result is not False:
    #     settings.FUNC_SYNC_INQUEUE.put_nowait(lambda: internal_send_any(item)) 
    #     return JSONResponse(status_code=200, content={"message": "Payload is valid"})
    # else:
    #     raise HTTPException(status_code=400, detail=error_msg)



# Create main application and include routers

app.include_router(router_root, prefix=f'/api', tags=["default"])
app.include_router(router_telegram, prefix=f'/api/telegram', tags=["telegram"])

def start_server():
    if settings.ENVIRONMENT in ["SANDBOX", "LOCAL"]:
        uvicorn.run(app, host="localhost", port=8989)
    else:
        uvicorn.run(app, host="0.0.0.0", port=8989)

class Server:
    def start():
        if settings.SERVER_THREAD == None:
            def run():
                try: start_server()
                except: pass
                logs_sys.alert(f"API Server has stopped running")
                time.sleep(1)
                settings.ASYNCIO_LOOP = False
                
            settings.SERVER_THREAD = kthread.KThread(target=run, args=(), daemon=True)
            settings.KNOWN_KTHREADS.append(settings.SERVER_THREAD)
            settings.SERVER_THREAD.start()
            logs_sys.info("Server started running")
        return "success"
        
    def shutdown():
        if settings.SERVER_THREAD != None:
            try:
                settings.SERVER_THREAD.kill()
            except:
                pass
            if settings.SERVER_THREAD in settings.KNOWN_KTHREADS:
                settings.KNOWN_KTHREADS.remove(settings.SERVER_THREAD)
            settings.SERVER_THREAD = None
            logs_sys.info("Server shutdown")
        else:
            logs_sys.info("Server is not running")
        return "success"
    
if __name__ == '__main__':
    time.sleep(2)
    logs_dev.info("Server has stopped running")
    start_server()
