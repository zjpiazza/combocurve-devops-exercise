FROM docker.io/python:3.10 AS builder

RUN pip install --user pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /app/

WORKDIR /app

RUN /root/.local/bin/pipenv sync

FROM docker.io/python:3.10 AS runtime

RUN mkdir -v /usr/src/.venv

COPY --from=builder /app/.venv/ /app/.venv/

WORKDIR /app/

ADD app.py /app/

CMD ["/app/.venv/bin/gunicorn", "-b 0.0.0.0:80", "app:app"]