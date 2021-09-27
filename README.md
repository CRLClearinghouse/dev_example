# Civil Rights Litigation Clearinghouse - Coding Task

The [Civil Rights Litigation Clearinghouse](https://clearinghouse.net), a project of the University of Michigan Law School, is seeking a part-time, remote (within the U.S.) full-stack developer. For more information about the role, see [the job posting](https://careers.umich.edu/job_detail/204257/full_stack_developer).

The purpose of this coding task is to demonstrate your abilities with Python, Django, and dealing with database data. It's intended to take 1-2 hours.

# Setup

## Cloning the Repository and Creating Your Own Mirror

To keep your submission private, you should create your own private repository that [mirrors this one](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository).

1. [Create a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
2. Create a bare clone of this repository:

```bash
$ git clone --bare https://github.com/CRLClearinghouse/dev_example.git
```

3. Mirror-push to your new repository:

```bash
$ cd dev_example
$ git push --mirror https://github.com/your-username/your-new-repository.git
```

4. Now remove your local directory for this repository, and clone your own repository:

```bash
$ cd ..
$ rm -r dev_example
$ git clone https://github.com/your-username/your-new-repository.git
```

5. Finally, create a new branch for your changes:

```bash
$ cd your-new-repository
$ git checkout -b your-branch-name
```

## Running the Server

Before starting on your changes, make sure you can run the server locally.

1. Install the dependencies:

```bash
$ pip install -r requirements.txt
```

*(Depending on your Python setup, you might need to use `pip3` instead of `pip`.)*

2. Download the Data:

```bash
$ wget https://www.dropbox.com/s/z9vnmd6vj8na45t/data.zip
```

(Or you can download it by visiting the Dropbox URL.) Once downloaded, you should also unzip the data:

```bash
$ unzip data.zip
```

3. Run the server:

```bash
$ python manage.py server
```

*(Depending on your Python setup, you might need to use `python3` instead of `python`.)*

Test your connection by going to http://127.0.0.1:8000/ and look for the text "Clearinghouse app is running!"

# Tasks

One thing the Clearinghouse keeps track of is people who are involved in the litigation of cases, e.g. attorneys and judges. The goal of this is to import people data into this Django project.

In this repository is a bare-bones Django project. There is an app called `clearinghouse` that already has two models: `Court` and `Person`. The data you downloaded includes an excerpt of data exported from three tables in the Clearinghouse: `chCourts`, `chPeople`, and `chPeopleCourts`. You have three tasks:

1. Import the first and last names of the entries in the `chPeople` table to the existing `Person` model. The only required fields are `first_name` and `last_name`, but you may extend the `Person` model and add additional fields if doing so makes it easier to complete the remaining tasks.
2. Create a model named `PersonCourt` for the data in `chPeopleCourts`. This data relates courts with judges in order to convey when a judge started working at a court. Some judges have worked at multiple courts.
3. Import the `chPeopleCourts` data into the model you created, preserving the appropriate relationships to `Person` and `Court`. You should ignore rows where the `personId` does not match the `id` of a row in `chPeople.csv`. (Hint: In the `Court` model, `ch_id` is the legacy court ID.)

You may use Google, Stack Overflow, Python/Django docs, etc. as resources. In addition, here are some potentially helpful links to Django documentation (you do not have to use these in your solution):

* [Using `save()` to save Python objects into the database](https://docs.djangoproject.com/en/3.2/ref/models/instances/#saving-objects)
* Relationships between models:
  * [Many-to-one](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one)
  * [Many-to-many](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many)
  * [One-to-one](https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one)
* [Running a Python shell](https://docs.djangoproject.com/en/dev/ref/django-admin/#shell)
  * [Running a Python script](https://stackoverflow.com/a/16853799)

As mentioned above, we don't intend for you to spend more than 1-2 hours on this task, and would rather see a partial submission than have you spend longer than 2 hours working on this. Good luck!

# Submission

1. [Create a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) in your repository with the code you have written.
2. In the description of the pull request, include the following information:
   1. The counts of `Court`, `Person`, and `PersonCourt` entries that display when looking at http://127.0.0.1:8000/.
   2. Any testing of your code.
   3. Any explanation of design choices you think need explanation.
3. From your repository's page, under Settings > Manage Access, add MargoSchlanger and laurenyu as collaborators so that we can see your submission.
4. Notify us by emailing mschlan [at] umich [dot] edu.
