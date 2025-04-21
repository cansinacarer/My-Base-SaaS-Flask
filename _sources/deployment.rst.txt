Deployment to Production
========================

This app is containerized and intended to be deployed in a Docker. This means you can deploy it anywhere from fully managed PaaS services to container hosting services and custom self-hosted solutions.

The ``Dockerfile`` will install the dependencies from the ``requirements.txt`` in the container and will run Flask with Gunicorn. Depending on your traffic and server resources, you will want to adjust the number of workers in the ``Dockerfile``.

For reference, the live demo website is running on a cheap VPS with `CapRover <https://caprover.com/>`_ installed. CapRover is a self-hosted PaaS built as a layer on Docker. It simplifies
setting environment variables, routing traffic to containers nginx
reverse proxy, and SSL set up. I use `this GitHub Actions
workflow <https://github.com/cansinacarer/My-Base-SaaS-Flask/actions/workflows/deploy.yml>`__ for continuous deployment.

Here is a Medium article I wrote about `configuring a server instance with CapRover <https://betterprogramming.pub/migrate-from-heroku-to-aws-ec2-756328d8e58a>`_.

A Pitfall for Cloudflare Proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the domain is proxied over Cloudflare, set SSL to Full (strict) to prevent ERR_TOO_MANY_REDIRECTS error.
