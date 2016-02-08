all: get-repositories docker-compose

collect:
	source /env/bin/activate
	python manage.py collectstatic --noinput

remove-docker:
	sudo apt-get remove docker*
	sudo apt-get autoremove
	sudo apt-get autoclean

install-docker:
	echo deb http://get.docker.com/ubuntu docker main | sudo tee /etc/apt/sources.list.d/docker.list
	sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
	sudo apt-get update
	sudo apt-get install -y lxc-docker-1.7.0
	sudo sh -c "curl -L https://github.com/docker/compose/releases/download/1.4.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
	sudo chmod +x /usr/local/bin/docker-compose
	sudo sh -c "curl -L https://raw.githubusercontent.com/docker/compose/1.4.0/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose"

get-repositories:
	git submodule init
	git submodule update

compose:
	docker-compose build --no-cache
	docker-compose up
