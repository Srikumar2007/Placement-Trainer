import auth
try:
    h = auth.get_password_hash("password123")
    print(f"Hash success: {h}")
except Exception as e:
    print(f"Hash failed: {e}")
    import traceback
    traceback.print_exc()
