import sys

from twisted.python import log
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

import json
import properties as helper

class MyServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        print("WebSocket connection open.")

    def onConnect(self, request):
        # I have no idea if this is a good practice
        self.memory = {}

        print("Client connecting: {0}".format(request.peer))

    def onMessage(self, payload, isBinary):

        # Not handling binary data
        if isBinary:
            return

        data = json.loads(payload.decode('utf8'))

        if 'cmd' not in data or 'args' not in data:
            # Reject
            print 'Rejected! Message does not contain the keys \'cmd\' and \'args\'.'
            return

        if data['cmd'] == 'LOAD_GRAPH':
            print 'Loading graph: %s' % data['args'][0]
            self.memory['graph'] = helper.loadGraph(data['args'][0])

            print 'Graph %s loaded!' % data['args'][0]
            self.sendMessage(json.dumps({
                'type': 'RETURN',
                'value': 0,
                }).encode('utf8'), False)

        elif data['cmd'] == 'GET_PROPERTIES':
            if 'graph' not in self.memory:
                self.sendMessage(json.dumps({
                    'type': 'ERROR',
                    'value': 'No graph is loaded yet!'
                    }).encode('utf8'), False)

                return

            graph = self.memory['graph']
            out_arr = []
            out_arr.append(helper.plotInDegDistr(graph))
            out_arr.append(helper.plotOutDegDistr(graph))
            out_arr.append(helper.plotSccDistr(graph))
            out_arr.append(helper.plotWccDistr(graph))
            out_arr.append(helper.plotClustCf(graph))

            self.sendMessage(json.dumps({
                'type': 'RETURN',
                'value': out_arr
                }).encode('utf8'), False)

        elif data['cmd'] == 'GEN_SCALE_FREE':
            print 'Generating scale-free network'
            self.memory['graph'] = helper.genScaleFree(N=10000)

            print 'Scale-free network is successfully generated'
            self.sendMessage(json.dumps({
                'type': 'RETURN',
                'value': 0,
                }).encode('utf8'), False)

        else:
            self.sendMessage(json.dumps({
                'type': 'ERROR',
                'value': 'Unknown command error!'
                }).encode('utf8'), False)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


host = 'localhost'
port = 8888

log.startLogging(sys.stdout)

factory = WebSocketServerFactory('ws://%s:%d' % (host, port))
factory.protocol = MyServerProtocol
# factory.setProtocolOptions(maxConnections=2)

# note to self: if using putChild, the child must be bytes...

reactor.listenTCP(port, factory)
reactor.run()
