class TokenPair {
  final String accessToken;
  final String refreshToken;
  final DateTime? accessTokenExpiresAt;

  TokenPair({
    required this.accessToken,
    required this.refreshToken,
    this.accessTokenExpiresAt,
  });

  bool get isAccessTokenExpired {
    if (accessTokenExpiresAt == null) return false;
    return DateTime.now().isAfter(accessTokenExpiresAt!);
  }
}
