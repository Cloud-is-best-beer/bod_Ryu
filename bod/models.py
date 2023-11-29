from bod import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    # User 모델과 Post 모델 연결
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # Post 모델에서 User 모델을 참조
    user = db.relationship('User', backref=db.backref('post_set'))

    # 수정날짜
    modify_date = db.Column(db.DateTime(), nullable=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))

    # 수정날짜
    modify_date = db.Column(db.DateTime(), nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    phonenum = db.Column(db.String(100))
    email = db.Column(db.String(150))
    create_date = db.Column(db.DateTime(), nullable=False)

