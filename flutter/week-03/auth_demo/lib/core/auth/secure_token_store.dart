import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'token_pair.dart';
import 'token_store.dart';

class SecureTokenStore implements TokenStore {
  final FlutterSecureStorage _storage;

  static const _accessTokenKey = 'auth.access_token';
  static const _refreshTokenKey = 'auth.refresh_token';
  static const _expiresAtKey = 'auth.expires_at';

  const SecureTokenStore(this._storage);

  @override
  Future<void> write(TokenPair tokens) async {
    await _storage.write(key: _accessTokenKey, value: tokens.accessToken);
    await _storage.write(key: _refreshTokenKey, value: tokens.refreshToken);
    if (tokens.accessTokenExpiresAt != null) {
      await _storage.write(
        key: _expiresAtKey,
        value: tokens.accessTokenExpiresAt!.toIso8601String(),
      );
    }
  }

  @override
  Future<TokenPair?> read() async {
    final access = await _storage.read(key: _accessTokenKey);
    final refresh = await _storage.read(key: _refreshTokenKey);

    if (access == null || access.isEmpty) return null;
    if (refresh == null || refresh.isEmpty) return null;

    final expiresAtRaw = await _storage.read(key: _expiresAtKey);
    final expiresAt = expiresAtRaw != null
        ? DateTime.tryParse(expiresAtRaw)
        : null;

    return TokenPair(
      accessToken: access,
      refreshToken: refresh,
      accessTokenExpiresAt: expiresAt,
    );
  }

  @override
  Future<void> clear() async {
    await _storage.delete(key: _accessTokenKey);
    await _storage.delete(key: _refreshTokenKey);
    await _storage.delete(key: _expiresAtKey);
  }
}
