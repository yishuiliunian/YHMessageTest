from flask import Flask
from flask import request
app = Flask(__name__)


ANALYSIS_MAP = {}
UI_ANA_MAP = {}
SERVER_CACHE_MAP = {}

@app.route('/reportsend')
def reportSend():
    if request.method == 'GET':
        msgID = request.args.get("msgID","")
        print("get send msgID %s" % (msgID))
        if msgID != None:
            ANALYSIS_MAP[msgID] = msgID
            UI_ANA_MAP[msgID] = msgID
            SERVER_CACHE_MAP[msgID] = msgID
        else:
            print("ERROR ! No args")
        return "{\"ret\":0}"
        pass
    pass

@app.route('/reportrecive')
def reportRecive():
    if request.method == 'GET':
        msgID = request.args.get("msgID","")
        print("get revicved DB message %s" % (msgID))
        if msgID != None:
            if msgID in ANALYSIS_MAP:
                del ANALYSIS_MAP[msgID]
            else:
                print("FAILED the msgID[%s] not exist in map" % (msgID))
        else:
            print("ERROR ! No args")
        return "{\"ret\":0}"

@app.route('/reportuirecive')
def reportUIRecive():
    if request.method == 'GET':
        msgID = request.args.get("msgID","")
        print("get revicved UI message %s" % (msgID))
        if msgID != None:
            if msgID in UI_ANA_MAP:
                del UI_ANA_MAP[msgID]
        else:
            print("ERROR ! No args")
        return "{\"ret\":0}"


@app.route('/reportcacherecive')
def reportCacheRecive():
    if request.method == 'GET':
        msgID = request.args.get("msgID","")
        print("get revicved UI message %s" % (msgID))
        if msgID != None:
            if msgID in SERVER_CACHE_MAP:
                del SERVER_CACHE_MAP[msgID]
        else:
            print("ERROR ! No args")
        return "{\"ret\":0}"

@app.route('/result')
def repotResult():
    ret = "The follows are not recived:\n"
    for eachKey in ANALYSIS_MAP.keys():
        ret = ret + "\n" + eachKey
    ret = ret+"\n UI not recived:\n"
    for eachKey in UI_ANA_MAP.keys():
        ret = ret + "\n" + eachKey
    ret = ret+"\n Cache not recived:\n"
    for eachKey in SERVER_CACHE_MAP.keys():
        ret = ret + "\n" + eachKey
    return ret

if __name__ == "__main__":
    app.debug = True
    app.run(host='172.24.102.137')
