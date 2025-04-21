Continuous Integration and Continuous Deployment
================================================

We have 5 GitHub Actions workflows for CI/CD:


Pre-Commit Hooks
-----------------------------------
|Pre-Commit Hooks|

Pre-Commit checks for linting and conventional commit messages are enforced with ``.github/workflows/pre-commit.yml``.


Run Tests
-----------------
|Tests|

Unit tests are run with ``.github/workflows/test.yml``.


Semantic Release
-----------------
|Semantic Release|

If the tests are successful, changelog is generated, a new version is tagged, and a release is created with ``.github/workflows/semantic-release.yml``.


Build & Deploy
-----------------
|Build & Deploy|

If the tests are successful, the app is built and deployed to CapRover with ``.github/workflows/deploy.yml``.


Build & Deploy Sphinx Docs
-----------------
|Build & Deploy Sphinx Docs|

If the tests are successful, this documentation is built with Sphinx and its autoapi extension, then prepared for deployment to GitHub Pages with ``.github/workflows/docs.yml``.


.. |Pre-Commit Hooks| image:: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/pre-commit.yml/badge.svg
   :target: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/pre-commit.yml
.. |Tests| image:: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/test.yml/badge.svg
   :target: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/test.yml
.. |Semantic Release| image:: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/semantic-release.yml/badge.svg
   :target: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/semantic-release.yml
.. |Build & Deploy| image:: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/deploy.yml/badge.svg
   :target: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/deploy.yml
.. |Build & Deploy Sphinx Docs| image:: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/docs.yml/badge.svg
   :target: https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/docs.yml
