from states.user_state import UserState


def update_UserState_action(func):
    def wrapper(*args, **kwargs):
        UserState.action = func.__name__
        return func(*args, **kwargs)
    return wrapper
