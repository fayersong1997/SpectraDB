from flask import Blueprint

# 给auth这个模块的路由前缀都加上了/auth
bp = Blueprint("auth", __name__, url_prefix="/auth")

# /auth/login
@bp.route('/login')
def login():
    pass