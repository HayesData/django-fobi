__title__ = 'fobi.contrib.plugins.form_elements.fields.radio.conf'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_setting',)

from django.conf import settings

from fobi.contrib.plugins.form_elements.fields.radio import defaults

def get_setting(setting, override=None):
    """
    Get a setting from `fobi.contrib.plugins.form_elements.fields.radio` conf
    module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults
        to None.
    :return: Setting value.
    """
    if override is not None:
        return override
    if hasattr(settings, 'FOBI_FORM_ELEMENT_RADIO_{0}'.format(setting)):
        return getattr(settings, 'FOBI_FORM_ELEMENT_RADIO_{0}'.format(setting))
    else:
        return getattr(defaults, setting)
