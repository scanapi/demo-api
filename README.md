![](https://github.com/scanapi/design/raw/main/images/github-hero-dark.png)

# Demo API

This is an API built only for demo purposes of [ScanAPI](https://github.com/camilamaia/scanapi). It
can be accessed at https://demo.scanapi.dev/.


## Development

### How to run demo-api locally

> The setup process's prerequisites are [Python 3.6+](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed in your system.

1. **Fork scanapi/demo-api**

* [Fork](https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo) a repo in your github account such as you get *yourusername*/demo-api. Now that you own a copy of the repo, you can easily clone the repo with the command below so that you can start making changes to the repo.

```
git clone https://github.com/<your username>/demo-api.git
```

2. **Create and activate a new virtual environment**

* For creating virtual environment we are using the method mentioned in the [Python documentation](https://docs.python.org/3/tutorial/venv.html).
```
python3 -m venv DemoAPI
source DemoAPI/bin/activate
```

 * Feel free to use any other library like [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) for creating a new environment if you have any other prefrences.

3. **Install the demo-api dependencies**

```
cd demo-api
pip install -r requirements.txt
```

4. **Make migrations and run the demo-api**
```
python manage.py migrate
python manage.py runserver
```

* If everything runs smoothly without any errors you should see the API live at http://127.0.0.1:8000/. Feel free to create an issue if run into problems while setting up the project.


## Deployment

Currently the demo-api is hosted on Heroku with an auto deployment enabled i.e whenver any branch is merged into the main branch. A new deployment is triggered at [demo.scanapi.dev](https://demo.scanapi.dev/api/v1/).

You can check the status/activity log of the current deployment as well as the past ones [here](https://github.com/scanapi/demo-api/deployments).
