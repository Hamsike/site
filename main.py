from data import db_session
from data.work import User
from data.jobs import Jobs

db_session.global_init("db/blogs.db")


def add_user(sur, name, age, pos, spec, ad, email):
    user = User()
    user.surname = sur
    user.name = name
    user.age = age
    user.pos = pos
    user.speciality = spec
    user.address = ad
    user.email = email
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def add_jobs(team, job, work, coll, start, is_f):
    jobs = Jobs()
    jobs.team_leader = team
    jobs.job = job
    jobs.work_size = work
    jobs.collaborators = coll
    jobs.start_date = start
    jobs.is_finished = is_f


users = [{
    'surname': 'Scott',
    'name': 'Ridley',
    'age': 21,
    'position': 'captain',
    'speciality': 'research engineer',
    'address': 'module_1',
    'email': 'scott_chief@mars.org'
}, {
    'surname': 'Melnik',
    'name': 'Ruslan',
    'age': 16,
    'position': 'captain',
    'speciality': 'research engineer',
    'address': 'module_1',
    'email': 'melnik_ruslan@mars.org'
},
    {'surname': 'Greb',
     'name': 'Ilya',
     'age': 15,
     'position': 'captain',
     'speciality': 'research engineer',
     'address': 'module_1',
     'email': 'greb_ilya@mars.org'
     },

    {'surname': 'Erbulatov',
     'name': 'Hamit',
     'age': 17,
     'position': 'captain',
     'speciality': 'research engineer',
     'address': 'module_1',
     'email': 'erbulatov_hamit@mars.org'}]

[add_user(*value.values()) for value in users]
