from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from .. import db
from .auth_views import login_required
from ..forms import PostForm, CommentForm
from ..models import Post

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/modify/<int:post_id>', methods=('GET', 'POST'))
@login_required
def modify(post_id):
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('post.detail', post_id=post_id))
    if request.method == 'POST': # 수정 후 저장 버튼
        form=PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)     # form 변수에 들어 있는 데이터를 업데이트
            post.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('post.detail', post_id=post_id))
    else: # 수정 버튼
        # 이미 조회된 데이터는 obj 매개변수에 전달하는 것이 간단함
        # 제목, 내용이 화면에 바로 표시됨
        form=PostForm(obj=post)
    return render_template('post/post_form.html', form=form)


@bp.route('/delete/<int:post_id>')
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('post.detail', post_id=post_id))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post._list'))



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
