import os

from django.core.management.utils import get_random_secret_key

from lib.utils import edit_if_say_yes, save_to_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def prompt_config():
    print("Please enter Project setting:")
    debug = edit_if_say_yes(
        "We are going to use this value for DEBUG in setting.py:\n"
        "SECURITY WARNING: don't run with debug turned on in production!\n"
        "DEBUG ('y' for True / 'n' for False)", "True", value_type='bool'
    )
    allowed_host = edit_if_say_yes(
        "We are going to use this value for ALLOWED_HOSTS in setting.py:\nALLOWED_HOSTS", "['*']"
    )
    print("Please enter PostgreSQL connection details:")
    name = input("Database name: ")
    user = input("Username: ")
    password = input("Password: ")
    host = edit_if_say_yes(
        "We are going to use this value for host:\nHostname", "localhost"
    )
    port = edit_if_say_yes(
        "We are going to use this value for port:\nPort Number", 5432, value_type='number'
    )
    return [debug, allowed_host], [host, name, user, password, port]


def config_project():
    setting, conn_details = prompt_config()
    if conn_details[-1] == 5432:
        conn_details[-1] = "''"
    data = """SECRET_KEY_LOCAL = '{}'

DEBUG = {}

ALLOWED_HOSTS = {}

CONNECTION_SETTING = (
    'HOST': '{}',
    'NAME': '{}',
    'USER': '{}',
    'PASSWORD': '{}',
    'PORT': {},
)
""".format(get_random_secret_key(), setting[0], setting[1], conn_details[0], conn_details[1], conn_details[2],
           conn_details[3], conn_details[4])
    data = data.replace('(', '{')
    data = data.replace(')', '}')

    local_setting_path = os.path.join(BASE_DIR, 'instagram/local_setting.py')
    save_to_file(local_setting_path, data)
    # log_info_msg(
    #     __name__,
    #     "script configured. and config_local.py file has been created."
    # )


if __name__ == "__main__":
    config_project()
