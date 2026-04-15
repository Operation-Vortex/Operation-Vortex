import 'package:dio/dio.dart';
import 'token_store.dart';

class AuthInterceptor extends Interceptor {
  final TokenStore _tokenStore;

  AuthInterceptor(this._tokenStore);

  @override
  Future<void> onRequest(
    RequestOptions options,
    RequestInterceptorHandler handler,
  ) async {
    final tokens = await _tokenStore.read();

    if (tokens != null && tokens.accessToken.isNotEmpty) {
      options.headers['Authorization'] = 'Bearer ${tokens.accessToken}';
    }

    handler.next(options);
  }
}
