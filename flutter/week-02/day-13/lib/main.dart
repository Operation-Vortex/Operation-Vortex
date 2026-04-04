import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:navigation_demo/error_screen.dart';
import 'package:navigation_demo/home_screen.dart';
import 'package:navigation_demo/login_screen.dart';
import 'package:navigation_demo/profile_screen.dart';
import 'package:navigation_demo/screens/about_screen.dart';
import 'package:navigation_demo/settings_screen.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  MyApp({super.key});

  final GoRouter _router = GoRouter(
    redirect: (context, state) {
    final isLoggedIn = false; // hardcoded for now
    final isGoingToLogin = state.matchedLocation == '/login';

    if (!isLoggedIn && !isGoingToLogin) {
      return '/login';
    }

    return null; // null means "no redirect, continue normally"
  },
    errorBuilder: (context, state) => ErrorScreen(),
    routes: [
      GoRoute(path: '/', builder: (context, state) => const HomeScreen()),
      GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
      GoRoute(
        path: '/profile/:id',
        builder: (context, state) {
          final userId = state.pathParameters['id']!;
          return ProfileScreen(userId: userId);
        },
      ),
      GoRoute(
        path: '/settings',
        builder: (context, state) => const SettingsScreen(),
      ),
      GoRoute(path:   '/about', builder: (context, state) => const AboutScreen())
    ],
  );

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(routerConfig: _router);
  }
}
