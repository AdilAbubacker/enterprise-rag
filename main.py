def hello_world(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: Name of the person or entity to greet. Defaults to 'World'.

    Returns:
        A friendly greeting string.
    """
    message = f"Hello, {name}!"
    return message


if __name__ == "__main__":
    greeting = hello_world()
    print(greeting)
