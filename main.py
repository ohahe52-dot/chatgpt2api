from __future__ import annotations

import os
import uvicorn
from api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        access_log=False,
        log_level="info"
    )
