from app.database.repositories.user_repository import UserRepository


class AuthService:
    """
    Handles the business logic for authentication (login, register).
    """

    @staticmethod
    def register(name: str, username: str, email: str, password: str):
        # 1. Check if username already exists
        if UserRepository.get_by_username(username):
            return {
                "success": False,
                "error": "Username sudah dipakai. Silahkan pilih username lain.",
            }

        # 2. Check if email already exists
        if UserRepository.get_by_email(email):
            return {
                "success": False,
                "error": "Email sudah terdaftar. Silahkan gunakan email lain.",
            }

        # 3. If all checks pass, create the user
        try:
            new_user = UserRepository.create(
                name=name, username=username, email=email, password=password
            )
            return {"success": True, "user": new_user}
        except Exception as e:
            # Log the exception e for debugging
            return {
                "success": False,
                "error": "Terjadi kesalahan.",
            }

    @staticmethod
    def login(username: str, password: str):
        # 1. Find the user by username
        user = UserRepository.get_by_username(username)

        # 2. Check if user exists and if the password is correct
        if not user or not user.check_password(password):
            return {
                "success": False,
                "error": "Username atau password salah. Silahkan coba lagi.",
            }

        # 3. If credentials are valid, return success
        return {"success": True, "user": user}
