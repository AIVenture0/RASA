# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import time
import selenium.webdriver
import pandas as pd

#with open('test_new.csv', 'r') as file:
#	reader = list(csv.reader(file))

#print(len(reader)) 
#reader = pd.read_csv('test_new.csv')
#print(reader.head())

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionRefundStatus(Action):
	def name(self) -> Text:
		return "action_refund_status"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		event_list = []
		
		for event in tracker.events:
			if event.get("event") == "user":
				event_list.append(event.get("parse_data")["entities"])
				
		
		print(event_list)
		print("\n")	
		if len(event_list)==0:
			print("No Entity detected...")
				
		pnr_test = []
		for i in range(0, len(event_list[0])):
			if event_list[0][i]['entity'] == 'PNR':
				pnr_test.append(event_list[0][i]['value'])
				print(pnr_test)  
		print(pnr_test)
		#if len(pnr_test) == 0:
		#	if event_list[1][0]['entity'] == 'PNR':
		#		pnr_test.append(event_list[1][0]['value'])
		#		print(pnr_test)
		
		if len(pnr_test) == 0:
			pnr_test.append(tracker.get_slot("PNR"))
		print(pnr_test)
		
		#for i in range(0, len(event_list)):
		#	if event_list[0][i]['entity'] == 'surname':
		#		surname_test = event_list[0][i]['value']
		#		print(surname_test)
		
		surname_test = tracker.get_slot("surname")
		
		print(surname_test)
		print(pnr_test[0])
		message =[]
		if not surname_test:
			print("No surname found")
		else:
			for i in range(0,len(pnr_test)):
				baseDataUrl = "https://www.goindigo.in/member/my-booking.html"
				driver = selenium.webdriver.Chrome(r"C:/Users/vinay/Downloads/chromedriver_win32/chromedriver.exe")
				driver.get(baseDataUrl) 
				time.sleep(10)
				
				try:

					#PNR
					driver.find_element_by_id('booking-reference').send_keys(pnr_test[i])
					#Surname
					driver.find_element_by_id('email-lastname').send_keys(surname_test)

					#Button
					driver.find_element_by_id('mybooking-retrive-button').click()
					time.sleep(8)
					flight_status= driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/section/div[1]/div[1]/section[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]').text
					payment_status = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/section/div[1]/div[1]/section[2]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]').text
			
					shell=""
					try:
						shell = driver.find_elements_by_class_name('cnf-credit-blck')[2].text
					except:
						pass
			
					if shell=="":
						driver.execute_script("window.scrollBy(0, 700)")
						info = driver.find_element_by_class_name('cnf-price-details.price-summary').text
						#third_party = driver.find_elements_by_class_name('cnf-contact-desc.contact-address')[1].text
				
						message.append("Greetings from Indigo! Details for PNR: "+ (pnr_test[i])+ "The flight is " + (flight_status) + "\n" + "The Payment status is " + (payment_status) + "\n"+ "Refund Status is: " + (info) + "\n" + "If not received the amount plz contact your travel agency.")
					else:
						message.append("Greetings from Indigo! Details for PNR: "+ (pnr_test[i])+ "The flight is " + (flight_status) + ". The Payment status is " + (payment_status) + ". Shell Status: " + (shell))
				
					dispatcher.utter_message(text=message[i])
				except:
					dispatcher.utter_message(text="Provided details are incorrect. ")
					
		print(message)
		return []

class ActionBaggage(Action):
	def name(self) -> Text:
		return "action_baggage"

	def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		entities = tracker.latest_message['entities']
		print(entities)
		
		for i in range(0, len(entities)):
			if entities[i]['entity'] == 'product':
				if entities[i]['entity'] == "prohibited":
					dispatcher.utter_message(text = entities[i]['value'] + " is NOT allowed")
				elif entities[i]['entity'] == "cabin_prohibited":
					dispatcher.utter_message(text = entities[i]['value'] + " is allowed in check in luggage")
				else:
					dispatcher.utter_message(text = entities[i]['value'] + " is allowed in both cabin or check in luggage")
			
		#dispatcher.utter_message(text="Hello World!")
		return []