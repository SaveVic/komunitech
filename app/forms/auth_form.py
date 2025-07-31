from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.database.repositories.user_repository import UserRepository


class RegistrationForm(FlaskForm):
    """
    Form untuk pengguna membuat akun baru.
    """

    name = StringField(
        "Nama Lengkap", validators=[DataRequired(message="Nama tidak boleh kosong.")]
    )
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username tidak boleh kosong."),
            Length(
                min=4,
                max=25,
                message="Username harus memiliki panjang antara 4 dan 25 karakter.",
            ),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email tidak boleh kosong."),
            Email(message="Alamat email tidak valid."),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password tidak boleh kosong."),
            Length(min=6, message="Password minimal harus 6 karakter."),
        ],
    )
    confirm_password = PasswordField(
        "Konfirmasi Password",
        validators=[
            DataRequired(message="Konfirmasi password tidak boleh kosong."),
            EqualTo("password", message="Konfirmasi password tidak cocok."),
        ],
    )
    submit = SubmitField("Daftar")


class LoginForm(FlaskForm):
    """
    Form untuk pengguna masuk ke akun.
    """

    username = StringField(
        "Username", validators=[DataRequired(message="Username tidak boleh kosong.")]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Password tidak boleh kosong.")]
    )
    remember_me = BooleanField("Ingat Saya")
    submit = SubmitField("Masuk")
