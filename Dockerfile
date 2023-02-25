FROM debian:10.13-slim
RUN apt-get update && apt-get install -y python3 python3-pip

# Prepare app
COPY ./setup.py /prowessive/setup.py
COPY ./README.md /prowessive/README.md
WORKDIR /prowessive
RUN python3 -m pip install .
COPY prowessive /prowessive
COPY entrypoint.sh /prowessive/entrypoint.sh

# Clean packages
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0

EXPOSE 8000
ENTRYPOINT ["/bin/bash"]
CMD ["entrypoint.sh"]

