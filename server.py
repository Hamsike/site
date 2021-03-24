import datetime as dt
global_init(input())
db_sess = create_session()


class jobs(Jobs):
    def __repr__(self):
        return f'<Job> {Jobs.job}'


for el in db_sess.query(Jobs).filter(Jobs.is_finished == 0,
                                     dt.timedelta(Jobs.end_date - Jobs.start_date).microseconds < 72000000000):
    print(el)