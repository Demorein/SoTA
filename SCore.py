class SoTACore():
    #Read json file. Returns a list
    #EXAMPLE: print(_json_read(file)["Variable"])
    def _json_read(file:str) -> str:
        import json
        with open(file, "r") as f:
            return(json.load(f))
        
    #Write Log in file, Returns None
    #EXAMPLE: _log("Hello", log)
    def _logs(log:str, file:str) -> None:
        with open(f"{file}.txt", "a") as f:
            f.write(f"{log}")

    #Returns a list with date and time
    #EXAMPLE1: _time()[0] --> return(time)
    #EXAMPLE2: _time()[0] --> return(date)
    def _time() -> str:
        import datetime
        dt = datetime.datetime.now()
        nowtime = dt.time()
        nowdate = dt.date()
        return([f"{nowtime.hour}:{nowtime.minute}:{nowtime.second}",f"{nowdate.day}.{nowdate.month}.{nowdate.year}"])
        