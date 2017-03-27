from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_businesses(location, term):
	auth = Oauth1Authenticator(
		consumer_key = os.environ['consumer_key'],
	    consumer_secret= os.environ['consumer_secret'],
	    token= os.environ['token'],
	    token_secret= os.environ['token_secret']
	)

	client = Client(auth)

	params = {
	    'term': term,
	    'lang': 'en',
	    'limit': 3

	}

	response = client.search(location, **params)

	businesses= []

	for business in response.businesses:
		#print(business.name, business.rating, business.phone)
		#businesses.append(business.name)
		businesses.append({"name": business.name, 
			"rating": business.rating, "phone":business.phone

		})

	return businesses


businesses = get_businesses('Fort Worth', 'food')

print(businesses)

