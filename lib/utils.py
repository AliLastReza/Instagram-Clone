# from khayyam import JalaliDate, jalali_datetime
# from unidecode import unidecode
# from logger import file_logger


# def jalali_datetime_now():
#     return jalali_datetime.JalaliDatetime.now()
#
#
# def convert_to_jalali(datetime_obj):
#     return jalali_datetime.JalaliDatetime(datetime_obj)
#
#
# def log_inserted_instance_count(inserted_count, model_name):
#     file_logger.info(": {} {} model instances added to {} table.".format(
#         ':::::', inserted_count, model_name
#     ))
#
#
# def log_instance_added_to_table(module, instance_name, table_name):
#     log_info_msg(
#         module, "{} model instance has been added to {} table.".format(
#             instance_name, table_name
#         )
#     )
#
#
# def log_instance_exist_in_table(module, instance_name, table_name):
#     log_info_msg(
#         module, "{} model instance exist in {} table.".format(
#             instance_name, table_name
#         )
#     )
#
#
# def log_info_msg(module, msg):
#     file_logger.info("[{}]: {}".format(module, msg))
#
#
# def log_debug_msg(module, msg):
#     file_logger.debug("[{}]: {}".format(module, msg))
#
#
# def log_main_process_start(func):
#     def func_wrapper(*args, **kwargs):
#         string = kwargs['msg']
#         file_logger.info(": {} {} has been started.\n".format('#' * 5, string)
#                          )
#         func(*args, **kwargs)
#         file_logger.info(
#             ": {} {} has been finished.\n\n".format('/#' * 5, string)
#             )
#
#     return func_wrapper
#
#
# def log_function_start_end(func):
#     def func_wrapper(*args, **kwargs):
#         file_logger.debug(
#             "[{}]: {} function has been started.".format(func.__module__,
#                                                          func.__name__)
#         )
#         # print("{} function has been started.".format(func.__name__))
#         result = func(*args, **kwargs)
#         file_logger.debug(
#             "[{}]: {} function has been finished.".format(func.__module__,
#                                                           func.__name__)
#         )
#         return result
#
#     return func_wrapper
#
#
# def strptime_jalali(string):
#     return JalaliDate.strptime(string, '%y/%m/%d')
#
#
# def jalali_todate(jalali_date):
#     return jalali_date.todate()
#
#
# def unidecode_persian_string(string):
#     return unidecode(string)
#
#
# def convert_lastUpdated_to_date(string):
#     return jalali_todate(strptime_jalali(unidecode_persian_string(string)))
#


def input_number(string, **kwargs):
    value = input(f"{string}: ")
    try:
        value = int(value)
    except ValueError:
        print(
            "Invalid input. \"{}\" isn't a number. try again...".format(value))
        return input_number(string)
    return value


def input_bool(string, true_false="y/n", output="bool"):
    true, false = true_false.split('/')
    value = input(f"{string}? ")
    try:
        if value.lower() not in [true.lower(), false.lower()]:
            raise ValueError
    except ValueError:
        print(
            f"Invalid input. \"{value}\" isn't one of "
            + f"({true_false}). try again..."
        )
        return input_bool(string, true_false, output)

    if output == "bool":
        if value == true:
            value = True
        else:
            value = False

    return value


def edit_if_say_yes(string, value, value_type="string", **kwargs):
    input_as_wanted = input
    if value_type == "number":
        input_as_wanted = input_number
    elif value_type == "bool":
        input_as_wanted = input_bool

    wanna_change_this = input_bool(
        f"{string}: {value}\nDo you want to edit this (y/n)", output="bool")
    if wanna_change_this:
        if value_type != "string":
            value = input_as_wanted(f"{string}", **kwargs)
        else:
            value = input_as_wanted(f"{string}: ", **kwargs)
    return value


def save_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.writelines(data)
