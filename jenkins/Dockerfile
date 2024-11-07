FROM jenkins/jenkins:lts

EXPOSE 8080
EXPOSE 50000

USER root
RUN mkdir -p /var/jenkins_home/workspace && \
    chown -R jenkins:jenkins /var/jenkins_home/workspace

USER jenkins