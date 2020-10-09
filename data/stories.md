## get_refund_status path
* refund_status{"refund":"refund", "PNR": "ZQYE2E"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status

## get_refund_status_2 path
* refund_status{"refund":"refund"}
  - utter_ask_pnr
* input_pnr{"PNR": "ZQYE2E"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status

## get_refund_status_5 path
* refund_status{"refund":"refund", "nopnr":"PLEASE"}
  - utter_ask_pnr
* input_pnr{"PNR": "ZQYE2E"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status
  
## get_refund_status_6 path
* refund_status{"refund":"refund", "nopnr":"PLEASE", "PNR":"ZQYE2E"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status
  
## get_refund_status_3 path
* refund_status{"refund":"refund", "PNR": "ZQYE2E", "shell":"credit shell"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status

## get_refund_status_4 path
* refund_status{"refund":"refund", "shell":"credit shell"}
  - utter_ask_pnr
* input_pnr{"PNR": "ZQYE2E"}
  - utter_surname
* surname{"surname": "Singh"}
  - action_refund_status

## No_refund path
* refund_status{"PNR": "ZQYE2E"}
  - utter_noreply

## No_refund_2 path
* refund_status
  - utter_noreply

## No_refund_3 path
* refund_status{"PNR": "ZQYE2E", "surname": "Singh"}
  - utter_noreply

## general_enquiry_4 path
* refund_status{"surname": "Singh"}
  - utter_noreply
  
## goodbye path
* thank_you
  - utter_done

## goodbye_refund path
* thank_you {"PNR": "ZQYE2E", "refund":"refund"}
  - utter_done

## baggage_noreply1 path
* baggage{"baggage": "baggage"}
  - utter_noreply

## baggage_noreply2 path
* baggage
  - utter_noreply

## baggage_1 path
* baggage{"baggage": "baggage", "weight": "10kg"}
  - utter_baggage_allowance

## baggage_product_1 path
* baggage{"baggage": "baggage", "product": "guitar", "cabin_prohibited": "power bank", "prohibited": "lighter"}
  - action_baggage
  - utter_product_allowance
  
## baggage_product_2 path
* baggage{"baggage": "baggage", "product": "guitar", "cabin_prohibited": "power bank"}
  - action_baggage
  - utter_product_allowance 

## baggage_product_3 path
* baggage{"baggage": "baggage", "product": "guitar", "prohibited": "lighter"}
  - action_baggage
  - utter_product_allowance 

## baggage_product_4 path
* baggage{"baggage": "baggage", "prohibited": "lighter", "cabin_prohibited": "power bank"}
  - action_baggage
  - utter_product_allowance 

## baggage_product_5 path
* baggage{"baggage": "baggage", "product": "guitar", "cabin_prohibited": "power bank", "prohibited": "lighter", "weight": "10kg"}
  - action_baggage
  - utter_product_allowance
  
## baggage_product_6 path
* baggage{"baggage": "baggage", "product": "guitar", "cabin_prohibited": "power bank", "weight": "10kg"}
  - action_baggage
  - utter_product_allowance 

## baggage_product_7 path
* baggage{"baggage": "baggage", "product": "guitar", "prohibited": "lighter", "weight": "10kg"}
  - action_baggage
  - utter_product_allowance 

## baggage_product_8 path
* baggage{"baggage": "baggage", "prohibited": "lighter", "cabin_prohibited": "power bank", "weight": "10kg"}
  - action_baggage
  - utter_product_allowance 

## baggage_alcohol path
* baggage{"baggage": "baggage", "alcohol": "alcohol"}
  - utter_alcohol

## seat_noreply1 path
* seat{"seat": "seat"}
  - utter_noreply

## seat_noreply2 path
* seat
  - utter_noreply

## seat_selection1 path
* seat{"seat": "seat", "select": "select"}
  - utter_seat
  
## flight_status1 path
* flight_status{"status": "status", "flight": "flight"}
  - utter_flight_status

## flight_status_2 path
* flight_status{"status": "status", "flight": "flight", "PNR": "VNZR6A"}
  - utter_flight_status

## flight_status_3 path
* flight_status{"book": "book", "location": "Hyderabad"}
  - utter_flight_status

## flight_status_4 path
* flight_status{"book": "book", "location": "Hyderabad", "flight": "flight"}
  - utter_flight_status
  
## flight_status_5 path
* flight_status{"status": "status", "flight": "flight", "PNR": "VNZR6A", "book": "book"}
  - utter_flight_status

## flight_status_6 path
* flight_status{"status": "status", "flight": "flight", "book": "book"}
  - utter_flight_status

## flight_status_7 path
* flight_status{"status": "status", "flight": "flight", "PNR": "VNZR6A", "book": "book", "location": "Hyderabad"}
  - utter_flight_status

## flight_status_8 path
* flight_status{"status": "status", "flight": "flight", "book": "book", "location": "Hyderabad"}
  - utter_flight_status

## flight_status_9 path
* flight_status{"book": "book", "location": "Hyderabad", "PNR": "VNZR6A"}
  - utter_flight_status