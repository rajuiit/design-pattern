class Middleware:
    def __init__(self, next_middleware=None):
        self.next_middleware = next_middleware

    def process(self, request):
        if self.next_middleware:
            self.next_middleware.process(request)

class AuthenticationMiddleware(Middleware):
    def process(self, request):
        if "user" in request:
            print("Authentication successful.")
        else:
            print("Authentication failed.")
        super().process(request)

class LoggingMiddleware(Middleware):
    def process(self, request):
        print(f"Logging request: {request}")
        super().process(request)

class ValidationMiddleware(Middleware):
    def process(self, request):
        if "data" in request:
            print("Request data validated.")
        else:
            print("Invalid request data.")
        super().process(request)

class MiddlewareManager:
    def __init__(self):
        self.chain = None

    def add_middleware(self, middleware):
        if not self.chain:
            self.chain = middleware
        else:
            current = self.chain
            while current.next_middleware:
                current = current.next_middleware
            current.next_middleware = middleware

    def process_request(self, request):
        if self.chain:
            self.chain.process(request)


if __name__ == "__main__":
    manager = MiddlewareManager()

    # Add middleware components to the chain
    manager.add_middleware(AuthenticationMiddleware())
    manager.add_middleware(LoggingMiddleware())
    manager.add_middleware(ValidationMiddleware())

    # Create a request object
    request = {"user": "Alice", "data": "Sample data"}

    # Process the request through the middleware chain
    manager.process_request(request)
