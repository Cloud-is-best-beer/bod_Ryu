from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for, g
from werkzeug.utils import redirect

from .. import db
from .auth_views import login_required
from ..forms import PostForm, CommentForm
from ..models import Post

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/list/')
def _list():
    # GET 방식으로 요청한 URL에서 page값을 가져옴
    page = request.args.get('page', type=int, default=1)
    post_list = Post.query.order_by(Post.create_date.desc())
    # paginate 함수로 페이징을 적용
    # 첫번째 인수인 page는 현재 조회할 페이지의 번호
    # 두번째 인수인 per_page는 페이지마다 보여줄 post 개수
    post_list = post_list.paginate(page=page, per_page=10)
    return render_template('post/post_list.html', post_list=post_list)



@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    form=CommentForm()
    post = Post.query.get_or_404(post_id)
    return render_template('post/post_detail.html', post=post, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(subject=form.subject.data, content=form.content.data,
                    create_date=datetime.now(), user=g.user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('post/post_form.html', form=form)
