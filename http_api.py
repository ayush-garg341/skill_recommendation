import json
import requests
import csv

class SendData:

	def __init__(self, url_post, file_path):
		self.url = url_post
		self.file = file_path

	def send_data(self):
		example_file = open(self.file, encoding = "ISO-8859-1")
		example_reader = csv.reader(example_file)
		try:
			for row in example_reader:
				payload = {'keyskills':row[0]}
				res = requests.post(self.url, json = payload)
				#print(res.content)
		
		except requests.exceptions.HTTPError as err:
			return err

		except requests.exceptions.Timeout as err:
			return err

		except requests.exceptions.TooManyRedirects as err:
			return err

		except requests.exceptions.RequestException as err:
			return err

		except KeyboardInterrupt :
			return "Keyboard Interrupt"

		except:
			return "Unknown error"

