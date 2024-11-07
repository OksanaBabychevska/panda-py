FROM jenkins/jenkins:lts

EXPOSE 8080
EXPOSE 50000

USER root

RUN mkdir -p /var/jenkins_home/workspace/panda

COPY Jenkinsfile /var/jenkins_home/workspace/panda/

RUN chown -R jenkins:jenkins /var/jenkins_home/workspace/panda/

USER jenkins