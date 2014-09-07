# SimpleHistoryExample.py
import blpapi 
from optparse import OptionParser 
import inspect

def getPrice(fund, year="2014", month="09", day="05"):
    
    sessionOptions = blpapi.SessionOptions()
    sessionOptions.setServerHost("10.8.8.1")

    # Create a Session
    session = blpapi.Session(sessionOptions)
    # Start a Session
    if not session.start():
        print "Failed to start session."
        return
    try:
        # Open service to get historical data from
        if not session.openService("//blp/refdata"):
            print "Failed to open //blp/refdata"
            return
        # Obtain previously opened service
        refDataService = session.getService("//blp/refdata")
        date = year + month + day
        # Create and fill the request for the historical data
        request = refDataService.createRequest("HistoricalDataRequest")
        request.getElement("securities").appendValue(fund)
        request.getElement("fields").appendValue("PX_LAST")
        request.set("periodicityAdjustment", "ACTUAL")
        request.set("periodicitySelection", "DAILY")
        request.set("startDate", date)
        request.set("endDate", date)
        request.set("maxDataPoints", 10)
        # Send the request
        session.sendRequest(request)
        # Process received events
        while(True):
            # We provide timeout to give the chance for Ctrl+C handling:
            ev = session.nextEvent(500)
            if ev.eventType() == blpapi.Event.RESPONSE:
                for msg in ev:
                  # print msg
                  #print type(msg.getElement("securityData"))
                  result = msg.getElement("securityData").getElement("fieldData").getValueAsElement(0).getElementAsFloat("PX_LAST")#.getElement(0)#.getValueAsString("PX_LAST")
                  #print result

		  return result

                # Response completely received, so we could exit
                break
    finally:
        # Stop the session
        session.stop() 

if __name__ == "__main__":
    print "SimpleHistoryExample"
    try:
        print getPrice("VTI US EQUITY","2014","09","05") * 2
    except KeyboardInterrupt:
        print "Ctrl+C pressed. Stopping..."
