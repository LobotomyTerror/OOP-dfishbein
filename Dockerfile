FROM python:3

RUN apt update \
  && apt install -y \
  g++ gcc make sqlite3 time curl git nano dos2unix \
  net-tools iputils-ping iproute2 sudo gdb less \
  default-jre graphviz && apt clean

ARG USER=user
ARG UID=1000
ARG GID=1000

# Set environment variables
ENV USER                ${USER}
ENV HOME                /home/${USER}

# Create user and setup permissions on /etc/sudoers
RUN useradd -m -s /bin/bash -N -u $UID $USER && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers && \
    chmod 0440 /etc/sudoers && \
    chmod g+w /etc/passwd 

WORKDIR ${HOME}

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install zsh - use "Bira" theme with some customization. 
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t bira \
    -p git \
    -p ssh-agent \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting

# Creates dirctory and installs plantuml.jar file for uml design through cmd line
RUN mkdir /opt/plantuml && \
    curl -L http://sourceforge.net/projects/plantuml/files/plantuml.jar/download -o /opt/plantuml/plantuml.jar && chmod 754 /opt/plantuml/plantuml.jar

# Sets an environment variable to be able to use for java jar script
ENV PLANT=/opt/plantuml/plantuml.jar

RUN echo "#alias plantuml='java -jar $PLANT'" >> ~/.bashrc

USER user

CMD zsh
