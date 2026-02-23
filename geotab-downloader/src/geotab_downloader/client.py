import os

import mygeotab


def create_geotab_client(username: str, database: str, password: str) -> mygeotab.API:
    if not is_session_saved(username, database):
        session_id = get_new_session_id(username, database, password)
        save_session_id(username, database, session_id)
        return mygeotab.API(
            username=username,
            database=database,
            session_id=session_id,
        )

    session_id = load_saved_session(username, database)
    if not is_session_valid(
        username=username, database=database, session_id=session_id
    ):
        session_id = get_new_session_id(username, database, password)
        save_session_id(username, database, session_id)

    return mygeotab.API(
        username=username,
        database=database,
        session_id=session_id,
    )


def get_new_session_id(username: str, database: str, password: str) -> str:
    api = mygeotab.API(
        username=username,
        database=database,
        password=password,
    )
    api.authenticate()
    return api.credentials.session_id


def is_session_saved(username: str, database: str) -> bool:
    cached_session = session_filename(username, database)
    return os.path.exists(cached_session)


def load_saved_session(username: str, database: str) -> str:
    cached_session = session_filename(username, database)
    with open(cached_session, "r") as f:
        session_id = f.read().strip()
    return session_id


def save_session_id(username: str, database: str, session_id: str):
    cached_session = session_filename(username, database)
    with open(cached_session, "w") as f:
        f.write(session_id)


def session_filename(username: str, database: str) -> str:
    return f"./geotab-session-{username}@{database}"


def is_session_valid(username: str, database: str, session_id: str) -> bool:
    api = mygeotab.API(
        username=username,
        database=database,
        session_id=session_id,
    )
    try:
        api.call("Get", typeName="User", search={"name": username})
    except mygeotab.AuthenticationException:
        return False
    return True
