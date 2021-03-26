all:
	rm -f blenderbot_italian.zip
	rm -f bugbyte.*
	rm -f model.*
	python3 download_model.py
	nohup python3 server.py &