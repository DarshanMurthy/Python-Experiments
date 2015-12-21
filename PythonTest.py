from slacker import Slacker
from jenkinsapi.jenkins import Jenkins

class jenkins:
	def __init__(self,url):
		self.url = url
	def jenkinsServerName(self):
		server = Jenkins(self.url)
		return server

jenkins = jenkins("http://scit-i-ec76021a:8080/")
print jenkins.jenkinsServerName()
