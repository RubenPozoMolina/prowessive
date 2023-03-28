from code.function_utils import create_function

query_files = """
SELECT path, file_bytes FROM files
"""


class FrontEnd:
    flask_application = None
    database = None

    def __init__(self, flask_application, database):
        self.flask_application = flask_application
        self.database = database

    def load_urls_from_database(self):
        files = self.database.query(query_files)
        for file in files:
            path = file[0]
            file_content = bytes(file[1])
            func_name = path.replace('.', '_').replace('/', '_')
            arguments = ''
            code = f"""
            from flask import make_response
            response = make_response({file_content})
            # response.headers.set('Content-Type', 'text/html')
            return response
            """
            func = create_function(func_name, arguments, code)
            self.flask_application.add_url_rule(path, func_name, view_func=func)

    @staticmethod
    def example_page():
        return """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Example</title>
            </head>
            <body>
                <p>This is an example of a simple HTML page with one paragraph.</p>
            </body>
        </html> 
        """