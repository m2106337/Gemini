FROM python:3.11-slim

# Install minimal dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates wget curl \
 && rm -rf /var/lib/apt/lists/*

# Create a non-root user (best practice)
RUN useradd --create-home actionuser || true
USER actionuser

WORKDIR /action

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
