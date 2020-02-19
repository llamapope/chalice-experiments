Repository from [Python Utah North, 2020-02-19](https://www.meetup.com/Python-Utah-North/events/268643043/) meetup.

[Slide deck](https://docs.google.com/presentation/d/1g9P5T829nhRaMMc7-D1Gl8GD046uNi2UewOelwbgnbg/edit?usp=sharing)

# Chalice Experiements

Each experiment is a self contained chalice app, located in the [experiements folder](experiements). Many have configurations or dependencies that are unique to the experiment. See each README.md and requirements.txt file for details.

It is assumed that you will use a new virtual environment per experiment to avoid any potential conflicts. Chalice commands are assumed to be ran in each experiement's folder.

> Minimal front-ends are contained in a `client/` folder for each project. They are assumed to be deployed to a webserver to function. Some may have variables that must be modified to function. e.g. `cd client` then `python3.7 -m http.server 8080` visit http://127.0.0.1:8080

* [S3 Image upload/resize](experiments/s3-image-resize/README.md)

If you have ideas or experiments you want to add to this repository, send a pull request.

# Experiments Repository Notes

Tested with python 3.7.

> If you are just using the projects from this repository directly, you can skip the rest of this guide and go to the project specific guides. If you are wanting to follow along, you can get the same setup that was used to create all projects in this repository by following the rest of this guide.

* [AWS_PROFILE](docs/aws-profile.md) *optional, but recommended if using multiple AWS accounts*
* [User chalice setup](docs/user-chalice-setup.md) *handles pip version issues*
* [New project setup](docs/new-project-setup.md) *how each project was created*
* [Common Commands](docs/common-commands.md) *chalice commands you'll want to remember*