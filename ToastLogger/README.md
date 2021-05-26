# JSON Logger Python

Easy JSON Logger for Python3
(I made this to get JSON log easily)

## Usage
```python
from JsonLog import JsonLog
from JsonLog import Log as log

try:
    <code>
except:
    log("[SYSTEM] Error...", "ERROR")  # log("message", "Log Level")
  # log("My Error: {}".format(err), "ERROR")
```

- You can add a ENV VAR like -> `DEBUG_LOGS=true`
```python
#CHECK DEBUG ENV VAR
env_debug = os.environ.get("DEBUG_LOGS")
debug = False
if env_debug is None or env_debug.lower() != "true":
    debug = False
else:
    debug = True
```

## Log types (you can add directly in JsonLog.py)
```
ERROR
INFO
DEBUG
```
