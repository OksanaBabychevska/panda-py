FROM jenkins/jenkins:lts

EXPOSE 8080
EXPOSE 50000

USER root

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    sudo

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | tee /etc/apt/trusted.gpg.d/docker.asc && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

RUN apt-get update && apt-get install -y docker-ce

RUN mkdir -p /var/jenkins_home/workspace && \
    chown -R jenkins:jenkins /var/jenkins_home/workspace


USER jenkins

CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]
