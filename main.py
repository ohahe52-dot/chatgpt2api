from __future__ import annotations

import os
import uvicorn
from api import create_app

app = create_app()

PORT = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        reload=False
    )
