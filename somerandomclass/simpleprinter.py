from service.loggin_service import timer


class SimplePrinter:
    """Simple printer class to illustrate how "any" class could fit into the framework.
    """
    def __init__(self, app_config):
        # TODO: You can pass app_config here. You can use app_config for authorization to DB/Storage/ES etc.
        self.app_config = app_config

    @timer
    def print_n_times(self, msg, n):
        for _ in range(n):
            print(msg)
