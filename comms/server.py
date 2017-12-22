import os,sys, subprocess
from tinyrpc.transports import ServerTransport
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.dispatch import public, RPCDispatcher
from tinyrpc.server import RPCServer

""" This is a POC example of how to write a custom UI for the signer. The UI starts the 
signer process with the '--stdio-ui' option, and communicates with the signer binary
using standard input / output.

The standard input/output is a relatively secure way to communicate, as it does not require opening any ports
or IPC files. Needless to say, it does not protect against memory inspection mechanisms where an attacker
can access process memory."""

try:
    import urllib.parse as urlparse
except ImportError:
    import urllib as urlparse

class StdIOTransport(ServerTransport):
    """ Uses std input/output for RPC """
    def receive_message(self):
        return None, urlparse.unquote(sys.stdin.readline())

    def send_reply(self, context, reply):
        print(reply)

class PipeTransport(ServerTransport):
    """ Uses std a pipe for RPC """

    def __init__(self,input, output):
        self.input = input
        self.output = output

    def receive_message(self):
        data = self.input.readline()
        print(">> {}".format( data))
        return None, urlparse.unquote(data)

    def send_reply(self, context, reply):
        print("<< {}".format( reply))
        self.output.write(reply)
        self.output.write("\n")


class StdIOHandler():

    def __init__(self):
        pass

    @public
    def ApproveTx(self,req):
        """
        :param transaction: transaction info
        :param call_info: info abou the call, e.g. if ABI info could not be
        :param meta: metadata about the request, e.g. where the call comes from
        :return: 
        """
        return {
            "approved" : False,
            "transaction" : req.get('transaction'),
            "from" : req.get('from'),
            "password" : None,
        }

    @public
    def ApproveSignData(self,req):
        """ Example request


        """
        return {"approved": False,
                "password" : None}

    @public
    def ApproveExport(self,req):
        """ Example request

        """
        return {"approved" : False}

    @public
    def ApproveImport(self,req):
        """ Example request

        """
        return {"approved" : False, "old_password": "", "new_password": ""}

    @public
    def ApproveListing(self,req):
        """ Example request
        """
        return {'accounts': []}

    @public
    def ApproveNewAccount(self,req):
        """
        Example request

        :return:
        """
        return {"approved": False, "password": ""}

    @public
    def ShowError(self, req):
        """
        Example request:

        :param text: to show
        :return: nothing
        """
        sys.stderr.write("Error: {}\n".format( req.get('text')))
        return

    @public
    def ShowInfo(self,req):
        """

        :param text: to display
        :return:nothing
        """
        sys.stdout.write("Info: {}\n".format( req.get('text')))
        return


def connectHandler(cmd, handler):
    dispatcher = RPCDispatcher()
    print("cmd: {}".format(" ".join(cmd)))
    # line buffered
    p = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    transport = PipeTransport(p.stdout, p.stdin)
    rpc_server = RPCServer(
        transport,
        JSONRPCProtocol(),
        dispatcher
    )
    dispatcher.register_instance(handler, '')
    return (rpc_server, p)

def main(args):

    d ="/home/martin/go/src/github.com/ethereum/go-ethereum/cmd/signer/"
    cmd = ["{}/signer".format(d),
        "--4bytedb","{}/4byte.json".format(d),
        "--stdio-ui", 
        "--stdio-ui-test"]

    if len(args) > 0 and args[0] == "test":
        cmd.extend(["--stdio-ui-test"])

    handler = StdIOHandler()
    connectHandler(cmd, handler)
    handler.run()


if __name__ == '__main__':
    main(sys.argv[1:])

