class DataProvider:
    """
    Decorator for unittest tests

    Usage example:

    @staticmethod
    def data():
        return (x1, y1), (x2, y2)

    @DataProvider("data")
    def test_with_data(self, x, y):
        self.assertEqual(x, y)
    """
    def __init__(self, data_provider_name):
        self.data_provider = data_provider_name

    def __call__(self, test_function):
        def decorator(test_class_instance):
            data_provider_object = test_class_instance.__class__.__dict__[self.data_provider]
            for test_values in data_provider_object.__func__():
                test_function(test_class_instance, *test_values)

        return decorator
