=====
Museum
=====

Museum is a simple Django app to manage different image sizes.

Quick start
-----------

1. Add "museum" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'museum',
    ]

2. Run `python manage.py migrate` to create the museum models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create new image sizes (you'll need the Admin app enabled).

4. Now, you're able to upload Pictures and resize them!