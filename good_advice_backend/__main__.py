import logging

import uvicorn

logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(name)s:%(lineno)s:%(message)s",
    level="DEBUG",
)
logging.getLogger("asyncio").setLevel(logging.WARNING)

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
