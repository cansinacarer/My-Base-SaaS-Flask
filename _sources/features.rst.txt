Features
========================================

-  💳 Stripe checkout flows:

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

-  🔒 Authentication,

   -  Sign up flow,

      -  Sign up with Google option,
      -  Email validation requirement,

   -  Two factor authentication (TOTP only),
   -  Forgot password flow,
   -  Account details page where the user can:

      -  Upload a profile picture (stored in S3),
      -  Change profile details like first & last name.

-  📧 Transactional emails sent over SMTP:

   -  About Stripe subscription changes:

      -  Confirmation,
      -  Cancellation,
      -  Expiration.

   -  Email verification on registration,
   -  Forgot password.

-  🗄️ Database model with ORM, automatically created on first run to
   accommodate the features above,
-  🚨 Security measures:

   -  CSRF (Cross-Site Request Forgery) protection in all forms,
   -  Rate limiting: App-wide and form specific limits.

-  🐳 Dockerized for stateless continuous deployment,
-  🔔 UI components ready to use:

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

   -  ``flash()`` messages of Flask styled as Bootstrap 5 alerts,

-  🌐 HTML templates:

   -  Email templates for the email validation, password reset,
   -  2 sets of page templates,

      -  Public pages (``templates/public``),

         -  Login/sign up pages,

      -  Backend (auth required) pages (``templates/private``),

   -  Utilizes the new ootb Bootstrap 5 components like floating form
      labels,
   -  Last, but not least: User configurable dark mode. 😎
