"""
Django 自带的验证器
"""

from django.core import validators
from django.core.validators import RegexValidator, validate_integer


def val_xx(scheme_value, param_value):
    for schema_value_item in scheme_value:
        for param_value_item in param_value:
            if isinstance(schema_value_item, dict) and isinstance(
                    param_value_item, dict):
                val_body(param_value_item,
                         schema_body=schema_value_item)
            elif isinstance(schema_value_item, str) and isinstance(
                    param_value_item, str):
                pi = param_value.index(param_value_item)
                RegexValidator(scheme_value[pi],
                               message="list参数%s的值不合法" % param_value_item).__call__(
                    param_value_item)
            elif isinstance(isinstance(schema_value_item, list) and isinstance(
                    param_value_item, list)):
                val_xx(schema_value_item, param_value_item)


def val_body(param, schema_body=None):
    if isinstance(param, dict):
        for schema_key, scheme_value in schema_body.items():
            # if isinstance(schema_body[0], dict-study):
            for param_key, param_value in param.items():
                if schema_key == param_key:
                    if isinstance(param_value, str):
                        RegexValidator(scheme_value,
                                       message="参数%s的值不合法" % param_key).__call__(
                            param_value)
                    elif isinstance(param_value, int):
                        validate_integer(param_value)
                    elif isinstance(param_value, list):
                        val_xx(scheme_value, param_value)
                    elif isinstance(param_value, dict):
                        val_body(param_value,
                                 schema_body=scheme_value)


def validate(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        val_body(args[0], schema_body=schema_body)
        # RegexValidator("", message="不合法").__call__(value)
        return func(*args, **kwargs)

    return wrapper


@validate
def get_body(body, schema_body=None):
    print(body)
