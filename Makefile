all:
	rm blenderbot_italian.zip
	rm bugbyte.*
	rm model.*
	source env/bin/activate
	python3 download_model.py
	nohup python3 server.py &