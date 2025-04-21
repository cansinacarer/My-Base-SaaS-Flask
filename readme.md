# Cansin's Base SaaS (Flask)

[![Docs](https://img.shields.io/badge/Docs-blue?&logo=read-the-docs&logoColor=white)](https://cansinacarer.github.io/My-Base-SaaS-Flask/)
![Test Coverage](tests/coverage/coverage-badge.svg)
[![Uptime](https://uptime.apps.cansin.net/api/badge/5/uptime)](https://uptime.apps.cansin.net/status/base-saas-flask-demo)
![Last Commit](https://img.shields.io/github/last-commit/cansinacarer/My-Base-SaaS-Flask?color=blue)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)

[![Pre-Commit Hooks](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/pre-commit.yml)
[![Tests](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/test.yml/badge.svg)](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/test.yml)
[![Semantic Release](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/semantic-release.yml/badge.svg)](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/semantic-release.yml)
[![Build & Deploy](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/deploy.yml/badge.svg)](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/deploy.yml)
[![Build & Deploy Sphinx Docs](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/docs.yml/badge.svg)](https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/docs.yml)

The starter SaaS framework I built with Flask for my side projects with paid subscriptions.

[Live Demo](https://base-saas-flask.apps.cansin.net/) → use with [Stripe test card numbers](https://docs.stripe.com/testing?testing-method=card-numbers#cards)

## 📄 Documentation

- [Development](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html)
  - [Code Quality, Conventional Commits, and Releases](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#code-quality-conventional-commits-and-releases)
  - [Developing in Dev Containers](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#developing-in-dev-containers)
    - [Debugging](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#debugging)
    - [Testing Stripe Webhooks](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#testing-stripe-webhooks)
  - [Developing in a Virtual Environment](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#developing-in-a-virtual-environment)
  - [How to Build On Top of This App](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#how-to-build-on-top-of-this-app)
    - [Adding New Pages](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#adding-new-pages)
    - [Defining More Configuration Variables](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#defining-more-configuration-variables)
    - [Updating Dependencies](https://cansinacarer.github.io/My-Base-SaaS-Flask/development.html#updating-dependencies)
- [Continuous Integration and Continuous Deployment](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html)
  - [Pre-Commit Hooks](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html#pre-commit-hooks)
  - [Run Tests](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html#run-tests)
  - [Semantic Release](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html#semantic-release)
  - [Build & Deploy](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html#build-deploy)
  - [Build & Deploy Sphinx Docs](https://cansinacarer.github.io/My-Base-SaaS-Flask/ci-cd.html#build-deploy-sphinx-docs)
- [Deployment to Production](https://cansinacarer.github.io/My-Base-SaaS-Flask/deployment.html)
  - [A Pitfall for Cloudflare Proxy](https://cansinacarer.github.io/My-Base-SaaS-Flask/deployment.html#a-pitfall-for-cloudflare-proxy)
- [Auto Generated Documentation](https://cansinacarer.github.io/My-Base-SaaS-Flask/autoapi/index.html)

## ⭐ Features

- 💳 Stripe checkout flows:
  - Subscriptions,
    - Different subscription tiers,
    - Billing page with Invoices,
    - Integration mechanism:
      - To begin a subscription, we send the user to Stripe with a checkout session,
      - Then listen to Stripe webhook events to process the results,
      - We set the Products in Stripe, then insert their prices into the Tiers table.
  - One-off credit purchases for pre-paid metered usage.
- 🔒 Authentication,
  - Sign up flow,
    - Sign up with Google option,
    - Email validation requirement,
  - Two factor authentication (TOTP only),
  - Forgot password flow,
  - Account details page where the user can:
    - Upload a profile picture (stored in S3),
    - Change profile details like first & last name.
- 📧 Transactional emails sent over SMTP:
  - About Stripe subscription changes:
    - Confirmation,
    - Cancellation,
    - Expiration.
  - Email verification on registration,
  - Forgot password.
- 🗄️ Database model with ORM, automatically created on first run to accommodate the features above,
- 🚨 Security measures:
  - CSRF (Cross-Site Request Forgery) protection in all forms,
  - Rate limiting: App-wide and form specific limits.
- 🐳 Dockerized for stateless continuous deployment,
- 🔔 UI components ready to use:
  - Toast notifications

    ```javascript
    showToast(
        "This is a test toast notification!",
        "Toast Title",
        "success",
        { autohide: false }
    );
    ```

  - Modals

    ```javascript
    showAlert(
        "Title",
        "This is a test modal dialog!",
        "Back",
        "info"
    );
    ```

  - `flash()` messages of Flask styled as Bootstrap 5 alerts,
- 🌐 HTML templates:
  - Email templates for the email validation, password reset,
  - 2 sets of page templates,
    - Public pages (`templates/public`),
      - Login/sign up pages,
    - Backend (auth required) pages (`templates/private`),
  - Utilizes the new ootb Bootstrap 5 components like floating form labels,
  - Last, but not least: User configurable dark mode. 😎

## Screenshots

<table>
    <tr>
        <td colspan="2" align="center"><strong>Billing Page</strong> <code>/app/billing</code></td>
    </tr>
    <tr>
        <td><img src="screenshots/billing-dark.png"></td>
        <td><img src="screenshots/billing-light.png"></td>
    </tr>
    <tr>
        <td colspan="2" align="center"><strong>My Account Page</strong> <code>/app/my-account</code></td>
    </tr>
    <tr>
        <td><img src="screenshots/my-account-dark.png"></td>
        <td><img src="screenshots/my-account-light.png"></td>
    </tr>
    <tr>
        <td colspan="2" align="center"><strong>Public Home Page with Personalization</strong> <code>/</code></td>
    </tr>
    <tr>
        <td><img src="screenshots/public-home-page-dark.png"></td>
        <td><img src="screenshots/public-home-page-light.png"></td>
    </tr>
</table>
