from bgt_app import app


@app.task
def add(x, y):
    result = x + y
    # logger.info(f"{x} + {y} = {result}")
    print(f"{x} + {y} = {result}")
    return result


@app.task
def sub(x, y):
    result = x - y
    # logger.info(f"{x} - {y} = {result}")
    print(f"{x} - {y} = {result}")
    return result
