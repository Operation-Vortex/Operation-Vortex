import 'package:dio/dio.dart';
import 'auth_repository.dart';
import 'auth_session_controller.dart';
import 'token_pair.dart';
import 'token_store.dart';

class AuthRepositoryImpl implements AuthRepository {
  final Dio _dio;
  final TokenStore _tokenStore;
  final AuthSessionController _sessionController;

  AuthRepositoryImpl({
    required Dio dio,
    required TokenStore tokenStore,
    required AuthSessionController sessionController,
  }) : _dio = dio,
       _tokenStore = tokenStore,
       _sessionController = sessionController;

  @override
  Future<bool> login({
    required String identifier,
    required String password,
  }) async {
    try {
      final response = await _dio.post(
        '/auth/login/',
        data: {'identifier': identifier, 'password': password},
      );

      final data = response.data;
      final accessToken = data['access']?.toString() ?? '';
      final refreshToken = data['refresh']?.toString() ?? '';

      if (accessToken.isEmpty || refreshToken.isEmpty) return false;

      await _tokenStore.write(
        TokenPair(accessToken: accessToken, refreshToken: refreshToken),
      );

      _sessionController.setAuthenticated();
      return true;
    } catch (e) {
      return false;
    }
  }

  @override
  Future<void> logout() async {
    await _tokenStore.clear();
    _sessionController.setUnauthenticated();
  }
}
