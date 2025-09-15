from sodapy import Socrata

client = Socrata('www.datos.gov.co', None)

results = client.get("ceyp-9c7c", limit=2000)
