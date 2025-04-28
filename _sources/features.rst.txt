Features
========================================

🧑‍💻 Developer Experience
---------------------------------------------

-  Dev containers:

   -  **Flask** container with pre-configured with:

      -  VSCode launch.json for debugging the Flask app,
      -  Prettier for HTML, CSS, and JS formatting,
      -  Pre-commit hooks for code quality checks,
      -  Markdownlint for Markdown formatting,
      -  Black for Python code formatting,
      -  Commitlint for commit message linting.

   -  **Postgres** as a development database,

   -  **pgAdmin** pre-connected to the development.

-  CI/CD pipelines with GitHub Actions to:

   -  Run pre-commit hooks,
   -  Run tests,
   -  Automate semantic release for versioning and changelog generation,
   -  Build and deploy the documentation,
   -  Build and deploy the app to production.

☁️ Deployment
---------------------------------------------

-  🐳 Dockerized Flask for stateless continuous deployment for scalability,
-  🗄️ Database model abstracted with ORM,
-  📦 S3 object storage with pre-signed URLs.


💳 Stripe Integrations
---------------------------------------------

   -  Subscriptions,

      -  Different subscription tiers,
      -  Billing page with Invoices,
      -  Integration mechanism:

         -  To begin a subscription, we send the user to Stripe with a
            checkout session,
         -  Then listen to Stripe webhook events to process the results,
         -  We set the Products in Stripe, then insert their prices into
            the Tiers table.

   -  One-off credit purchases for pre-paid metered usage.

🔒 Authentication
---------------------------------------------

   -  Sign up flow,

      -  Sign up with Google option,
      -  Email validation requirement,

   -  Two factor authentication (TOTP only),
   -  Forgot password flow,
   -  Account details page where the user can:

      -  Upload a profile picture (stored in S3),
      -  Change profile details like first & last name.

📧 Transactional Emails with SMTP
---------------------------------------------

   -  About Stripe subscription changes:

      -  Confirmation,
      -  Cancellation,
      -  Expiration.

   -  Email verification on registration,
   -  Forgot password.

🚨 Security
---------------------------------------------

   -  Cross-Site Request Forgery (CSRF) protection in all forms,
   -  Rate limiting: App-wide and form specific limits,
   -  Cross-Site Scripting (XSS) protection,
   -  Cross-Origin Resource Sharing (CORS) protection.


🎨 UI
---------------------------------------------

🔔 Notifications
~~~~~~~~~~~~~~~~~~~~~~~~

-  Toast notifications

   .. code:: javascript

      showToast(
          "This is a test toast notification!",
          "Toast Title",
          "success",
          { autohide: false }
      );

-  Modals

   .. code:: javascript

      showAlert(
          "Title",
          "This is a test modal dialog!",
          "Back",
          "info"
      );

-  ``flash()`` messages from Flask styled as Bootstrap 5 alerts,

🌐 Bootstrap HTML templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Email templates for the email validation, password reset,
-  2 sets of page templates and Flask Blueprints:

    -  Public pages (``templates/public/``),

    -  Auth pages for login, sign up, and password reset, 2FA (``templates/auth/``),

    -  Backend (auth required) pages (``templates/private/``).

-  Utilizes the new ootb Bootstrap 5 components like floating form labels,
-  Last, but not least: User configurable dark mode. 😎
