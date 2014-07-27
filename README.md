djangocms-column
================

A Multi Column Plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-column``.
* Add ``'djangocms_column'`` to your ``INSTALLED_APPS`` setting.
* If using Django 1.7 add ``'djangocms_column': 'djangocms_column.migrations_django',``
  to ``MIGRATION_MODULES``  (or define ``MIGRATION_MODULES`` if it does not exists);
  when django CMS 3.1 will be released, migrations for Django 1.7 will be moved
  to the standard location and the south-style ones to ``south_migrations``.
* Run ``manage.py migrate cmsplugin_column``.


Usage
-----

There are 2 plugins: MultiColumn and Column
The first is MultiColumn that should be added to your placeholder conf.
MultiColumn only allows one plugin as a child: the Column plugin.
The Column plugin has a parameter width. With this parameter you can control the width 
of the column. 

You can add a new setting to your settings.py called `COLUMN_WIDTH_CHOICES`

the default is::

	COLUMN_WIDTH_CHOICES = (
	    ('1', _("normal")),
	    ('2', _("2x")),
	    ('3', _("3x")),
	    ('4', _("4x"))
	)

but you can change that to fit your CSS grid framework or other purposes.

Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-column/

