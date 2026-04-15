class AuthSession {
  final bool? isAuthenticated;

  const AuthSession({required this.isAuthenticated});

  static const authenticated = AuthSession(isAuthenticated: true);
  static const unauthenticated = AuthSession(isAuthenticated: false);
}
