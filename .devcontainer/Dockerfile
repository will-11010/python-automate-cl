FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Remove Yarn repository with broken GPG keys
RUN rm -f /etc/apt/sources.list.d/yarn.list

# System packages used by PyAutoGUI workflows on Linux.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-tk \
        python3-dev \
        scrot \
        xclip \
    && rm -rf /var/lib/apt/lists/*
