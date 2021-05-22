from pydantic import validate_arguments


class Parent:
    def parent_method(self):
        print("parent_method")


@validate_arguments
def check_parent_arg(p: Parent):
    p.parent_method()


check_parent_arg(Parent())
# RuntimeError: no validator found for <class '__main__.Parent'>, see `arbitrary_types_allowed` in Config
