import 'package:flutter_riverpod/legacy.dart';

import 'auth_session.dart';
import 'token_store.dart';

class AuthSessionController extends StateNotifier<AuthSession> {
  final TokenStore _tokenStore;

  AuthSessionController(this._tokenStore) : super(AuthSession.unauthenticated);

  Future<void> hydrate() async {
    final tokens = await _tokenStore.read();

    if (tokens == null) {
      state = AuthSession.unauthenticated;
      return;
    }

    if (tokens.isAccessTokenExpired && tokens.refreshToken.isEmpty) {
      state = AuthSession.unauthenticated;
      return;
    }

    state = AuthSession.authenticated;
  }

  void setAuthenticated() => state = AuthSession.authenticated;
  void setUnauthenticated() => state = AuthSession.unauthenticated;

  Future<void> logout() async {
    await _tokenStore.clear();
    setUnauthenticated();
  }
}
