djangocms-column
================

A Multi Column Plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 3.8 or higher to be properly installed.

* In your projects virtualenv, run ``pip install djangocms-column``.
* Add ``'djangocms_column'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_column``.


Usage
-----

There are 2 plugins: `MultiColumn` and `Column`
The first is `MultiColumn` that should be added to your placeholder conf.
`MultiColumn` only allows one plugin as a child: the `Column` plugin.
The `Column` plugin has a parameter width. With this parameter you can control the width
of the column. 

You can add a new setting to your settings.py called `COLUMN_WIDTH_CHOICES`

the default is::

	COLUMN_WIDTH_CHOICES = (
            ('10%', _("10%")),
            ('25%', _("25%")),
            ('33.33%', _('33%')),
            ('50%', _("50%")),
            ('66.66%', _('66%')),
            ('75%', _("75%")),
            ('100%', _('100%')),
	)

but you can change that to fit your CSS grid framework or other purposes.

Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-column/
