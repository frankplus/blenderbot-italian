all:
	rm blenderbot_italian.zip
	rm bugbyte.*
	rm model.*
	python3 download_model.py
	nohup python3 server.py &