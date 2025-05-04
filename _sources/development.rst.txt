Development
=================

Code Quality, Conventional Commits, and Releases
------------------------------------------------

Code quality is maintained by *pre-commit* hooks and ``.vscode/settings.json`` locally; then also enforced with GitHub Actions in the remote repository.

- Python scripts are required to follow ``black`` code style.
- HTML, CSS, and Javascript files are checked with ``prettier``.
- Markdown files are checked with ``markdownlint``.

Commit messages are required to follow the conventional commits standard. This is enforced by the ``commitlint`` pre-commit hook and the CI/CD pipeline.

The release process is automated with GitHub Actions. When a new tag is pushed, the CI/CD pipeline will automatically build and deploy the app to the production server based on the semantic release standards, and create a Changelog file with the changes since the last release.


Developing in Dev Containers
-------------------------------

Dev Containers are a the recommended way to develop this project. You simply clone this repository and open it in VS Code. Make sure that the Docker daemon is running, then use ``>Dev Containers: Reopen in Container`` command in VS Code. This will create containers with the following applications:

- Flask
   - Accessible at ``https://localhost:5000``. It uses the self-signed SSL
     certificate generated in ``.devcontainer/ssl``. Never use these certificates for production!

   - This is where the app runs. It is based on the official Python image
     with the packages from ``requirements.txt`` installed.

   - It also has additional packages installed for development, such as
     ``black``, ``pytest``, and ``pre-commit``.

- pgAdmin
   - Accessible at ``http://localhost:5002``. You can use this to manage the
     Postgres database.
   - It is already configured to connect to the Postgres container. When prompted
     for the database password, use ``password``.

- Postgres
   - When Flask is initialized, it will create the tables in this database.
   - If you need to access the database, it is available at ``localhost:5432``.


Local Endpoints Served by the Dev Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+---------------------------------------------------------------------------------+
| Port                   | Application                                                                     |
+========================+=================================================================================+
| https://localhost:5000 | Flask application run with debug mode active                                    |
+------------------------+---------------------------------------------------------------------------------+
| https://localhost:5001 | Flask application run with VSCode debugger                                      |
+------------------------+---------------------------------------------------------------------------------+
| http://localhost:5002  | pgAdmin instance connected to the local development database                    |
+------------------------+---------------------------------------------------------------------------------+
| http://localhost:5003  | HTTP service serving the html files of the documentation in ``docs/build/html`` |
+------------------------+---------------------------------------------------------------------------------+


Debugging
~~~~~~~~~
The configuration in ``.vscode/launch.json`` allows us to use the VSCode debugger to set breakpoints and inspect variables. The Flask instance run this way will be available at ``http://localhost:5001``.


Testing Stripe Webhooks
~~~~~~~~~~~~~~~~~~~~~~~
For testing with Stripe, you’ll need to get the webhook secret (``whsec_...``) using this Stripe CLI command:

``stripe listen --forward-to https://localhost:5000/app/webhook --skip-verify``

If you want to test subscription events used by this app, run the
following to make stripe CLI listen and forward the following events:

-  customer.subscription.updated
-  customer.subscription.deleted

``stripe listen -e customer.subscription.updated,customer.subscription.deleted,checkout.session.completed --forward-to https://localhost:5000/app/webhook/stripe --skip-verify``

This returns the webhook signing secret we use to verify that Stripe
is the one sending webhook requests. This secret needs to be saved in
the ``.env`` file as shown in ``.env.template``.

.. HINT::
   Some of the functionality will not work in your local development environment without having this listener forward the events from Stripe to the local instance of this app. For example, the account balance will not increment as this depends on the event from Stripe.

Developing in a Virtual Environment
--------------------------------------

I do not recommend using a virtual environment for development, but here is the legacy documentation I had for it before I switched to devcontainers.

1. Clone the repo, navigate to the repo directory,

2. Create a virtual environment: ``python -m venv env``

3. Activate the virtual environment:

   -  For Windows:

      ``env\Scripts\activate``

   -  For macOS/Linux:

      ``source env/bin/activate``

4. Install the dependencies inside the virtual environment:

   ``pip install -r requirements.txt``

5. Set the environment variables listed in the ``.env.template`` file

6. Generate a self signed SSL certificate for using https locally. On
   Linux or with WSL in the root path:

   ``openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes``

7. Run ``flask run``


How to Build On Top of This App
-------------------------------

Adding New Pages
~~~~~~~~~~~~~~~~

1. In both ``public`` and ``private`` directories, you can copy the
   ``sample-page.html`` as a starter and rename it (e.g. ``test.html``).
   The generic routing in ``views.py`` will automatically be served at
   ``/test`` directory.
2. Update the page title at ``{% set page_title = "Sample Page" %}``.
3. Insert a link to this page in ``components/header/nav-menu.html``.
   For the active page highlighting, we also need to update the path for
   active link condition in this class:
   ``class="nav-link {% if path == 'sample-page' %}active{% endif %}"``.
4. Insert content between ``{% block content %}`` and
   ``{% endblock content %}`` as needed.

Note that URLs with trailing slashes (e.g. ``/test/``) are redirected to
the alternatives without one (e.g. ``/test``).

Defining More Configuration Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to have more config variables (e.g. credentials for a new
OAuth provider):

1. Define environment variables for them both in your local ``.env``
   file and in prod,
2. In ``app/config.py``, add a new attribute for the ``Config`` class.
   Use the ``config`` method from decouple.
3. You can then call the config value anywhere in the app as
   ``app.config[""]``.

Updating Dependencies
~~~~~~~~~~~~~~~~~~~~~

To include new Python packages, you can first install them in your local
virtual environment during development. Before pushing a change with a
new package, also update the dependencies using
``pip freeze > requirements.txt``.
