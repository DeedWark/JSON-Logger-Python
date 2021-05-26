class JsonLog:
    import logging
    import json_log_formatter
    formatter = json_log_formatter.JSONFormatter() 
    json_handler = logging.StreamHandler()  # .FileHandler(filename="salesdesk_logs.json") to export logs in file
    json_handler.setFormatter(formatter)
    logger = logging.getLogger('log_json')
    logger.addHandler(json_handler)
    logger.setLevel(logging.INFO)

def Log(message, level):
    if level.lower() == "error":
        level = "ERROR"
        typelvl = JsonLog.logger.error("{}".format(message), extra={'level': '{}'.format(level)})
    elif level.lower() == "debug":
        level = "DEBUG"
        typelvl = JsonLog.logger.info("{}".format(message), extra={'level': '{}'.format(level)})
    else:
        level = "INFO"
        typelvl = JsonLog.logger.info("{}".format(message), extra={'level': '{}'.format(level)})

    try:
        typelvl
    except:
        print('{"level": "ERROR-Logger", "message": "Error when formating string but we can continue!", "time": "NOW"}')