class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

try:
    raise DatabaseError("Something went wrong in the database")
except AppError as e:
    print(f"Caught: {e}")