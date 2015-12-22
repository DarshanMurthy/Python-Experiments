from slacker import Slacker
from jenkinsapi.jenkins import Jenkins

class jenkins:
	def __init__(self,url,job):
		self.url = Jenkins(url)
		self.job = job
	
	def jenkinsVersion(self):
		J = self.url
		print J.version
	
	def listofJobs(self):
		print self.url.keys()

	
	def getlastgoodbuild(self):
		print "The current Job is",self.url[self.job]
		job = self.url[self.job]
		print "The current job's last build ", job.get_last_build()
		print "The current job's Good Build is ",job.get_last_good_build()

	def isBuildGood(self):
		job = self.url[self.job]
		print job.is_good()


		
			
		
if __name__ == '__main__':
	jenkins = jenkins("http://scit-i-ec76021a:8080/","Test_My_Solar_City_15_12_C")
	print jenkins.jenkinsVersion() 
	print jenkins.listofJobs()
	print jenkins.getlastgoodbuild()
	print jenkins.isBuildGood()