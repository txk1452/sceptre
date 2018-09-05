from sceptre.resolvers import Resolver
import json

class SSM(Resolver):
    """
    Resolver for SSM. Resolves the value stored in the parameter store.

    :param argument: The SSM parameter
    :type argument: str

    """

    def __init__(self, *args, **kwargs):
        super(SSM, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the parameter value from SSM Parameter Store.

        :returns: parameter value
        :rtype: str
        """
        decoded_value = None
        if self.argument:
            param = self.argument
            ssm_client = self.connection_manager.boto_session.client('ssm')
            print("param: ", param, " json param: ", json.dumps(param))
            meta = ssm_client.get_parameter(Name=param, WithDecryption=True)
            decoded_value = meta['Parameter']['Value']
        return decoded_value
