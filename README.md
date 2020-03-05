# Setup

To get up and running, it should be as easy as:

```sh
# `cd` to the project directory.
echo "cd path/stuff/demo_models"

# Create a new virtual environment.
python3 -m venv .venv

# Load the venv.
source .venv/bin/activate

# Install the necessary modules (and dependencies).
python3 -m pip install -r requirements.txt
```

You'll also probably want to create the database:

```sh
# The upgrade process also handles the "no db yet" scenario.
flask db upgrade
```

# Test Drive

There's no actual website to go along with this demo. Just use the python shell.

```sh
# Launch a python interpreter with predefined variables.
flask shell
```

## Sample transcript:

```
>>> p1 = Person(username='alice', color='Aqua')
>>> db.session.add(p1)
>>> db.session.commit()
>>> p2 = Person(username='bob', color='Bright Blue')
>>> db.session.add(p2)
>>> db.session.commit()
>>> people = Person.query.all()
>>> people
[<Person alice>, <Person bob>]
>>> for p in people:
...     print(p.id, p.username, p.color)
... 
1 alice Aqua
2 bob Bright Blue
>>> p = Person.query.get(1)
>>> p
<Person alice>
>>> m = Message(body="Amazing announcement!", author=p)
>>> db.session.add(m)
>>> db.session.commit()
>>> messages = p.messages.all()
>>> messages
[<Message Amazing announcement!>]
>>> messages = Message.query.all()
>>> for m in messages:
...     print(m.id, m.author.username, m.body)
... 
1 alice Amazing announcement!
>>> exit()
```
