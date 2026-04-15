abstract class AuthRepository {
  Future<bool> login({required String identifier, required String password});

  Future<void> logout();
}
